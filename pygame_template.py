### - Import modules - ###
import pygame
import os


### - Define Variables - ###
run = True
s_w = 1200
s_h = 800
here = os.path.dirname(os.path.realpath(__file__))


### - Initialize Pygame - ###
pygame.init()
win = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption("Pygame")
keys = pygame.key.get_pressed()


### - Main Loop
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    



    win.fill((0, 0, 0))
    pygame.display.update()


pygame.quit()
