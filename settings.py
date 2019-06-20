#coding=gb2312
from win32api import GetSystemMetrics
import os
#得到屏幕大小
SCREENWIDTH = GetSystemMetrics (0)
SCREENHEIGHT = GetSystemMetrics (1)

class Settings():
	def __init__(self):
		#屏幕宽度为400
		self.screen_width=500
		#屏幕高度为600
		self.screen_height=600
		os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((SCREENWIDTH-self.screen_width)/2,(SCREENHEIGHT-self.screen_height)/2)
		self.bg_color=(255,255,255)
		#玩家水平移动速度为8
		self.man_wid_speed_factor=8
		#玩家在传送带上的水平速度
		self.man_wid_conveyer_factor=4
		
		  		
		
		
