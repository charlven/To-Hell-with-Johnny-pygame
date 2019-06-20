#coding=gb2312
import pygame,random,time
from settings import Settings
ai_settings=Settings()
#定义碎石
class Macadam_2s():
	def __init__(self,screen):
		self.image=pygame.image.load('images/gravel.png') #获取碎石图像
		self.rect=self.image.get_rect() #获取碎石矩形
		self.screen=screen
		screen_rect=screen.get_rect()
		self.rect.x=random.randrange(350,400) #随机定义碎石初始横坐标，范围为350-400
		self.rect.y=300
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
	def update_hei(self,screen):
		#如果碎石到达屏幕的顶端
		if self.rect.top<0:
			#那么碎石纵坐标变成600，横坐标随机设定，并重新自下往上升
			self.y=600
			self.rect.y=self.y
			self.x=random.randrange(50,550)
			self.rect.x=self.x
		#如果碎石没有到达屏幕顶端，那么碎石障碍继续自下往上升
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
	
	#定义函数判断碎石是否消失		
	def check_collide(self,screen,man,man_2):
		#如果玩家1在碎石上：
		if self.rect.top<man.rect.bottom<self.rect.bottom and self.rect.left<man.rect.right<self.rect.right:
			#如果玩家中间的坐标在碎石的某个范围之内（centerx-10,centerx+10)
			if self.rect.centerx-10<man.rect.centerx<self.rect.centerx+10:
				#那么碎石的纵坐标立刻变成600，横坐标随机出现
				self.y=600
				self.rect.y=self.y
				self.rect.x=random.randrange(200,350)
		#如果玩家2在碎石上：		
		elif self.rect.top<man_2.rect.bottom<self.rect.bottom and self.rect.left<man_2.rect.right<self.rect.right:
			#如果如果玩家中间的坐标在碎石的某个范围之内（centerx-10,centerx+10)
			if self.rect.centerx-10<man_2.rect.centerx<self.rect.centerx+10:
				#那么碎石的纵坐标立刻变成600，横坐标随机出现
				self.y=600
				self.rect.y=self.y
				self.rect.x=random.randrange(200,350)
					

			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		
