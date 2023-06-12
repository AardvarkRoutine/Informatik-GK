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
red=(0,0,0)
green=(255,255,0)
blue=(0,0,255)
clock = pygame.time.Clock()



while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
 

        display.fill(blue)
        pixAr = pygame.PixelArray(display)
        pixAr[10][20] = black
        pygame.draw.circle(display, black, (100,350), 60)
        
        pygame.display.update()
        clock.tick(60)
     
pygame.quit()
quit()
