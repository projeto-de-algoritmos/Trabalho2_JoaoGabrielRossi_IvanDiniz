import pygame
from pygame.locals import *
import random
import time
pygame.init()
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RANDOM CARDS')
clock = pygame.time.Clock()
background_colour = (255,255,255)

#difficulty
difficulty = ['noob','beginner','easy','normal','hard','hardcore','despair','hell','impossible']

#colors
black=(0,0,0)
white = (255,255,255)
red = (255,0,0)
lime = (0,255,0)
blue = (0,0,255)
Yellow =(255,255,0)
Cyan = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Gray = (128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Green = (0,128,0)
Purple = (128,0,128)
Teal = (0,128,128)
Navy = (0,0,128)
COLORS = list((black,white,red,lime,blue,Yellow,Cyan,Magenta,Silver,Gray,Maroon,Olive,Green,Purple,Teal))

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText,black)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def game_intro():

    intro = True
    font = pygame.font.Font(None, 30)
    orig_surf = font.render('Press any key to continue', True, black)
    txt_surf = orig_surf.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    choose_difficulty()
        alpha -= 4
        if alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            txt_surf = orig_surf.copy()  # Don't modify the original text surf.
            # Fill alpha_surf with this color to set its alpha value.
            alpha_surf.fill((255, 255, 255, alpha))
            # To make the text surface transparent, blit the transparent
            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        else:
            font = pygame.font.Font(None, 30)
            orig_surf = font.render('Press any key to continue', True, black)
            txt_surf = orig_surf.copy()
            # This surface is used to adjust the alpha of the txt_surf.
            alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
            alpha = 255  # The current alpha value of the surface.

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Choose your fate", largeText,black)
        TextRect.center = ((width/2),(height/3))
        txt_rect = txt_surf.get_rect()
        txt_rect.center  = ((width/2),(height*0.8))
        screen.blit(TextSurf, TextRect)
        screen.blit(txt_surf,txt_rect)
        #screen.blit(txt_surf, (500, 400))
        pygame.display.update()
        clock.tick(25)


def choose_difficulty():
    choosing=True
    while choosing :
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        x_difficulty=0
        largeText = pygame.font.Font('freesansbold.ttf', 16)
        for k in range (9):
            pygame.draw.rect(screen,black,(50+x_difficulty, 250, 90, 50))
            txt_surf, txt_rect = text_objects(difficulty[k], largeText, blue)
            txt_rect.center = ((50 + x_difficulty + (90 / 2)), (250 + (50 / 2)))
            screen.blit(txt_surf, txt_rect)
            x_difficulty += 100
        mouse = pygame.mouse.get_pos()
        x_difficulty=0
        for k in range (9):
            if 50+x_difficulty+90> mouse[0] > 50+x_difficulty and 250+50>mouse[1]>250:
                pygame.draw.rect(screen, red ,(50+x_difficulty, 250, 90, 50))
            txt_surf, txt_rect = text_objects(difficulty[k], largeText, blue)
            txt_rect.center = ((50 + x_difficulty + (90 / 2)), (250 + (50 / 2)))
            screen.blit(txt_surf, txt_rect)
            x_difficulty += 100


        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Choose the difficulty", largeText,black)
        TextRect.center = ((width / 2), (height *0.2))
        screen.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(30)


def game_loop():
    running = True
    #for a in COLORS:
    #   print(a)
    x = 10
    y = 10
    back=0
    front=1
    while running:
        random.shuffle(COLORS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        screen.fill(background_colour)
        pygame.draw.rect(screen,(255,0,0),(890,250,20,100))
        if x == 700 or back==1:
            pygame.draw.rect(screen,COLORS[random.randint(0,len(COLORS)-1)], (190+x,250,20,100))
            #print("b")
            x-=10
            back=1
            front=0
        if x==0 or front ==1:
            pygame.draw.rect(screen,COLORS[random.randint(0,len(COLORS)-1)],(190+x,250,20,100))
            #print("a")
            x+=10
            front=1
            back=0
        pygame.display.update()
        clock.tick(120)

game_intro()
game_loop()
pygame.quit()
quit()
