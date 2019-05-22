#coding=gbk
class GameStats():
	def __init__(self,man):
		self.man=man
		self.reset_stats()
		self.game_active=True
	def reset_stats(self):
		self.man_death=float(self.man.rect.bottom)
		
