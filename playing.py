# coding=gb2312
import csv
import os
import pygame
import sys
import time

from win32api import GetSystemMetrics

import game_function as gf
from conveyer import Conveyers
from initial_ordinary import Initial_Ordinary
from macadam_2 import Macadam_2s
from man import Man
from man_2 import Man_2
from ordinary_1 import Ordinary_1
from ordinary_2 import Ordinary_2
from ordinary_3 import Ordinary_3
from settings import Settings
from stick import Stick

# 设置画面大小、分辨率、颜色等
FPS = 300
WINWIDTH = 800
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BGCOLOR = WHITE  # 背景颜色为白色
TEXTCOLOR = BLACK  # 字体颜色为黑色

# 得到屏幕大小
SCREENWIDTH = GetSystemMetrics(0)
SCREENHEIGHT = GetSystemMetrics(1)

font = pygame.font.SysFont(None, 48)
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')


def main():
    # global表示这些变量是函数外定义的全局变量
    global FPSCLOCK, IMAGESDICT, BASICFONT, DISPLAYSURF, PARAMETER

    pygame.init()  # 初始化
    # 固定屏幕位置
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((SCREENWIDTH - WINWIDTH) / 2, (SCREENHEIGHT - WINHEIGHT) / 2)
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    # 初始化用于显示的窗口并设置窗口尺寸,宽为800，高为600，以像素为单位
    FPSCLOCK = pygame.time.Clock()  # 设置创建时钟对象(可以控制游戏循环频率)
    pygame.display.set_caption("Lingnan Jump")  # 设置程序窗口的标题
    pygame.font.init()
    BASICFONT = pygame.font.Font('Comici.ttf', 18)  # 字体为Comici，字号为18号
    pygame.display.flip()

    # IMAGEDICT包含该程序所需要的所有图片对象
    # IMAGEDICT包含该程序所需要的所有图片对象
    IMAGESDICT = {'title': pygame.image.load('gametitle.png'),
                  'ordinary': pygame.image.load('images/common.png'),
                  'macadam': pygame.image.load('gravel.png'),
                  'conveyor': pygame.image.load('images/convey.png'),
                  'explanation': pygame.image.load('explain.png'),
                  'smallhelp': pygame.image.load('help.png'),
                  'monster_im': pygame.image.load('images/monster_1.png')}

    PARAMETER = {'coefficient': 1}

    startScreen()


# while True:
# run the game

