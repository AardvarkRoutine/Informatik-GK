import pygame,sys
from pygame.locals import *
pygame.init()
display_width=800
display_height=600
display = pygame.display.set_mode((display_width, display_height))
 
pygame.display.set_caption("Spiel")
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)
 
black = (0,0,0)
white = (255,255,255)
green=(0,255,0)
red=(255,0,0)
clock = pygame.time.Clock()

kreis_x=150#kreiskoordinaten
kreis_y=150
kreis_x_change = 0
kreis_y_change=0

dreieck_x=400#dreieckkoordinaten
dreieck_y=400
dreieck_x_change=0
dreieck_y_change=0


pixAr = pygame.PixelArray(display)
pixAr[10][20] = black

def kreis(kreis_x,kreis_y):
    pygame.draw.circle(display, black, (kreis_x,kreis_y), 75)


def dreieck(x, y):
    pygame.draw.polygon(display, green, ((x, y + 75), (x + 50, y), (x - 50, y)), 0)



while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    kreis_x_change = -5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    kreis_x_change = 5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    kreis_y_change = -5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    kreis_y_change = 5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dreieck_y_change = -5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    dreieck_y_change = 5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dreieck_x_change = -5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    dreieck_x_change = 5
    

        kreis_x+=kreis_x_change
        kreis_y+=kreis_y_change
        dreieck_x+=dreieck_x_change
        dreieck_y+=dreieck_y_change
        display.fill(white)
        
        kreis(kreis_x,kreis_y)
        dreieck(dreieck_x,dreieck_y)
               
        pygame.display.update()
        clock.tick(60)
     
pygame.quit()
quit()
