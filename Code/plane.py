#-*-coding:utf-8-*-

'''Create by Sheldon on 2018/2/19.
   Description :
   管理我方飞机的类
   记录初始化飞机、键盘监控，移动管理等方法
'''

import pygame
from pygame.locals import *

class Plane(pygame.sprite.Sprite):

    # 初始化类
    def __init__(self,bg_size):
        # 初始化碰撞检测
        pygame.sprite.Sprite.__init__(self)
        # 加载飞机素材1
        self.plane1 = pygame.image.load("images/plane1.png").convert_alpha()
        # 加载飞机素材2
        self.plane2 = pygame.image.load("images/plane2.png").convert_alpha()
        # 最终输出的飞机
        self.plane = self.plane1
        # 获取飞机实际像素区域
        self.mask = pygame.mask.from_surface(self.plane)
        # 设置精灵列表
        self.death_spirits = list()
        # 加载精灵素材
        self.spirit1 = pygame.image.load("images/plane_blowup_n1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/plane_blowup_n2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/plane_blowup_n3.png").convert_alpha()
        # 将精灵存放进精灵列表中
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3])
        # 设置精灵列表播放下标
        self.spirits_index = 0
        # 切换参数
        self.swich = True
        # 计数器总数
        self.count = 3
        # 计数器
        self.scaler = self.count
        # 获取图片矩形大小
        self.rect = self.plane1.get_rect()
        # 获取游戏区域 宽 和 高
        self.width, self.height = bg_size[0], bg_size[1]
        # 设置移动速度
        self.speed = 10
        # 初始化位置
        self.set_position()

    # 上移
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    # 下移
    def moveDown(self):
        if self.rect.bottom < self.height - 50:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom =self.height - 50

    # 左移
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    # 右移
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width


    # 移动的总操作方法
    def move(self):
        # 获取用户键盘操作
        self.key_pressed = pygame.key.get_pressed()
        # 进行操作判断
        if self.key_pressed[K_w] or self.key_pressed[K_UP]:
            self.moveUp()
        if self.key_pressed[K_s] or self.key_pressed[K_DOWN]:
            self.moveDown()
        if self.key_pressed[K_a] or self.key_pressed[K_LEFT]:
            self.moveLeft()
        if self.key_pressed[K_d] or self.key_pressed[K_RIGHT]:
            self.moveRight()

        # 控制图片切换
        if self.swich:
            self.plane = self.plane1
        else:
            self.plane = self.plane2
        # 计数器判定
        if self.scaler == 0:
            self.swich = not self.swich
            self.scaler = self.count
        # 计数器计数
        self.scaler -= 1

    def set_position(self):
        # 设置存活属性
        self.survival = True
        # 连同精灵下标也归零
        self.spirits_index = 0
        # 设置飞机左侧坐标
        self.rect.left = (self.width - self.rect.width) / 2
        # 设置飞机的顶部坐标
        self.rect.top = self.height - self.rect.height - 50
