#coding=gb2312
import pygame
#定义刺
class Stick():
	def __init__(self,screen):
		self.screen=screen
		#引入刺的图像、矩形
		self.image=pygame.image.load('images/stick_2.png')
		self.rect=self.image.get_rect()
		#定义刺的位置
		self.rect.centerx=300
		self.rect.top=0
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
