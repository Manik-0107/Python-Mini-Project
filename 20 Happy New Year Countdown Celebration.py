# Project Name: Happy New Year Countdown Celebration

import pygame
import random
import math
import sys

# Initialize pygame
try:
    pygame.init()
except Exception as e:
    print(f"Error initializing pygame: {e}")
    sys.exit()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
try:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Happy New Year 2026!")
except Exception as e:
    print(f"Error setting up display: {e}")
    sys.exit()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 100)
BLUE = (100, 150, 255)
PURPLE = (200, 100, 255)
SILVER = (200, 200, 200)
COLORS = [RED, GOLD, GREEN, BLUE, PURPLE]

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Firework particles
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 4)
        self.speed = random.uniform(2, 6)
        self.angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed
        self.life = random.randint(40, 80)
        self.gravity = 0.1
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.life -= 1
        
    def draw(self):
        if self.life > 0:
            # Draw the particle
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
            # Draw a smaller bright circle inside
            inner_radius = max(1, self.radius // 2)
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), inner_radius)
            
    def is_alive(self):
        return self.life > 0

# Fireworks
class Firework:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT
        self.color = random.choice(COLORS)
        self.speed = random.uniform(3, 6)
        self.particles = []
        self.exploded = False
        self.target_y = random.randint(50, HEIGHT // 2)
        
    def update(self):
        if not self.exploded:
            self.y -= self.speed
            if self.y <= self.target_y:
                self.explode()
        else:
            for particle in self.particles[:]:
                particle.update()
                if not particle.is_alive():
                    self.particles.remove(particle)
                    
    def explode(self):
        self.exploded = True
        # Create explosion particles
        for _ in range(random.randint(80, 150)):
            self.particles.append(Particle(self.x, self.y, self.color))
            
    def draw(self):
        if not self.exploded:
            # Draw the rising firework
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 4)
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 2)
            
            # Draw a trail
            for i in range(5):
                pos_y = self.y + i * 4
                trail_color = self.color
                pygame.draw.circle(screen, trail_color, (int(self.x), int(pos_y)), 2)
        else:
            for particle in self.particles:
                particle.draw()
                
    def is_done(self):
        return self.exploded and len(self.particles) == 0

# Text animation with fallback fonts
class TextAnimation:
    def __init__(self, text, size, y_pos):
        self.text = text
        self.size = size
        self.y_pos = y_pos
        
        # Try multiple fonts with fallbacks
        font_names = ['arial', 'freesansbold', 'freesans', 'dejavusans', 'ubuntu']
        self.font = None
        
        for font_name in font_names:
            try:
                self.font = pygame.font.SysFont(font_name, size, bold=True)
                break
            except:
                continue
        
        # If no font found, use the default
        if self.font is None:
            self.font = pygame.font.Font(None, size)
        
        self.alpha = 0
        self.alpha_speed = 3
        self.color_index = 0
        self.color_timer = 0
        self.colors = COLORS
        
    def update(self):
        # Fade in
        if self.alpha < 255:
            self.alpha += self.alpha_speed
            if self.alpha > 255:
                self.alpha = 255
                
        # Color cycling
        self.color_timer += 1
        if self.color_timer >= 5:
            self.color_index = (self.color_index + 1) % len(self.colors)
            self.color_timer = 0
            
    def draw(self):
        color = self.colors[self.color_index]
        text_surface = self.font.render(self.text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, self.y_pos))
        
        # Draw the text
        screen.blit(text_surface, text_rect)
        
        # Draw a simple glow effect when fully visible
        if self.alpha == 255:
            glow_surface = self.font.render(self.text, True, WHITE)
            glow_rect = glow_surface.get_rect(center=(WIDTH // 2, self.y_pos))
            # Draw glow with small offsets
            for offset in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                screen.blit(glow_surface, glow_rect.move(offset))

# Star background
stars = []
for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.uniform(0.1, 1.5)
    speed = random.uniform(0.2, 0.8)
    stars.append([x, y, size, speed])

# Create text animations
main_text = TextAnimation("HAPPY NEW YEAR!", 64, HEIGHT // 3)
year_text = TextAnimation("2026", 72, HEIGHT // 2)
wish_text = TextAnimation("May all your dreams come true!", 32, HEIGHT // 1.5)

# Create fireworks list
fireworks = []
firework_timer = 0

# Countdown timer for New Year
countdown_value = 10  # 10 seconds countdown
countdown_font = pygame.font.SysFont('arial', 36, bold=True)
last_countdown_time = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # Add a firework when space is pressed
                fireworks.append(Firework())
            elif event.key == pygame.K_f:
                # Toggle fullscreen
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode((WIDTH, HEIGHT))
                else:
                    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    
    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw stars
    for star in stars:
        x, y, size, speed = star
        # Update star position
        y += speed
        if y > HEIGHT:
            y = 0
            x = random.randint(0, WIDTH)
        star[1] = y
        
        # Draw star with twinkling effect
        time_factor = pygame.time.get_ticks() * 0.001
        brightness = int(150 + 100 * math.sin(time_factor * 2 + x * 0.01))
        star_color = (brightness, brightness, brightness)
        pygame.draw.circle(screen, star_color, (int(x), int(y)), size)
    
    # Update and draw fireworks
    firework_timer += 1
    if firework_timer >= 30 and len(fireworks) < 8:
        fireworks.append(Firework())
        firework_timer = 0
    
    for firework in fireworks[:]:
        firework.update()
        firework.draw()
        if firework.is_done():
            fireworks.remove(firework)
    
    # Draw a countdown timer
    if countdown_value > 0:
        if current_time - last_countdown_time >= 1000:  # 1 second has passed
            countdown_value -= 1
            last_countdown_time = current_time
        
        countdown_text = f"New Year in: {countdown_value}"
        countdown_surface = countdown_font.render(countdown_text, True, GOLD)
        countdown_rect = countdown_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(countdown_surface, countdown_rect)
        
        # Draw countdown circle
        progress = (10 - countdown_value) / 10
        angle = 2 * math.pi * progress
        pygame.draw.arc(screen, GOLD, (WIDTH//2 - 60, 20, 120, 60), 0, angle, 5)
    else:
        # New Year has arrived!
        celebration_text = "HAPPY NEW YEAR!!!"
        celebration_surface = countdown_font.render(celebration_text, True, RED)
        celebration_rect = celebration_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(celebration_surface, celebration_rect)
    
    # Update and draw text animations
    main_text.update()
    year_text.update()
    wish_text.update()
    
    main_text.draw()
    year_text.draw()
    wish_text.draw()
    
    # Draw instructions at the bottom
    font = pygame.font.SysFont("arial", 18)
    instruction1 = font.render("Press SPACE for more fireworks | ESC to exit", True, SILVER)
    instruction2 = font.render("Press F for fullscreen mode", True, SILVER)
    
    screen.blit(instruction1, (WIDTH // 2 - instruction1.get_width() // 2, HEIGHT - 50))
    screen.blit(instruction2, (WIDTH // 2 - instruction2.get_width() // 2, HEIGHT - 30))
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
sys.exit()
