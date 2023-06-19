import pygame
import sys
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

objects = []

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("My Game")

black = (0, 0, 0)
green = (0, 255, 0)

clock = pygame.time.Clock()

def create_object(shape, x, y, x_change, y_change):
    return {
        "shape": shape,
        "x": x,
        "y": y,
        "x_change": x_change,
        "y_change": y_change
    }

def handle_key_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for obj in objects:
                    obj["x_change"] = -5
            elif event.key == pygame.K_RIGHT:
                for obj in objects:
                    obj["x_change"] = 5
            elif event.key == pygame.K_UP:
                for obj in objects:
                    obj["y_change"] = -5
            elif event.key == pygame.K_DOWN:
                for obj in objects:
                    obj["y_change"] = 5
            elif event.key == pygame.K_n:
                new_obj = create_object("new_shape", 400, 400, 0, 0)
                objects.append(new_obj)

def update_object_positions():
    for obj in objects:
        obj["x"] += obj["x_change"]
        obj["y"] += obj["y_change"]

def draw_objects():
    for obj in objects:
        if obj["shape"] == "kreis":
            pygame.draw.circle(display, black, (obj["x"], obj["y"]), 75)
        elif obj["shape"] == "dreieck":
            pygame.draw.polygon(display, green, ((obj["x"], obj["y"] + 75), (obj["x"] + 50, obj["y"]), (obj["x"] - 50, obj["y"])), 0)
        else:
            # Handle unknown shapes
            pass

while True:
    handle_key_events()

    update_object_positions()

    display.fill((255, 255, 255))  # Fill the display with white color

    draw_objects()

    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS
