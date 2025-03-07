"""
Made by 5quirre1 on 3/6/2025 at 6:49 PM
no license or copyright cause it's pong so uhh use if ya want or some shit
"""
import os
try:
    import pygame
except ImportError:
    os.system("pip install pygame")
    import pygame
import random


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")


white = (255, 255, 255)
black = (0, 0, 0)


paddle_width, paddle_height = 10, 100
paddle_speed = 5


paddle_a = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_a_speed = 0


paddle_b = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_b_speed = 0
ai_speed = 4 


ball_size = 10
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))


score_a = 0
score_b = 0
font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_a_speed = -paddle_speed
            if event.key == pygame.K_s:
                paddle_a_speed = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_a_speed = 0


    paddle_a.y += paddle_a_speed
    paddle_a.y = max(0, min(paddle_a.y, height - paddle_height))


    if ball.y < paddle_b.y + paddle_height // 2:
        paddle_b.y -= ai_speed
    elif ball.y > paddle_b.y + paddle_height // 2:
        paddle_b.y += ai_speed
    paddle_b.y = max(0, min(paddle_b.y, height - paddle_height))


    ball.x += ball_speed_x
    ball.y += ball_speed_y

 
    if ball.y <= 0 or ball.y >= height - ball_size:
        ball_speed_y *= -1


    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1.05  
        ball_speed_y *= 1.05


    if ball.x <= 0:
        score_b += 1
        ball.x = width // 2 - ball_size // 2
        ball.y = height // 2 - ball_size // 2
        ball_speed_x = 4 * random.choice((1, -1))
        ball_speed_y = 4 * random.choice((1, -1))
    if ball.x >= width - ball_size:
        score_a += 1
        ball.x = width // 2 - ball_size // 2
        ball.y = height // 2 - ball_size // 2
        ball_speed_x = 4 * random.choice((1, -1))
        ball_speed_y = 4 * random.choice((1, -1))

    screen.fill(black)
    pygame.draw.rect(screen, white, paddle_a)
    pygame.draw.rect(screen, white, paddle_b)
    pygame.draw.rect(screen, white, ball)
    text = font.render(f"Player: {score_a}  AI: {score_b}", True, white)
    screen.blit(text, (width // 2 - text.get_width() // 2, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
