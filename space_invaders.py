import pygame
import sys
from pygame.locals import *

pygame.init()
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Space Invaders")
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)

black = (0, 0, 0)
green = (0, 255, 0)
clock = pygame.time.Clock()

# Variables
num_cols = 5
num_rows = 2
attacker_width = 40
attacker_height = 40
rectangle_spacing = 60
attacker_speed = 40
attacker_direction = 1
movement_interval = 45
projectile_speed = 10
projectile_cooldown = 45  # Cooldown in frames
defender_speed = 5

defender_image = pygame.image.load("defender.png").convert_alpha()
defender_rect = defender_image.get_rect()
defender_rect.center = (display_width // 2, display_height - 50)

attacker_image = pygame.image.load("attacker.png").convert_alpha()
attacker_rect = attacker_image.get_rect()

rectangle_width = 160
rectangle_height = 20
rect1 = pygame.Rect((display_width - (rectangle_width * 3 + rectangle_spacing * 2)) // 2, display_height - 200, rectangle_width, rectangle_height)
rect2 = pygame.Rect(rect1.right + rectangle_spacing, display_height - 200, rectangle_width, rectangle_height)
rect3 = pygame.Rect(rect2.right + rectangle_spacing, display_height - 200, rectangle_width, rectangle_height)

bounding_box = pygame.Rect(0, 0, display_width, display_height)
game_over = False

defender_projectiles = []
attackers = []

def game_over_screen():
    Fnt = pygame.font.SysFont("Arial", 50)
    game_over_image = pygame.image.load("game_over.png").convert_alpha()
    display.blit(game_over_image, (display_width // 2 - game_over_image.get_width() // 2, display_height // 2 - game_over_image.get_height() // 2))
    text = Fnt.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (display_width // 2, display_height // 2)
    display.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def check_projectile_collision():
    global defender_projectiles, attackers

    attackers_to_remove = []
    projectiles_to_remove = []

    for projectile_rect in defender_projectiles:
        for attacker in attackers:
            if attacker['rect'].colliderect(projectile_rect):
                attacker['health'] -= 1
                if attacker['health'] == 0:
                    projectiles_to_remove.append(projectile_rect)
                    attackers_to_remove.append(attacker)

    for projectile_rect in projectiles_to_remove:
        if projectile_rect in defender_projectiles:
            defender_projectiles.remove(projectile_rect)

    for attacker in attackers_to_remove:
        attackers.remove(attacker)

    if len(attackers) == 0:
        # Display win screen
        Fnt = pygame.font.SysFont("Arial", 50)
        win_text = Fnt.render("You Win!", True, (0, 255, 0))
        text_rect = win_text.get_rect(center=(display_width // 2, display_height // 2))
        display.blit(win_text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

# Create attackers
for row in range(num_rows):
    for col in range(num_cols):
        x = (col * (attacker_width + rectangle_spacing)) + ((display_width - (num_cols * (attacker_width + rectangle_spacing))) // 2)
        y = row * (attacker_height + rectangle_spacing)
        attacker_rect = attacker_image.get_rect(topleft=(x, y))
        attackers.append({'rect': attacker_rect, 'health': 1})

frame_counter = 0
projectile_cooldown_counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    x_direction = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]

    defender_rect.x += x_direction * defender_speed

    display.fill(black)

    for attacker in attackers:
        display.blit(attacker_image, attacker['rect'])

    pygame.draw.rect(display, green, rect1)
    pygame.draw.rect(display, green, rect2)
    pygame.draw.rect(display, green, rect3)

    display.blit(defender_image, defender_rect)

    for projectile_rect in defender_projectiles:
        pygame.draw.rect(display, (255, 255, 255), projectile_rect)

    check_projectile_collision()

    for projectile_rect in defender_projectiles:
        projectile_rect.y -= projectile_speed

    defender_projectiles = [projectile_rect for projectile_rect in defender_projectiles if projectile_rect.y > 0]

    for attacker in attackers:
        if attacker['rect'].colliderect(rect1) or attacker['rect'].colliderect(rect2) or attacker['rect'].colliderect(rect3):
            game_over = True
            break

    if game_over:
        game_over_screen()
        break

    frame_counter += 1
    if frame_counter >= movement_interval:
        frame_counter = 0
        move_down = False
        for attacker in attackers:
            attacker['rect'].x += attacker_speed * attacker_direction

            if attacker['rect'].left <= 0 or attacker['rect'].right >= display_width:
                move_down = True

        if move_down:
            attacker_direction *= -1
            for attacker in attackers:
                attacker['rect'].y += attacker_height + rectangle_spacing

    if keys[pygame.K_SPACE] and projectile_cooldown_counter == 0:
        projectile_rect = pygame.Rect(defender_rect.centerx - 2, defender_rect.top, 4, 8)
        defender_projectiles.append(projectile_rect)
        projectile_cooldown_counter = projectile_cooldown

    if projectile_cooldown_counter > 0:
        projectile_cooldown_counter -= 1

    pygame.display.update()
    clock.tick(60)
