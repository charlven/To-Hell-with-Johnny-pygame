#coding=gbk
import pygame
from pygame.sprite import Sprite
class Sticks(Sprite):
	def __init__(self,screen,ai_settings):
		super(Sticks,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		
		self.image=pygame.image.load('images/stick.bmp')
		self.rect=self.image.get_rect()
		
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
		self.x=float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
