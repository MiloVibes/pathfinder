import pygame
import pygame.font
from utilities import make_grid, draw_grid, get_clicked_pos
from algorithm import algorithm
from node import *

# Initialize pygame
pygame.init()

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Caveman Survival")
FONT = pygame.font.SysFont("comicsans", 40)

def draw(win, grid, rows, width):
    win.fill((0, 255, 0))  # Assume GREEN is defined here

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def show_message(win, message, duration=1500):
    win.fill((0, 0, 0))  # Fill the background to make the text more readable
    text = FONT.render(message, True, (255, 255, 255))  # White color for the text
    text_rect = text.get_rect(center=(WIDTH / 2, WIDTH / 2))  # Center the text
    win.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(duration)  # Display the message for specified duration in milliseconds

def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            WIN.blit(FONT.render(l, 0), (x, y + fsize*i))

def show_story(win):
    story_parts = [

        "Long before the age of technology, ",
        "in a world where danger lurked",
        "in every shadow...",
        "...a small tribe of cavemen ",
        "embarked on a quest for safety, ",
        "their survival hanging by a thread.",
        "Their journey was fraught with peril, ",
        "Facing the colossal dinosaurs that ruled...",
        "...but with cunning and unity, ",
        "They sought to outsmart these behemoths, ",
        "Securing a future for their kin.",
        "This is their tale. And with new tech.",
        "THEY WILL SURVIVE!!!!!!"
    ]
    for part in story_parts:
        show_message(win, part, 1500)

def show_start_message(win):
    messages = [
        "Welcome to Caveman Survival!.",
        "1st click to place caveman house.",
        "2nd click to place destination.",
        "Rest of clicks create or remove obstacles.",
        "Press SPACE to start the algorithm.",
        "Press 'R' to reset the grid.",
        "Press any key to continue...",
    ]
    win.fill((0, 0, 0))  # Fill the screen with black
    y_offset = 50  # Start a bit down from the top of the window
    for message in messages:
        text_surface = FONT.render(message, True, (200, 200, 200))  # Render the text
        text_rect = text_surface.get_rect(center=(WIDTH / 2, y_offset))
        win.blit(text_surface, text_rect)
        y_offset += 50  # Move down for the next line
    pygame.display.update()

    # Wait for a key press to continue
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True  # Indicate we should quit
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False
    return False  # Indicate it's okay to proceed

def main(win, width):
    show_story(win)  # Show the story before starting the game
    
    should_quit = show_start_message(win)
    if should_quit:
        return  # Exit if the startup message procedure requested a quit

    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    dragging = False  # Keep track of whether we're dragging to create barriers

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if pygame.mouse.get_pressed()[0]:  # LEFT button down
                    if not start and node != end:
                        start = node
                        start.make_start()
                    elif not end and node != start:
                        end = node
                        end.make_end()
                    else:
                        if node != end and node != start:
                            node.make_barrier()
                            dragging = True  # Start dragging
                elif pygame.mouse.get_pressed()[2]:  # RIGHT button down
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None
                    dragging = False  # Stop dragging for right click

            if event.type == pygame.MOUSEMOTION and dragging:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if node != start and node != end:
                    node.make_barrier()

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False  # Stop dragging on mouse button release

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end and not dragging:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    started = True
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    started = False

                if event.key == pygame.K_r:  # Resetting the game
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    dragging = False  # Ensure dragging is reset on grid reset

    pygame.quit()


if __name__ == "__main__":
    main(WIN, WIDTH)
