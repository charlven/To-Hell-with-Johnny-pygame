#coding=gbk
import pygame
from settings import Settings
from pygame.locals import*
ai_settings=Settings()
class Monster():
	def __init__(self,screen):
		self.screen=screen
		self.image=pygame.image.load('images/monster_1.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centery=300
		self.rect.centerx=100
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
		
	def play_monster(self,ai_settings):
		while True:
			self.rect.centerx+=ai_settings.man_wid_speed_factor
			if self.rect.left<0 or self.rect.right>400:
				b=-ai_settings.man_wid_speed_factor
				self.rect.centerx+=b
			
				
		
		
		
		
		
			
		
			
		
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		
		
		
		

