import pygame
import sys
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Spiel")
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)

black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()

motive_image = pygame.image.load("motive.png").convert_alpha()

motive_rect = motive_image.get_rect()
motive_rect.center = (display_width // 2, display_height // 2)

bounding_box = pygame.Rect(0, 0, display_width, display_height)

motive_speed = 5  # Adjust the speed as needed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    x_direction = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    y_direction = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    motive_rect.x += x_direction * motive_speed
    motive_rect.y += y_direction * motive_speed

    display.fill(white)

    display.blit(motive_image, motive_rect)

    collision = False
    for x in range(motive_rect.width):
        for y in range(motive_rect.height):
            motive_pixel = motive_image.get_at((x, y))
            if motive_pixel.a != 0 and not bounding_box.collidepoint(motive_rect.x + x, motive_rect.y + y):
                collision = True
                break
        if collision:
            break

    if collision:
        motive_rect.clamp_ip(bounding_box)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
