#coding=gbk
import sys
import pygame,random,time

from pygame.sprite import Group
from man import Man
from settings import Settings
from initial_ordinary import Initial_Ordinary
from ordinary_1 import Ordinary_1
from ordinary_2 import Ordinary_2
from macadam_2 import Macadam_2s
from conveyer import Conveyers


import game_function as gf
font=pygame.font.SysFont(None,48)
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')
def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Lingnan Leaping")
	
	man=Man(screen)
	
	
	
	initial_ordinary=Initial_Ordinary(ai_settings,screen,man)
	ordinary_1=Ordinary_1(screen)
	ordinary_2=Ordinary_2(screen)
	macadam_2=Macadam_2s(screen)
	conveyer=Conveyers(screen)
	
	score=0
	pygame.mixer.music.play(-1, 0.0)

	
	
	

	while True:
		
		if man.rect.y<600:
			score+=0.01
			gf.check_events(ai_settings,screen,man,score)
			initial_ordinary.update_hei()
			ordinary_1.update_hei(screen)
			man.update_wid()
			man.update_hei(initial_ordinary)
			man.update_hei_1(initial_ordinary,ordinary_1,ordinary_2,macadam_2,conveyer)
			ordinary_2.update_hei(screen)
			macadam_2.update_hei(screen)
			macadam_2.check_collide(screen,man)
			conveyer.update_hei(screen)
			gf.update_screen(ai_settings,screen,man,initial_ordinary,ordinary_1,ordinary_2,macadam_2,conveyer)
						

		else:
			score+=0
			gf.check_events(ai_settings,screen,man,score)
			gf.drawText('GAME OVER', font, screen, (ai_settings.screen_width / 3), (ai_settings.screen_height / 3))

			pygame.display.update()
			pygame.mixer.music.stop()
			gameOverSound.play()
			time.sleep(1)

			break
			
			
			
			
		
		gf.update_screen(ai_settings,screen,man,initial_ordinary,ordinary_1,ordinary_2,macadam_2,conveyer)
		
		
		
		
	
		
run_game()

