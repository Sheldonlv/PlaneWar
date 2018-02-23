#-*-coding:utf-8-*-

'''Create by Sheldon on 2018/2/21.
   Description :
   用于管理子弹的类
   记录初始化子弹，子弹移动，重设等方法
'''

import pygame

class Bullet(pygame.sprite.Sprite):

    # 初始化类
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载子弹素材
        self.bullet = pygame.image.load("images/bullet.png")
        # 获取子弹实际像素区域
        self.mask = pygame.mask.from_surface(self.bullet)
        # 获取图片矩形大小
        self.rect = self.bullet.get_rect()
        # 初始化子弹坐标
        self.set_position(position)
        # 设置子弹速度
        self.speed = 15

    # 移动方法
    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    # 设置子弹坐标
    def set_position(self, position):
        # 设置存活属性
        self.survival = True
        # 子弹坐标设置
        self.rect.left, self.rect.top = position

