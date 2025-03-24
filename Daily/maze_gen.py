import pygame
import random
import sys
import time
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("oooo pretty")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True]  
    def draw(self):
        x = self.x * CELL_SIZE
        y = self.y * CELL_SIZE
        if self.visited:
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
        if self.walls[0]:  
            pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 2)
        if self.walls[1]:  
            pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
        if self.walls[2]:  
            pygame.draw.line(screen, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
        if self.walls[3]:  
            pygame.draw.line(screen, WHITE, (x, y), (x, y + CELL_SIZE), 2)
    def get_neighbors(self, grid):
        neighbors = []
        for i, (dx, dy) in enumerate(DIRECTIONS):
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                if not grid[ny][nx].visited:
                    neighbors.append((grid[ny][nx], i))
        return neighbors
    def remove_wall(self, other, direction):
        self.walls[direction] = False
        other.walls[(direction + 2) % 4] = False
def generate_maze():
    grid = [[Cell(x, y) for x in range(COLS)] for y in range(ROWS)]
    current = grid[random.randint(0, ROWS-1)][random.randint(0, COLS-1)]
    current.visited = True
    stack = [current]
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(BLACK)
        for row in grid:
            for cell in row:
                cell.draw()
        x = current.x * CELL_SIZE
        y = current.y * CELL_SIZE
        pygame.draw.rect(screen, BLUE, (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4))
        if stack:
            neighbors = current.get_neighbors(grid)
            if neighbors:
                next_cell, direction = random.choice(neighbors)
                current.remove_wall(next_cell, direction)
                next_cell.visited = True
                stack.append(next_cell)
                current = next_cell
            else:
                current = stack.pop()
                if stack:
                    x = current.x * CELL_SIZE
                    y = current.y * CELL_SIZE
                    pygame.draw.rect(screen, GREEN, (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4))
        else:
            pygame.display.flip()
            time.sleep(2)  
            grid = [[Cell(x, y) for x in range(COLS)] for y in range(ROWS)]
            current = grid[random.randint(0, ROWS-1)][random.randint(0, COLS-1)]
            current.visited = True
            stack = [current]
        pygame.display.flip()
        clock.tick(30)  
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    generate_maze()
