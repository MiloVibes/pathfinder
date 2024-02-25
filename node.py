import pygame

# Define colors
GREEN = (34, 139, 34)  
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

# Loads the images for dinosaurs and cavemen
DINOSAUR_IMG = pygame.image.load('images/dinosaur.png')
CAVEMAN_START_IMG = pygame.image.load('images/caveman_start.png')
CAVEMAN_END_IMG = pygame.image.load('images/caveman_end.png')

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = GREEN  # This will be the default color for empty node 
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.image = None  # Displays specific images for start, end, and barrier nodes

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.color = WHITE
        self.image = None

    def make_start(self):
        self.image = CAVEMAN_START_IMG

    def make_closed(self):
        self.color = RED
        self.image = None  

    def make_open(self):
        self.color = GREEN
        self.image = None  

    def make_barrier(self):
        self.image = DINOSAUR_IMG

    def make_end(self):
        self.image = CAVEMAN_END_IMG

    def make_path(self):
        self.color = PURPLE
        self.image = None 

    def draw(self, win):
        if self.image:
            win.blit(pygame.transform.scale(self.image, (self.width, self.width)), (self.x, self.y))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            row, col = self.row + dx, self.col + dy
            if 0 <= row < self.total_rows and 0 <= col < self.total_rows and not grid[row][col].is_barrier():
                self.neighbors.append(grid[row][col])

    def is_barrier(self):
        return self.image == DINOSAUR_IMG

    def __lt__(self, other):
        return False
