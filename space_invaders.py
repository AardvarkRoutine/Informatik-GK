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

defender_image = pygame.image.load("defender.png").convert_alpha()
defender_rect = defender_image.get_rect()
defender_rect.center = (display_width // 2, display_height - 50)

attacker_image = pygame.image.load("attacker.png").convert_alpha()
attacker_rect = attacker_image.get_rect()

attacker_width = attacker_rect.width
attacker_height = attacker_rect.height

num_rows = 3
num_cols = 5

rectangle_width = 160
rectangle_height = 20
rectangle_spacing = 60

def game_over_screen():
    Fnt = pygame.font.SysFont("Arial", 50)
    game_over_image = pygame.image.load("game_over.png").convert_alpha()
    #display it in the middle of the screen
    display.blit(game_over_image, (display_width // 2 - game_over_image.get_width() // 2, display_height // 2 - game_over_image.get_height() // 2))
    text = Fnt.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (display_width // 2, display_height // 2)
    display.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

attackers = []
for row in range(num_rows):
    for col in range(num_cols):
        x = (col * (attacker_width + rectangle_spacing)) + ((display_width - (num_cols * (attacker_width + rectangle_spacing))) // 2)
        y = 100 + row * (attacker_height + rectangle_spacing)  # Adjusted y position
        attacker_rect = attacker_image.get_rect(topleft=(x, y))
        attackers.append(attacker_rect)

attacker_speed = 1
attacker_direction = 1

rect1 = pygame.Rect((display_width - (rectangle_width * 3 + rectangle_spacing * 2)) // 2, display_height - 200, rectangle_width, rectangle_height)
rect2 = pygame.Rect(rect1.right + rectangle_spacing, display_height - 200, rectangle_width, rectangle_height)
rect3 = pygame.Rect(rect2.right + rectangle_spacing, display_height - 200, rectangle_width, rectangle_height)

bounding_box = pygame.Rect(0, 0, display_width, display_height)

defender_speed = 5
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    x_direction = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]

    defender_rect.x += x_direction * defender_speed

    display.fill(black)

    for attacker_rect in attackers:
        display.blit(attacker_image, attacker_rect)

    pygame.draw.rect(display, green, rect1)
    pygame.draw.rect(display, green, rect2)
    pygame.draw.rect(display, green, rect3)

    display.blit(defender_image, defender_rect)

    collision = False
    for x in range(defender_rect.width):
        for y in range(defender_rect.height):
            defender_pixel = defender_image.get_at((x, y))
            if defender_pixel.a != 0 and not bounding_box.collidepoint(defender_rect.x + x, defender_rect.y + y):
                collision = True
                break
        if collision:
            break

    if collision:
        defender_rect.clamp_ip(bounding_box)

    # Check for wall collision
    for attacker_rect in attackers:
        if attacker_rect.colliderect(rect1) or attacker_rect.colliderect(rect2) or attacker_rect.colliderect(rect3):
            game_over = True
            break

    if game_over:
        game_over_screen()
        break

    # Move attackers and reverse direction if they touch the wall
    for attacker_rect in attackers:
        attacker_rect.x += attacker_speed * attacker_direction

        if attacker_rect.left <= 0 or attacker_rect.right >= display_width:
            attacker_direction *= -1
            for a in attackers:
                a.y += attacker_height

    pygame.display.update()
    clock.tick(60)
