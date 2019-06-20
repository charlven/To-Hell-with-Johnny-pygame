#coding=gb2312
import pygame,random,time
from settings import Settings
ai_settings=Settings()
#定义第二个普通障碍
class Ordinary_2():
	def __init__(self,screen):
		self.screen=screen
		#引入第一个普通障碍的图像、矩形
		self.image=pygame.image.load('images/common.png')
		self.rect=self.image.get_rect()
		#横坐标在（50，100）的随机数
		self.rect.centerx=random.randrange(400,500)
		#纵坐标为（400，500）的随机数
		self.rect.centery=random.randrange(400,500)
		self.y=float(self.rect.y)
	
	#定义更新普通障碍的数值坐标函数	
	def update_hei(self,screen):
		#如果普通障碍高于屏幕顶端，那么普通障碍的纵坐标回到屏幕底端，水平坐标随机抽取
		if self.rect.top<0:
			self.y=600
			self.rect.y=self.y
			self.rect.centerx=random.randrange(200,400)
		
		#如果普通障碍还没有到达屏幕顶端，那么普通障碍就会以bar_hei_speed_factor的速度向上升	
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
			
	
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
