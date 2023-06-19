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
green = (0, 255, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()

motive_image = pygame.image.load("motive.png")
motive_rect = motive_image.get_rect()
motive_rect.topleft = (0, 0)
motive_x_change = 0
motive_y_change = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motive_x_change = -5

            if event.key == pygame.K_RIGHT:
                motive_x_change = 5

            if event.key == pygame.K_UP:
                motive_y_change = -5

            if event.key == pygame.K_DOWN:
                motive_y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                motive_x_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                motive_y_change = 0

    motive_rect.x += motive_x_change
    motive_rect.y += motive_y_change

    display.fill(white)
    display.blit(motive_image, motive_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
