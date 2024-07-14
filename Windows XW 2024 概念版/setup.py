# -*- coding: utf-8 -*-
# /BLACKBOXES/BOOT

# /BLACKBOXES/KEY-VALUE
TC = True
import sys
import os
from datetime import datetime
import win32api
import pygame

NoneT = None
Inf = float('inf')
workdir = os.getcwd()
system = os.system
now = datetime.now
屏幕宽度 = win32api.GetSystemMetrics(0)
屏幕高度 = win32api.GetSystemMetrics(1)

# /BLACKBOXES/LOG
if not os.path.exists('debug.log'):  # 文件不存在时创建
    open('debug.log', 'w', encoding='utf-8').close()
with open('debug.log', 'a+', encoding='utf-8') as f:
    f.write(f'[{now().strftime('%Y-%M-%D')}][debug.log]\n')


def log(s, thread='main', level='debug'):
    if not os.path.exists('debug.log'):
        raise SystemExit('STOP:missing debug.log')

    with open('debug.log', 'a+', encoding='utf-8') as f:
        f.write(f'[{now().strftime('%H:%M:%S')}][{thread}/{level}]:{s}\n')


# /BLACKBOXES/MAIN
def write(s: str):
    log(s, 'main', 'info')
    sys.stdout.write(s + '\n')


def write_err(s: str):
    log(s, 'main', 'error')
    sys.stderr.write(s + '\n')


def pygame_testdraw(文本, 字体大小, 位置, 字体颜色=(255, 255, 255), 字体背景颜色=(0, 0, 0)):
    font = pygame.font.Font('C:/Windows/Fonts/STKAITI.TTF', 字体大小)
    text = font.render(文本, True, 字体颜色, 字体背景颜色)
    textRect = text.get_rect()
    textRect.center = 位置
    screen.blit(text, textRect)


def main():
    pygame.init()
    # noinspection PyGlobalUndefined
    global screen
    screen = pygame.display.set_mode((屏幕宽度-10, 屏幕高度-100))
    pygame.display.set_caption('Windows XW 2024 概念版 Setup')
    pygame.display.set_icon(pygame.image.load("setup.ico"))
    # screen.fill((0, 0, 0))
    pygame_testdraw('Windows XW 2024 概念版 Setup', 50, (0, 0))
    isrun = True
    while isrun:
        pygame.display.flip()  # 更新屏幕内容
        # 循环获取事件，监听事件状态
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isrun = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    isrun = False

    write('Boot at BIOS')
    write('Boot with USB Drive')
    write('安装程序正在启动...')
    write('Windows XW 2024 概念版')


if '__main__' == __name__:
    main()
