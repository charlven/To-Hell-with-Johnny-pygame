#coding=gbk
import pygame,random,time
from settings import Settings
ai_settings=Settings()
class Macadam_2s():
	def __init__(self,screen):
		self.image=pygame.image.load('images/gravel.png')
		self.rect=self.image.get_rect()
		self.screen=screen
		screen_rect=screen.get_rect()
		self.rect.x=random.randrange(350,400)
		self.rect.y=300
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
			
	def check_collide(self,screen,man):
		if self.rect.top<man.rect.bottom<self.rect.bottom and self.rect.left<man.rect.right<self.rect.right:
			if self.rect.centerx-10<man.rect.centerx<self.rect.centerx+10:
				self.y=600
				self.rect.y=self.y
				self.rect.x=random.randrange(200,350)
					

			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		