def startScreen():
    """显示开始界面"""

    titleRect = IMAGESDICT['title'].get_rect()  # 放置标题图像
    topCoord_1 = 35  # topCoord用于定位文本顶部的位置
    titleRect.top = topCoord_1
    titleRect.centerx = HALF_WINWIDTH
    topCoord_1 += titleRect.height

    SRLRect = IMAGESDICT['explanation'].get_rect()  # 放置explanation图像
    topCoord_2 = 380
    SRLRect.top = topCoord_2
    SRLRect.centerx = HALF_WINWIDTH
    topCoord_2 += SRLRect.height

    instructionText = ['Press Buttons to Begin',
                       '( 1 - Easy ; 2 - Hard ; 3 - Hell )',
                       'Impairment ratio for final score: Easy - 0.7 ; Hard - 0.8 ; Hell - 1']

    DISPLAYSURF.fill(BGCOLOR)
    # 绘制图像
    DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)
    DISPLAYSURF.blit(IMAGESDICT['explanation'], SRLRect)

    # 打印文本且确定位置
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord_1 += 8  # 每行文字之间有8个像素
        instRect.top = topCoord_1
        instRect.centerx = HALF_WINWIDTH
        topCoord_1 += instRect.height  # 调整每行的高度
        DISPLAYSURF.blit(instSurf, instRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 键被按下
                from settings import Settings
                ai_settings = Settings()
                if event.key == pygame.K_1:
                    Settings.bar_hei_speed_factor = 5
                    Settings.man_hei_speed_factor_up = 5
                    Settings.man_hei_speed_factor_down = 8
                    PARAMETER['coefficient'] = 0.7
                    run_game()
                elif event.key == pygame.K_2:
                    Settings.bar_hei_speed_factor = 6
                    Settings.man_hei_speed_factor_up = 6
                    Settings.man_hei_speed_factor_down = 6
                    PARAMETER['coefficient'] = 0.8
                    run_game()
                elif event.key == pygame.K_3:
                    Settings.bar_hei_speed_factor = 10
                    Settings.man_hei_speed_factor_up = 10
                    Settings.man_hei_speed_factor_down = 9
                    PARAMETER['coefficient'] = 1
                    run_game()
                return

        # 将DISPLAYSURF内容显示到实际屏幕
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# 定义游戏运行的函数
def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 设置屏幕长宽
    monster_image = IMAGESDICT['monster_im']
    monster_rect = monster_image.get_rect()  # 获取monster的矩形
    monster_rect.bottom = 500  # 设置monster初始位置
    monster_rect.right = 50  # 设置monster初始位置
    speed = [1, 1]  # monster的速度：水平速度为1，竖直速度为1
    # 用不同的名词替代class定义的类
    man = Man(screen)
    man_2 = Man_2(screen)
    initial_ordinary = Initial_Ordinary(ai_settings, screen, man)
    ordinary_1 = Ordinary_1(screen)
    ordinary_2 = Ordinary_2(screen)
    ordinary_3 = Ordinary_3(screen)
    macadam_2 = Macadam_2s(screen)
    conveyer = Conveyers(screen)
    stick = Stick(screen)
    # 两个玩家的初始成绩为0
    score_1 = 0
    score_2 = 0

    pygame.mixer.music.play(-1, 0.0)

    while True:
        monster_rect = monster_rect.move(speed)  # 让monster的位置根据speed移动
        if (monster_rect.left < 0) or (monster_rect.right > 400):  # 如果monster在水平位置上超出屏幕范围，那么monster的运动方向相反
            speed[0] = -speed[0]
        if (monster_rect.bottom > 600) or (monster_rect.top < 0):  # 如果monster在竖直方向上超出了屏幕范围，那么monster的运动方向相反
            speed[1] = -speed[1]
        screen.blit(monster_image, monster_rect)  # 让屏幕更新monster的状态

        if man.rect.y < 600 or man_2.rect.y < 600:  # 如果玩家1和玩家2还没有触碰到屏幕顶端，则游戏继续
            if man.rect.y < 600 and man_2.rect.y < 600:
                score_1 += 0.01 * PARAMETER['coefficient']
                score_2 += 0.01 * PARAMETER['coefficient']

            elif man.rect.y < 600 and man_2.rect.y > 600:  # 如果玩家2触及屏幕顶端，则玩家2死亡，玩家1继续
                score_1 += 0.01 * PARAMETER['coefficient']
                score_2 += 0
            elif man.rect.y > 600 and man_2.rect.y < 600:  # 如果玩家1触碰到屏幕顶端，则玩家1死亡，玩家2继续
                score_1 += 0
                score_2 += 0.01 * PARAMETER['coefficient']

            gf.check_events(ai_settings, screen, man, man_2, score_1, score_2)

            man.update_wid()  # 更新玩家1的左右位置
            man_2.update_wid()  # 更新玩家2的左右位置
            man.update_hei(initial_ordinary)  # 更新玩家1在初始障碍上运动的竖直位置
            man_2.update_hei(initial_ordinary)  # 更新玩家2在初始障碍上运动的竖直位置
            initial_ordinary.update_hei()  # 更新初始障碍的位置
            ordinary_1.update_hei(screen)  # 更新第一个普通障碍的位置
            ordinary_2.update_hei(screen)  # 更新第二个普通障碍的位置
            ordinary_3.update_hei(screen)  # 更新第三个普通障碍的位置
            macadam_2.update_hei(screen)  # 更新碎石障碍的位置
            conveyer.update_hei(screen)  # 更新传送带的位置
            man_2.update_hei_1(initial_ordinary, ordinary_1, ordinary_2, ordinary_3, macadam_2, conveyer,
                               monster_rect)  # 更新玩家2与普通障碍、碎石、传送带上运动的竖直位置
            man_2.update_stick(stick)  # 更新玩家2与刺的相对位置
            man.update_hei_1(initial_ordinary, ordinary_1, ordinary_2, ordinary_3, macadam_2, conveyer,
                             monster_rect)  # 更新玩家1与普通障碍、碎石、传送带上运动的竖直位置
            man.update_stick(stick)  # 更新玩家1与刺的相对位置
            macadam_2.check_collide(screen, man, man_2)  # 检查玩家与碎石是否碰撞

            gf.update_screen(ai_settings, screen, man, man_2, initial_ordinary, ordinary_1, ordinary_2, ordinary_3,
                             macadam_2, conveyer, stick)

        else:  # 如果玩家1和玩家2都死亡，则出现GAME OVER字样
            score_1 += 0
            score_2 += 0
            gf.check_events(ai_settings, screen, man, man_2, score_1, score_2)
            gf.drawText_1('GAME OVER', font, screen, (ai_settings.screen_width / 3), (ai_settings.screen_height / 3))
            pygame.display.update()

            pygame.mixer.music.stop()
            gameOverSound.play()
            time.sleep(3)
            score_1 = int(score_1)
            score_2 = int(score_2)

            Scorewinwid = 500
            Scorewinhei = 150
            TEXTCOLOR = (255, 255, 255)
            BACKGROUNDCOLOR = (0, 0, 0)
            pygame.init()
            # 固定屏幕位置
            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
                (SCREENWIDTH - Scorewinwid) / 2, (SCREENHEIGHT - Scorewinhei) / 2)
            ScoreWindow = pygame.display.set_mode((Scorewinwid, Scorewinhei))
            pygame.display.set_caption('Score Save')
            BASICFONT = pygame.font.Font('Comici.ttf', 20)
            gf.drawText_1("Do you want to save this score?", BASICFONT, ScoreWindow, (Scorewinwid / 3),
                          (Scorewinhei / 3) - 10)
            gf.drawText_1("If yes, please press Y !", BASICFONT, ScoreWindow, (Scorewinwid / 3), (Scorewinhei / 3 + 15))
            gf.drawText_1("If no, please press N !", BASICFONT, ScoreWindow, (Scorewinwid / 3), (Scorewinhei / 3 + 40))
            pygame.display.flip()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            sys.exit()
                        elif event.key == pygame.K_y:
                            score_1 = int(score_1)
                            stu1 = ["a", score_1]
                            out_1 = open('Stu1_csv.csv', 'a', newline="")
                            csv_write = csv.writer(out_1, dialect='excel')
                            csv_write.writerow(stu1)
                            print("write over")
                            filename = 'Stu1_csv.csv'
                            with open(filename) as f:
                                reader = csv.reader(f)
                                header_row = next(reader)
                                print(header_row)
                                for index, column_header in enumerate(header_row):
                                    print(index, column_header)
                                scores_1 = [score_1]
                                for row in reader:
                                    new_score = int(row[1])
                                    scores_1.append(new_score)
                                scores_1.remove(score_1)
                                scores_1.append(score_1)
                                print(scores_1)

                            score_2 = int(score_2)
                            stu2 = ["b", score_2]
                            out_2 = open('Stu2_csv.csv', 'a', newline="")
                            csv_write = csv.writer(out_2, dialect='excel')
                            csv_write.writerow(stu2)
                            print("write over")
                            filename_2 = 'Stu2_csv.csv'
                            with open(filename_2) as f:
                                reader = csv.reader(f)
                                header_row = next(reader)
                                print(header_row)
                                for index, column_header in enumerate(header_row):
                                    print(index, column_header)
                                scores_2 = [score_2]
                                for row in reader:
                                    new_score_2 = int(row[1])
                                    scores_2.append(new_score_2)
                                scores_2.remove(score_2)
                                scores_2.append(score_2)
                                print(scores_2)

                            from matplotlib import pyplot as plt
                            fig = plt.figure(dpi=128, figsize=(3, 2))
                            plt.plot(scores_1, c='red', label="score 1")
                            plt.plot(scores_2, c='gray', label="score 1")
                            plt.title("Score", fontsize=18)
                            plt.xlabel = ('')
                            plt.ylabel = ('score')
                            plt.tick_params(axis='both', which='major', labelsize=16)
                            plt.legend(loc=9)
                            plt.savefig('scoreshow.png', bbox_inches='tight')
                            top_score_1 = max(scores_1)
                            top_score_2 = max(scores_2)
                            if top_score_1 > top_score_2:
                                winner = 'Player 1'
                            elif top_score_1 < top_score_2:
                                winner = 'Player 2'
                            else:
                                winner = 'Player 1 and Player 2'
                            WINDOWWIDTH = 800
                            WINDOWHEIGHT = 600
                            pygame.init()
                            # 固定屏幕位置
                            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
                                (SCREENWIDTH - WINDOWWIDTH) / 2, (SCREENHEIGHT - WINDOWHEIGHT) / 2)
                            windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                            pygame.display.set_caption('Score Show')
                            DISPLAYSURF.fill(BGCOLOR)

                            BASICFONT_1 = pygame.font.Font('Comici.ttf', 38)
                            BASICFONT_2 = pygame.font.Font('Comici.ttf', 28)
                            gf.drawText_2(winner, BASICFONT_1, windowSurface, 330, 130)
                            gf.drawText_2("Player 1's current score is " + str(score_1), BASICFONT_2, windowSurface,
                                          225, 200)
                            gf.drawText_2("Player 2's current score is " + str(score_2), BASICFONT_2, windowSurface,
                                          225, 250)
                            Scoreimage = {'show': pygame.image.load('scoreshow.png'),
                                          'top': pygame.image.load('huizhang.jpg'),
                                          'title': pygame.image.load('winner.png')}
                            SHRect_1 = Scoreimage['show'].get_rect()
                            image_position = 300
                            SHRect_1.top = image_position
                            SHRect_1.centerx = HALF_WINWIDTH
                            image_position += SHRect_1.height
                            windowSurface.blit(Scoreimage['show'], SHRect_1)
                            SHRect_2 = Scoreimage['title'].get_rect()
                            image_position = 50
                            SHRect_2.top = image_position
                            SHRect_2.centerx = HALF_WINWIDTH
                            image_position += SHRect_2.height
                            windowSurface.blit(Scoreimage['title'], SHRect_2)
                            SHRect_3 = Scoreimage['top'].get_rect()
                            image_position = 46
                            SHRect_3.top = image_position
                            SHRect_3.centerx = 346
                            image_position += SHRect_3.height
                            windowSurface.blit(Scoreimage['top'], SHRect_3)
                            pygame.display.flip()
                            time.sleep(10)
                            return
            break

        gf.update_screen(ai_settings, screen, man, man_2, initial_ordinary, ordinary_1, ordinary_2, ordinary_3,
                         macadam_2, conveyer, stick)


if __name__ == '__main__':
    main()
