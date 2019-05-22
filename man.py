#coding=gbk
import pygame
from settings import Settings
ai_settings=Settings()
class Man():
	def __init__(self,screen):
		"""初始化人并设置初始位置"""
		self.screen=screen
		#加载人并获取图像
		self.image=pygame.image.load('images/man.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=550
		
		
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
		
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
		
	def update_wid(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.rect.centerx+=ai_settings.man_wid_speed_factor
		elif self.moving_left and self.rect.left>0:
			self.rect.centerx-=ai_settings.man_wid_speed_factor
			
	def update_hei(self,barrel):
		if barrel.rect.left<self.rect.right<barrel.rect.right:
			self.y-=ai_settings.man_hei_speed_factor_up
			self.rect.y=self.y
		else:
			self.y+=ai_settings.man_hei_speed_factor_down
			self.rect.y=self.y
			
				
				
		
#衔接人
	def update_hei_1(self,initial_ordinary,ordinary_1,ordinary_2,macadam_2,conveyer):
		if initial_ordinary.rect.bottom<self.rect.y:
			if ordinary_1.rect.top<self.rect.bottom<ordinary_1.rect.bottom and ordinary_1.rect.left<self.rect.right<ordinary_1.rect.right:
				self.y-=2*ai_settings.man_hei_speed_factor_down
				self.rect.y=self.y
			elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right<ordinary_2.rect.right:
				self.y-=2*ai_settings.man_hei_speed_factor_down
				self.rect.y=self.y
			
			elif macadam_2.rect.top<self.rect.bottom<macadam_2.rect.bottom and macadam_2.rect.left<self.rect.right<macadam_2.rect.right:
				self.y-=2*ai_settings.man_hei_speed_factor_down
				self.rect.y=self.y
			elif conveyer.rect.top<self.rect.bottom<conveyer.rect.bottom and conveyer.rect.left<self.rect.right<conveyer.rect.right:
				self.y-=2*ai_settings.man_hei_speed_factor_down
				self.rect.y=self.y
				self.x-=ai_settings.man_wid_conveyer_factor
				self.rect.x=self.x
			else:
				self.y+=ai_settings.man_hei_speed_factor_down
				self.rect.y=self.y
		
	
			
		
			
						
		
			
			
	
		
		
		
		
		
		
	
	def blitme(self):
		"""在指定位置绘制飞机"""
		self.screen.blit(self.image,self.rect)
		

