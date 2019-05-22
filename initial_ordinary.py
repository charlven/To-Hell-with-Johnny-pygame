#coding=gbk
import pygame
from man import Man
from settings import Settings
ai_settings=Settings()
class Initial_Ordinary():
	def __init__(self,ai_settings,screen,man):
		self.screen=screen
		self.image=pygame.image.load('images/common.png')
		self.rect=self.image.get_rect()
		self.rect.centerx=man.rect.centerx
		self.rect.top=man.rect.bottom
		self.y=float(self.rect.y)
		
		
	
	def update_hei(self):
		self.y-=ai_settings.bar_hei_speed_factor
		self.rect.y=self.y
		

		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		
		
