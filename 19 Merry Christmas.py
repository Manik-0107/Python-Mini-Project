# Project name: Wish for Merry Christmas Day --> 25-12-2025

import pygame
import random
import math
import sys

pygame.init()

# Window
W, H = 900, 650
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("🎄 Merry Christmas 🎄")
clock = pygame.time.Clock()

# Colors
BG = (10, 12, 18)
GOLD = (255, 220, 140)
RED = (255, 90, 90)
WHITE = (245, 245, 255)
BLUE = (180, 220, 255)

# Fonts
font_big = pygame.font.SysFont("georgia", 44, True)
font_small = pygame.font.SysFont("georgia", 26)

# Load tree image (EXACT SHAPE)
tree = pygame.image.load("tree.png").convert_alpha()
tree = pygame.transform.smoothscale(tree, (360, 520))
tree_x, tree_y = W//2 - 180, 70

# Snow particles
snow = [[random.randint(0, W), random.randint(0, H), random.randint(1, 3)]
        for _ in range(200)]

# Fireflies
fireflies = [[random.randint(250, 650), random.randint(150, 480),
              random.uniform(0, 2*math.pi)] for _ in range(30)]

# Light positions (manual style)
lights = []
for y in range(170, 480, 35):
    for x in range(310, 590, 50):
        lights.append([x, y, random.choice([GOLD, RED]), random.uniform(0, 3)])

# Wishes with emojis
wishes = [
    "🎄 Merry Christmas 🎄",
    "✨ May your life shine bright ✨",
    "🎁 Wishing you love & happiness 🎁",
    "❄️ Peace, Joy & Warmth ❄️",
    "🌟 Have a Magical Christmas 🌟",
    "❤️ With Love & Smiles ❤️"
]

# Soft circular glow (NO SQUARE)
def glow(x, y, r, color, strength=120):
    surf = pygame.Surface((r*6, r*6), pygame.SRCALPHA)
    for i in range(6, 0, -1):
        alpha = max(0, strength - i*18)
        pygame.draw.circle(
            surf,
            (color[0], color[1], color[2], alpha),
            (r*3, r*3),
            r + i*2
        )
    screen.blit(surf, (x - r*3, y - r*3))

# Main loop
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG)

    # Snowfall
    for s in snow:
        pygame.draw.circle(screen, WHITE, (s[0], s[1]), s[2])
        s[1] += s[2]
        if s[1] > H:
            s[0] = random.randint(0, W)
            s[1] = random.randint(-40, 0)

    # Tree
    screen.blit(tree, (tree_x, tree_y))

    t = pygame.time.get_ticks() / 400

    # Tree lights (twinkle + pulse)
    for l in lights:
        pulse = abs(math.sin(t + l[3]))
        glow(l[0], l[1], int(3 + pulse*2), l[2], int(90 + 80*pulse))

    # Firefly sparkles
    for f in fireflies:
        f[2] += 0.02
        x = f[0] + math.sin(f[2]) * 20
        y = f[1] + math.cos(f[2]) * 20
        glow(x, y, 3, BLUE, 80)

    # Star glow
    glow(W//2, 45, 14, GOLD, 160)

    # Animated wishes
    index = (pygame.time.get_ticks() // 2000) % len(wishes)
    wish_text = wishes[index]

    text = font_big.render(wish_text, True, GOLD)
    screen.blit(text, (W//2 - text.get_width()//2, 540))

    pygame.display.flip()
    clock.tick(60)
