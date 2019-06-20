# coding=gbk
import pygame, random, sys
from settings import Settings

ai_settings = Settings()


# 定义传送带
class Conveyers():
    def __init__(self, screen):
        # 引入传送带的图像、矩形
        self.image = pygame.image.load('images/convey.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        screen_rect = screen.get_rect()
        # 横坐标是（0，100）的随机数
        self.rect.x = random.randrange(200, 400)
        # 纵坐标是（0，100）的随机数
        self.rect.y = random.randrange(0, 100)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    # 定义函数更新传送带的纵坐标
    def update_hei(self, screen):
        # 如果传送带高于屏幕顶端，那么传送带返回屏幕底部，并自下往上升
        if self.rect.top < 0:
            self.y = 600
            self.rect.y = self.y
            self.x = random.randrange(350, 550)
            self.rect.x = self.x
        # 如果传送带没有超过屏幕顶端，那么传送带以bar_hei_speed_factor的速度向上升
        else:
            self.y -= ai_settings.bar_hei_speed_factor
            self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
