# coding=gb2312
import pygame
from man import Man
from settings import Settings

ai_settings = Settings()


# 定义初始障碍
class Initial_Ordinary():
    def __init__(self, ai_settings, screen, man):
        self.screen = screen
        self.image = pygame.image.load('images/common.png')  # 引入图像
        self.rect = self.image.get_rect()  # 获取矩形
        self.rect.centerx = man.rect.centerx  # 让游戏开始时玩家站在初始障碍的中央
        self.rect.top = man.rect.bottom
        self.y = float(self.rect.y)

    def update_hei(self):
        self.y -= ai_settings.bar_hei_speed_factor  # 让障碍从下至上以bar_hei_speed_factor的速度运动
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
