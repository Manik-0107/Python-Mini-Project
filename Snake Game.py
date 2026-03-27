# Install Library: pip install pygame

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
speed = 10

# Font
font = pygame.font.SysFont('Arial', 25)

def draw_text(text, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def game_loop():
    snake = [(100, 100)]
    direction = "RIGHT"

    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    score = 0

    while True:
        screen.fill(BLACK)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # MOve Snake
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= BLOCK_SIZE
        elif direction == "DOWN":
            head_y += BLOCK_SIZE
        elif direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)

        # Collision with wall
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return score

        # Collision with itself
        if new_head in snake:
            return score

        snake.insert(0, new_head)

        # Food Collision
        if head_x == food_x and head_y == food_y:
            score += 1
            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)
        else:
            snake.pop()

        # Draw food
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        # Draw Snake
        for block in snake:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw score
        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.update()
        clock.tick(speed)

def game_over(score):
    while True:
        screen.fill(BLACK)
        draw_text(f"Game over! Score: {score}", RED, 150, 150)
        draw_text("Press R to Restart or Q to Quit", WHITE, 120, 200)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Main Loop
while True:
    score = game_loop()
    game_over(score)
