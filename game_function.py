#coding=gbk
import pygame
import sys
import random
from settings import Settings
def update_screen(ai_settings,screen,man,initial_ordinary,ordinary_1,ordinary_2,macadam_2,conveyer):
	screen.fill(ai_settings.bg_color)
	man.blitme()
	initial_ordinary.blitme()
	ordinary_1.blitme()
	ordinary_2.blitme()
	macadam_2.blitme()
	conveyer.blitme()
	
	pygame.display.flip()
	
pygame.init()
ai_settings=Settings()

font=pygame.font.SysFont(None,48)
TEXTCOLOR = (255, 255, 255)
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def check_events(ai_settings,screen,man,score):
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				man.moving_right=True
			elif event.key==pygame.K_LEFT:
				man.moving_left=True
		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				man.moving_right=False
			elif event.key==pygame.K_LEFT:
				man.moving_left=False
	drawText('Score: %s' % int((score)), font, screen, 10, 0)
	pygame.display.update()
		


		
				
	


		
	
		
				
		
		
