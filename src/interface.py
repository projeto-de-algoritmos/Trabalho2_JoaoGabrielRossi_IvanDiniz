import pygame
from pygame.locals import *

pygame.init()
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RANDOM CARDS')
background_colour = (255,255,255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_colour)
    pygame.draw.rect(screen,(0,0,0), Rect(80,300,20,100))
    pygame.display.flip()
