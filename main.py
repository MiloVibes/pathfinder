import pygame
import pygame.font
from utilities import make_grid, draw_grid, get_clicked_pos
from algorithm import algorithm  # Ensure this is updated to return a boolean
from node import *

# Initialize pygame
pygame.init()

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Caveman Survival")
FONT = pygame.font.SysFont("comicsans", 40)

def draw(win, grid, rows, width):
    win.fill(GREEN)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def show_message(win, message):
    text = FONT.render(message, True, (255, 0, 0))
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, WIDTH / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)  # Display the message for 2 seconds

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    started = True
                    path_found = algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    started = False
                    if not path_found:
                        show_message(win, "No available paths!")

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_r:  # Resetting the game
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

if __name__ == "__main__":
    main(WIN, WIDTH)
