#coding=gbk
import pygame,random,time
from settings import Settings
ai_settings=Settings()
class Ordinary_2():
	def __init__(self,screen):
		self.screen=screen
		self.image=pygame.image.load('images/common.png')
		self.rect=self.image.get_rect()
		self.rect.centerx=random.randrange(50,100)
		self.rect.centery=random.randrange(400,500)
		self.y=float(self.rect.y)
		
	def update_hei(self,screen):
		if self.rect.top<0:
			self.y=600
			self.rect.y=self.y
			self.rect.centerx=random.randrange(200,400)
		
			
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
			
	
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
