#-*-coding:utf-8-*-

'''Create by Sheldon on 2018/2/21.
   Description :
   这是一个补给类
   记录初始化补给包、补给包移动方法
'''

import pygame
from random import *

# 炸弹补给类
class Bomb_Supply(pygame.sprite.Sprite):

    # 初始化类
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载炸弹素材
        self.bomb = pygame.image.load("images/ufo.png")
        # 获取炸弹实际像素区域
        self.mask = pygame.mask.from_surface(self.bomb)
        # 获取图片矩形大小
        self.rect = self.bomb.get_rect()
        # 获取图片宽和高
        self.width, self.height = bg_size[0], bg_size[1]
        # 初始化位置
        self.set_position()
        # 设置炮弹速度
        self.speed = 2

    # 移动
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.survival = False

    # 获取炮弹坐标
    def set_position(self):
        # 设置存活属性
        self.survival = True
        # 炮弹坐标奢侈
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.bottom = -100
