# coding=gbk
import pygame
import sys
import random
from settings import Settings


def update_screen(ai_settings, screen, man, man_2, initial_ordinary, ordinary_1, ordinary_2, ordinary_3, macadam_2,
                  conveyer, stick):
    screen.fill(ai_settings.bg_color)
    background = pygame.image.load('wall2.jpg').convert()
    screen.blit(background, (0, 0))
    man.blitme()
    man_2.blitme()
    initial_ordinary.blitme()
    ordinary_1.blitme()
    ordinary_2.blitme()
    ordinary_3.blitme()
    macadam_2.blitme()
    conveyer.blitme()
    stick.blitme()

    pygame.display.flip()


pygame.init()
ai_settings = Settings()

font = pygame.font.SysFont(None, 48)
TEXTCOLOR_1 = (255, 255, 255)


def drawText_1(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR_1)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


TEXTCOLOR_2 = (0, 0, 0)


def drawText_2(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR_2)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def check_events(ai_settings, screen, man, man_2, score_1, score_2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                man.moving_right = True
            elif event.key == pygame.K_LEFT:
                man.moving_left = True
            elif event.key == pygame.K_d:
                man_2.moving_right = True
            elif event.key == pygame.K_a:
                man_2.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                man.moving_right = False
            elif event.key == pygame.K_LEFT:
                man.moving_left = False
            elif event.key == pygame.K_d:
                man_2.moving_right = False
            elif event.key == pygame.K_a:
                man_2.moving_left = False

    drawText_1('Score1: %s' % int((score_1)), font, screen, 10, 0)
    drawText_1('Score2: %s' % int((score_2)), font, screen, 220, 0)

    pygame.display.update()
