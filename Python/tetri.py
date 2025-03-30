import pygame
import random
import time
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GRAY = (40, 40, 40)
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1], [1, 1]],  
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]]
]
COLORS = [CYAN, PURPLE, BLUE, ORANGE, YELLOW, GREEN, RED]
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 25)
        self.big_font = pygame.font.SysFont('Arial', 50, bold=True)
        self.reset_game()
    def reset_game(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.game_over_animation = False
        self.game_over_animation_start = 0
        self.game_over_fill_rows = []
        self.game_over_fill_progress = 0
        self.score = 0
        self.level = 1
        self.fall_speed = 0.5
        self.fall_time = 0
        self.paused = False
        self.animating = False
        self.animation_rows = []
        self.animation_start_time = 0
        self.animation_duration = 0.5 
    def new_piece(self):
        shape_idx = random.randint(0, len(SHAPES) - 1)
        return {
            'shape': SHAPES[shape_idx],
            'color': COLORS[shape_idx],
            'x': GRID_WIDTH // 2 - len(SHAPES[shape_idx][0]) // 2,
            'y': 0,
            'rotation': 0
        }
    def rotate_piece(self, piece, clockwise=True):
        shape = piece['shape']
        if clockwise:
            return [list(row) for row in zip(*shape[::-1])]
        else:
            return [list(row) for row in zip(*shape)][::-1]
    def valid_position(self, shape, x, y):
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    if (y + i >= GRID_HEIGHT or 
                        x + j < 0 or 
                        x + j >= GRID_WIDTH or 
                        (y + i >= 0 and self.grid[y + i][x + j])):
                        return False
        return True
    def add_to_grid(self):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + i][self.current_piece['x'] + j] = self.current_piece['color']
    def check_full_rows(self):
        full_rows = []
        for i, row in enumerate(self.grid):
            if all(row):
                full_rows.append(i)
        if full_rows:
            self.animation_rows = full_rows
            self.animating = True
            self.animation_start_time = time.time()
        return full_rows
    def clear_rows(self):
        if not self.animation_rows:
            return 0
        rows_to_clear = self.animation_rows
        for row_idx in sorted(rows_to_clear, reverse=True):
            self.grid.pop(row_idx)
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        cleared_count = len(rows_to_clear)
        self.animation_rows = []
        self.animating = False
        return cleared_count
    def update_score(self, cleared_rows):
        if cleared_rows == 1:
            self.score += 100 * self.level
        elif cleared_rows == 2:
            self.score += 300 * self.level
        elif cleared_rows == 3:
            self.score += 500 * self.level
        elif cleared_rows == 4:
            self.score += 800 * self.level
        if self.score >= self.level * 1000:
            self.level += 1
            self.fall_speed = max(0.05, self.fall_speed * 0.8)
    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(
                    self.screen, 
                    GRAY, 
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    1
                )
                if self.grid[y][x]:
                    is_animating_row = y in self.animation_rows
                    if is_animating_row:
                        animation_progress = (time.time() - self.animation_start_time) / self.animation_duration
                        flash_intensity = abs(((animation_progress * 12) % 2) - 1)
                        original_color = self.grid[y][x]
                        r = int(original_color[0] + (255 - original_color[0]) * flash_intensity)
                        g = int(original_color[1] + (255 - original_color[1]) * flash_intensity)
                        b = int(original_color[2] + (255 - original_color[2]) * flash_intensity)
                        color = (r, g, b)
                    else:
                        color = self.grid[y][x]
                    pygame.draw.rect(
                        self.screen, 
                        color, 
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    )
                    pygame.draw.rect(
                        self.screen, 
                        WHITE, 
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 
                        1
                    )
        pygame.draw.rect(
            self.screen, 
            WHITE, 
            (0, 0, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), 
            2
        )
    def draw_ghost_piece(self):
        if self.game_over or self.animating or self.game_over_animation:
            return
        ghost_y = self.current_piece['y']
        while self.valid_position(self.current_piece['shape'], 
                                self.current_piece['x'], 
                                ghost_y + 1):
            ghost_y += 1
        if ghost_y > self.current_piece['y']:
            for i, row in enumerate(self.current_piece['shape']):
                for j, cell in enumerate(row):
                    if cell:
                        ghost_color = self.current_piece['color']
                        pygame.draw.rect(
                            self.screen, 
                            (ghost_color[0]//2, ghost_color[1]//2, ghost_color[2]//2), 
                            ((self.current_piece['x'] + j) * BLOCK_SIZE, 
                            (ghost_y + i) * BLOCK_SIZE, 
                            BLOCK_SIZE, BLOCK_SIZE),
                            1
                        )
    def draw_current_piece(self):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen, 
                        self.current_piece['color'], 
                        ((self.current_piece['x'] + j) * BLOCK_SIZE, 
                         (self.current_piece['y'] + i) * BLOCK_SIZE, 
                         BLOCK_SIZE, BLOCK_SIZE)
                    )
                    pygame.draw.rect(
                        self.screen, 
                        WHITE, 
                        ((self.current_piece['x'] + j) * BLOCK_SIZE, 
                         (self.current_piece['y'] + i) * BLOCK_SIZE, 
                         BLOCK_SIZE, BLOCK_SIZE), 
                        1
                    )
    def draw_next_piece(self):
        info_x = GRID_WIDTH * BLOCK_SIZE + 20
        title = self.font.render("Next:", True, WHITE)
        self.screen.blit(title, (info_x, 20))
        next_piece = self.next_piece
        for i, row in enumerate(next_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen, 
                        next_piece['color'], 
                        (info_x + j * BLOCK_SIZE, 
                         60 + i * BLOCK_SIZE, 
                         BLOCK_SIZE, BLOCK_SIZE)
                    )
                    pygame.draw.rect(
                        self.screen, 
                        WHITE, 
                        (info_x + j * BLOCK_SIZE, 
                         60 + i * BLOCK_SIZE, 
                         BLOCK_SIZE, BLOCK_SIZE), 
                        1
                    )
    def draw_info(self):
        info_x = GRID_WIDTH * BLOCK_SIZE + 20
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (info_x, 150))
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (info_x, 180))
        if not self.game_over and not self.game_over_animation:
            controls = [
                "Controls:",
                "↑: Hard Drop",
                "←→: Move",
                "↓: Soft Drop",
                "Z/X: Rotate",
                "P: Pause"
            ]
        else:
            controls = [
                "dw!!!", "you did good!"
            ]
        for i, text in enumerate(controls):
            ctrl_text = self.font.render(text, True, WHITE)
            self.screen.blit(ctrl_text, (info_x, 230 + i * 30))
    def start_game_over_animation(self):
        self.game_over_animation = True
        self.game_over_animation_start = time.time()
        self.game_over_fill_rows = list(range(GRID_HEIGHT))
        self.game_over_fill_progress = 0
    def update_game_over_animation(self, delta_time):
        if not self.game_over_animation:
            return
        time_since_start = time.time() - self.game_over_animation_start
        total_animation_time = 1.5  
        target_fill_progress = min(GRID_HEIGHT, int((time_since_start / total_animation_time) * GRID_HEIGHT))
        while self.game_over_fill_progress < target_fill_progress and self.game_over_fill_rows:
            row_to_fill = GRID_HEIGHT - self.game_over_fill_progress - 1
            if row_to_fill >= 0:
                random_color = random.choice(COLORS)
                for x in range(GRID_WIDTH):
                    self.grid[row_to_fill][x] = random_color
            self.game_over_fill_progress += 1
        if self.game_over_fill_progress >= GRID_HEIGHT:
            self.game_over = True
            self.game_over_animation = False
    def draw_game_over(self):
        if not self.game_over:
            return
        overlay = pygame.Surface((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        game_over_text = self.big_font.render("aww.. gg", True, WHITE)
        text_rect = game_over_text.get_rect(center=(GRID_WIDTH * BLOCK_SIZE // 2, 
                                                  GRID_HEIGHT * BLOCK_SIZE // 2 - 30))
        self.screen.blit(game_over_text, text_rect)
        restart_text = self.font.render("press R to restart..", True, WHITE)
        restart_rect = restart_text.get_rect(center=(GRID_WIDTH * BLOCK_SIZE // 2, 
                                                   GRID_HEIGHT * BLOCK_SIZE // 2 + 30))
        self.screen.blit(restart_text, restart_rect)
    def hard_drop(self):
        while self.valid_position(self.current_piece['shape'], 
                                self.current_piece['x'], 
                                self.current_piece['y'] + 1):
            self.current_piece['y'] += 1
        self.add_to_grid()
        full_rows = self.check_full_rows()
        if not full_rows:
            self.current_piece = self.next_piece
            self.next_piece = self.new_piece()
            if not self.valid_position(self.current_piece['shape'], 
                                     self.current_piece['x'], 
                                     self.current_piece['y']):
                self.start_game_over_animation()
    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(60) / 1000
            if self.game_over_animation:
                self.update_game_over_animation(delta_time)
            if self.animating:
                if time.time() - self.animation_start_time >= self.animation_duration:
                    cleared_rows = self.clear_rows()
                    self.update_score(cleared_rows)
                    self.current_piece = self.next_piece
                    self.next_piece = self.new_piece()
                    if not self.valid_position(self.current_piece['shape'], 
                                             self.current_piece['x'], 
                                             self.current_piece['y']):
                        self.start_game_over_animation()
            if not self.paused and not self.game_over and not self.animating and not self.game_over_animation:
                self.fall_time += delta_time
                if self.fall_time >= self.fall_speed:
                    self.fall_time = 0
                    self.current_piece['y'] += 1
                    if not self.valid_position(self.current_piece['shape'], 
                                             self.current_piece['x'], 
                                             self.current_piece['y']):
                        self.current_piece['y'] -= 1
                        self.add_to_grid()
                        full_rows = self.check_full_rows()
                        if not full_rows:
                            self.current_piece = self.next_piece
                            self.next_piece = self.new_piece()
                            if not self.valid_position(self.current_piece['shape'], 
                                                     self.current_piece['x'], 
                                                     self.current_piece['y']):
                                self.start_game_over_animation()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game_over or self.game_over_animation:
                        if event.key == pygame.K_r:
                            self.reset_game()
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused
                    elif not self.paused and not self.animating:
                        if event.key == pygame.K_LEFT:
                            self.current_piece['x'] -= 1
                            if not self.valid_position(self.current_piece['shape'], 
                                                    self.current_piece['x'], 
                                                    self.current_piece['y']):
                                self.current_piece['x'] += 1
                        elif event.key == pygame.K_RIGHT:
                            self.current_piece['x'] += 1
                            if not self.valid_position(self.current_piece['shape'], 
                                                    self.current_piece['x'], 
                                                    self.current_piece['y']):
                                self.current_piece['x'] -= 1
                        elif event.key == pygame.K_DOWN:
                            self.current_piece['y'] += 1
                            if not self.valid_position(self.current_piece['shape'], 
                                                    self.current_piece['x'], 
                                                    self.current_piece['y']):
                                self.current_piece['y'] -= 1
                        elif event.key == pygame.K_z:
                            rotated_shape = self.rotate_piece(self.current_piece, False)
                            if self.valid_position(rotated_shape, 
                                                self.current_piece['x'], 
                                                self.current_piece['y']):
                                self.current_piece['shape'] = rotated_shape
                        elif event.key == pygame.K_x:
                            rotated_shape = self.rotate_piece(self.current_piece, True)
                            if self.valid_position(rotated_shape, 
                                                self.current_piece['x'], 
                                                self.current_piece['y']):
                                self.current_piece['shape'] = rotated_shape
                        elif event.key == pygame.K_UP:
                            self.hard_drop()
            self.screen.fill(BLACK)
            self.draw_grid()
            if not self.game_over and not self.animating and not self.game_over_animation:
                self.draw_ghost_piece()
                self.draw_current_piece()
            self.draw_next_piece()
            self.draw_info()
            self.draw_game_over()
            if self.paused and not self.game_over and not self.game_over_animation:
                pause_text = self.font.render("PAUSED", True, WHITE)
                text_rect = pause_text.get_rect(center=(GRID_WIDTH * BLOCK_SIZE // 2, 
                                                      GRID_HEIGHT * BLOCK_SIZE // 2))
                self.screen.blit(pause_text, text_rect)
            pygame.display.update()
        pygame.quit()
if __name__ == "__main__":
    game = Tetris()
    game.run()
