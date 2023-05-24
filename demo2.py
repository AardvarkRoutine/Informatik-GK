import pygame,sys
from pygame.locals import *
pygame.init()
display_width=800
display_height=600
display = pygame.display.set_mode((display_width, display_height))
 
pygame.display.set_caption("Kreis")
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)
 
black = (0,0,0)
white = (255,255,255)
green=(0,255,0)
red=(255,0,0)
clock = pygame.time.Clock()

x=150#kreiskoordinaten
y=150
x_change = 0
y_change=0

pixAr = pygame.PixelArray(display)
pixAr[10][20] = black


def kreis(x,y):
    pygame.draw.circle(display, black, (x,y), 75)


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
    
            #if event.type==pygame.KEYUP:
              #  if event.key==pygame.K_LEFT:
                #    x_change=0
 
        x+=x_change
        y+=y_change
        display.fill(white)
        
        kreis(x,y)
        

 
        
        pygame.display.update()
        clock.tick(60)
     
pygame.quit()
quit()
