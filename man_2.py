#coding=gb2312
import pygame
from settings import Settings
ai_settings=Settings()
#定义玩家2
class Man_2():
	def __init__(self,screen):
		self.screen=screen
		#加载人并获取图像、矩形，让玩家的初始位置为屏幕中央的下方
		self.image=pygame.image.load('images/man.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=550
		
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
		#玩家初始状态是静止的
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
	
	#定义函数更新玩家的横坐标	
	def update_wid(self):
		#如果玩家在向右移动并且它没有越过屏幕的右端，则玩家继续向右移动
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.rect.centerx+=ai_settings.man_wid_speed_factor
		#如果玩家在向左移动并且它没有越过屏幕的左端，则玩家继续向左移动
		elif self.moving_left and self.rect.left>0:
			self.rect.centerx-=ai_settings.man_wid_speed_factor
	
	#定义函数更新玩家与初始障碍的相对位置				
	def update_hei(self,initial_ordinary):
		#如果玩家位置在初始障碍之内，那么玩家和初始障碍一起向上升（相对静止）
		if initial_ordinary.rect.left<self.rect.right<initial_ordinary.rect.right:
			self.y-=ai_settings.man_hei_speed_factor_up
			self.rect.y=self.y
		#如果玩家的位置在初始障碍之外，那么玩家就会以man_hei_speed_factor_down的速度向下掉落
		else:
			self.y+=ai_settings.man_hei_speed_factor_down
			self.rect.y=self.y
			
	
			
	#定义函数，更新玩家与其他障碍的相对位置		
	def update_hei_1(self,initial_ordinary,ordinary_1,ordinary_2,ordinary_3,macadam_2,conveyer,monster_rect):
		#先判断玩家与初始障碍之间的位置：如果玩家从初始障碍之下
		if initial_ordinary.rect.bottom<self.rect.y:
			#再判断玩家与怪兽之间的相对位置：如果玩家在怪兽位置之上或者之下
			if self.rect.bottom<monster_rect.top or self.rect.top>monster_rect.bottom:
				#然后判断玩家与其他各个障碍之间的相对位置：
				#如果玩家在第一个普通障碍的范围之内：那么玩家可以在这个障碍上左右移动（玩家垂直上与障碍以相同速度向上运动）
				if ordinary_1.rect.top<self.rect.bottom<ordinary_1.rect.bottom and ordinary_1.rect.left<self.rect.right and self.rect.left<ordinary_1.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#如果玩家在第二个普通障碍的范围之内：那么玩家可以在这个障碍上左右移动（玩家垂直上与障碍以相同速度向上运动）
				elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right and self.rect.left<ordinary_2.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#如果玩家在第三个普通障碍的范围之内：那么玩家可以在这个障碍上左右移动（玩家垂直上与障碍以相同速度向上运动）
				elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right and self.rect.left<ordinary_2.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#如果玩家在碎石障碍范围之内：那么玩家可以这个障碍上左右移动（玩家垂直上与障碍以相同速度向上运动）
				elif macadam_2.rect.top<self.rect.bottom<macadam_2.rect.bottom and macadam_2.rect.left<self.rect.right<macadam_2.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#如果玩家在传送带的范围之内：
				elif conveyer.rect.top<self.rect.bottom<conveyer.rect.bottom and conveyer.rect.left<self.rect.right and self.rect.left<conveyer.rect.right:
					#玩家在垂直方向上与传送带以相同的速度向上升
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
					#玩家在水平方向上以man_wid_conveyer_factor向左移动
					self.x-=ai_settings.man_wid_conveyer_factor
					self.rect.x=self.x
				#如果玩家均不在任何一个障碍的范围之内，那么玩家将会以2*Settings.man_hei_speed_factor_down的速度下落
				else:
					self.y+=ai_settings.man_hei_speed_factor_down
					self.rect.y=self.y
			#如果玩家的纵坐标与怪兽的纵坐标范围有交集
			else:
				#如果玩家在水平方向上与怪兽没有交集（也就是玩家没有触碰到怪兽）
				if self.rect.right<monster_rect.left or monster_rect.right<self.rect.left:
					#那么，玩家与以上方式一样运动
					if ordinary_1.rect.top<self.rect.bottom<ordinary_1.rect.bottom and ordinary_1.rect.left<self.rect.right<ordinary_1.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
					elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right<ordinary_2.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
					elif macadam_2.rect.top<self.rect.bottom<macadam_2.rect.bottom and macadam_2.rect.left<self.rect.right<macadam_2.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
					elif conveyer.rect.top<self.rect.bottom<conveyer.rect.bottom and conveyer.rect.left<self.rect.right<conveyer.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
						self.x-=ai_settings.man_wid_conveyer_factor
						self.rect.x=self.x
					else:
						self.y+=ai_settings.man_hei_speed_factor_down
						self.rect.y=self.y
				#如果玩家与怪兽触碰，那么玩家的纵坐标为650，玩家死亡
				else:
					self.y=650
					self.rect.y=self.y
					
			
			
			
			
			
			
			
	def update_stick(self,stick):
		if self.rect.top<stick.rect.bottom:
			self.y=650
			self.rect.y=self.y	
			

		
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	
