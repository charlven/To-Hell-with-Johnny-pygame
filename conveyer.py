#coding=gbk
import pygame,random,sys
from settings import Settings
ai_settings=Settings()
class Conveyers():
	def __init__(self,screen):
		self.image=pygame.image.load('images/convey.png')
		self.rect=self.image.get_rect()
		self.screen=screen
		screen_rect=screen.get_rect()
		self.rect.x=random.randrange(0,100)
		self.rect.y=random.randrange(0,100)
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
	def update_hei(self,screen):
		if self.rect.top<0:
			self.y=600
			self.rect.y=self.y
			self.x=random.randrange(0,400)
			self.rect.x=self.x
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
			
	
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	
