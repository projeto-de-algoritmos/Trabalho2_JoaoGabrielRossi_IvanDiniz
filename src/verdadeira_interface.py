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

COLORS = list((black,white,red,lime,blue,Cyan,Silver,Gray,Olive,Green,Purple,Teal,(128,0,0),
(139,0,0),(165,42,42),(178,34,34),(220,20,60),(255,99,71),(255,127,80),(205,92,92),(240,128,128),(233,150,122),
(250,128,114),(255,160,122),(255,69,0),(255,140,0),(255,165,0),(255,215,0),(184,134,11),(218,165,32),(238,232,170),
(189,183,107),(240,230,140),(154,205,50),(85,107,47),(144,238,144),(143,188,143),(46,139,87),(102,205,170),(32,178,170),
(47, 79, 79),(0,139,139),(25,25,112),(0,0,128),(138,43,226),(75,0,130),(106,90,205),(139,0,139),(186,85,211),(238,130,238),
(255,0,255),(199,21,133),(219,112,147),	(255,20,147),(255,105,180),(245,222,179)))

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def paint_button(largeText,color,inactiveColor):
    x_difficulty = 0
    mouse = pygame.mouse.get_pos()
    for k in range(9):
        if 50 + x_difficulty + 90 > mouse[0] > 50 + x_difficulty and 250 + 50 > mouse[1] > 250:
            pygame.draw.rect(screen, inactiveColor, (50 + x_difficulty, 250, 90, 50))
            txt_surf, txt_rect = text_objects(difficulty[k], largeText, blue)
            txt_rect.center = ((50 + x_difficulty + (90 / 2)), (250 + (50 / 2)))
            screen.blit(txt_surf, txt_rect)
        else:
            pygame.draw.rect(screen, color, (50 + x_difficulty, 250, 90, 50))
            txt_surf, txt_rect = text_objects(difficulty[k], largeText, blue)
            txt_rect.center = ((50 + x_difficulty + (90 / 2)), (250 + (50 / 2)))
            screen.blit(txt_surf, txt_rect)

        x_difficulty += 100


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText,black)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

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
            if event.type == pygame.KEYUP:
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
            #to make the word appear again so it can fade
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
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                x_difficulty = 0
                for k in range(9):
                    if 50 + x_difficulty + 90 > mouse[0] > 50 + x_difficulty and 250 + 50 > mouse[1] > 250:
                        break
                    x_difficulty += 100
                game_loop(x_difficulty)

        screen.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 16)
        paint_button(largeText,black,red)

        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Choose the difficulty", largeText,black)
        TextRect.center = ((width / 2), (height *0.2))
        screen.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(30)

def structure(difficulty):
    A = []
    D = []
    verificador = 1
    pipu = 0
    # while difficulty > 0:
    g = [[0] * difficulty for i in range(difficulty)]
    count0 = [0] * difficulty
    #while verificador == 1:
        # generating random graph
    for i in range(difficulty):
        for j in range(5):
            v1 = random.randint(0, difficulty - 1)
            v2 = random.randint(0, difficulty - 1)
            if v1 > v2:
                g[v1][v2] = 1
            elif v1 < v2:
                g[v2][v1] = 1


    for p in range(difficulty):
        for z in range(difficulty):
            if g[p][z]==1:
                count0[z]+=1

    # throwing initial vertexes with 0 count0 into lists
    for i in range(difficulty):
        if count0[i] == 0:
            A.append(i)
            D.append(i)
            pipu += 1

    i=0
    while (len(A) != 0):
        c = A[0]
        i+=1
        A.remove(c)

        for o in range(difficulty):
            if g[c][o] == 1:
                count0[o] = count0[o] - 1
                if count0[o] == 0:
                    A.append(o)
                    D.append(o)
                    pipu += 1

    if pipu != difficulty:
        for u in range(difficulty):
            count0[u] = 0
            pipu = 0
            for j in range(difficulty):
                g[i][j] = 0
        A.clear()
        D.clear()
    else:
        verificador = 0
    return D

def draw1(level,width_card,temp,c):
    x=0
    for i in range(level):
        if i == (level - 1):
            width_card_2 = width - x
            pygame.draw.rect(screen, c[i], (x, 0, width_card_2, height))
        else:
            pygame.draw.rect(screen, c[i], (x, 0, width_card, height))
        x += width_card
        temp.append(c[i])

def draw2(level,width_card,temp):
    x = 0
    mouse = pygame.mouse.get_pos()
    for i in range(level):
        if i == (level - 1):
            width_card_2 = width - x
            pygame.draw.rect(screen, temp[i], (x, 0, width_card_2, height))
            if x + width_card > mouse[0] > x and height > mouse[1] > 0:
                pygame.draw.rect(screen, black, (x, 0, width_card_2, height), 5)
        else:

            pygame.draw.rect(screen, temp[i], (x, 0, width_card, height))
            if x + width_card > mouse[0] > x and height > mouse[1] > 0:
                pygame.draw.rect(screen, black, (x, 0, width_card, height), 5)

        x += width_card

def choice(level,width_card,num,temp, c, life):
    mouse = pygame.mouse.get_pos()
    x=0
    for i in range(level):
        if i == (level - 1):
            width_card_2 = width - x
            if x + width_card > mouse[0] > x and height > mouse[1] > 0:
                if c[num]==temp[i]:
                    del temp[i]
                else:
                    life -= 1
        else:
            if x + width_card > mouse[0] > x and height > mouse[1] > 0:
                if c[num]==temp[i]:
                    del temp[i]
                else:
                    life -= 1
        x += width_card
    return life

def game_loop(level):
    level //= 100
    level += 1
    level *= 5
    width_card = width // level
    temp = []
    v=1
    num=0
    D = structure(level)
    c = []
    life = (level // 3) + 1
    random.shuffle(COLORS)
    for a in D:
        c.append(COLORS[a])
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                t = len(temp)
                life = choice(len(temp),width_card,num,temp,c, life)
                if t > len(temp):
                    num += 1
                    # print(num)

            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        choose_difficulty()

        screen.fill(white)
        if v==1:
            draw1(len(c),width_card,temp,c)
            random.shuffle(temp)
            v=0
            pygame.display.update()
            time.sleep(5)
            
        else:
            draw2(len(temp),width_card,temp)
            pygame.display.update()

        if len(temp)>0:
            width_card = width // len(temp)

        if len(temp)==0:
            screen.fill(white)
            message_display("You won")
            game_intro()
        if not life:
            screen.fill(white)
            message_display("You lose :(")
            game_intro()



game_intro()
game_loop()
pygame.quit()
quit()
