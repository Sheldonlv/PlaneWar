#-*-coding:utf-8-*-

'''Create by Sheldon on 2018/2/21.
   Description :
   管理敌机的类
   记录初始化各类型敌机、移动管理等方法
'''

import pygame
from random import *

# 小型敌机类
class MiniEnemy(pygame.sprite.Sprite):

    # 初始化类
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载敌机素材
        self.enemy1 = pygame.image.load("images/enemy1.png").convert_alpha()
        self.enemy = self.enemy1
        # 获取敌机实际像素区域
        self.mask = pygame.mask.from_surface(self.enemy)
        # 设置精灵列表
        self.death_spirits = list()
        # 加载精灵素材
        self.spirit1 = pygame.image.load("images/enemy1_down1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/enemy1_down2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/enemy1_down3.png").convert_alpha()
        self.spirit4 = pygame.image.load("images/enemy1_down4.png").convert_alpha()
        # 将精灵存放进精灵列表中
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3, self.spirit4])
        # 设置精灵列表播放下标
        self.spirits_index = 0
        # 敌机尺寸
        self.rect = self.enemy1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 敌机速度
        self.speed = 2
        # 初始化位置
        self.set_position()

    # 敌机移动类
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.set_position()

    # 定义敌机初始位置
    def set_position(self):
        # 设置存活属性
        self.survival = True
        # 连同精灵下标也归零
        self.spirits_index = 0
        # 敌机出现时左侧坐标
        self.rect.left = randint(0, self.width - self.rect.width)
        # 敌机出现时顶部坐标
        self.rect.top = randint(-3 * self.height, 0)

# 中型敌机类
class MediumEnemy(pygame.sprite.Sprite):
    hp = 5

    # 初始化类
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载中型敌机素材
        self.enemy2 = pygame.image.load("images/enemy2.png").convert_alpha()
        self.enemy = self.enemy2
        # 加载被击中素材
        self.enemy_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        # 设置是否被击中的参数
        self.hit = False
        # 获取敌机实际像素区域
        self.mask = pygame.mask.from_surface(self.enemy)
        # 设置精灵列表
        self.death_spirits = list()
        # 加载精灵素材
        self.spirit1 = pygame.image.load("images/enemy2_down1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/enemy2_down2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/enemy2_down3.png").convert_alpha()
        self.spirit4 = pygame.image.load("images/enemy2_down4.png").convert_alpha()
        # # 将精灵存放进精灵列表中
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3, self.spirit4])
        # 设置精灵列表播放下标
        self.spirits_index = 0
        # 敌机尺寸
        self.rect = self.enemy2.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 敌机速度
        self.speed = 1.5
        # 初始化位置
        self.set_position()

    # 敌机移动类
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.set_position()

    # 定义敌机初始位置
    def set_position(self):
        # 设置存活属性
        self.survival = True
        # 设置血量
        self.hp = MediumEnemy.hp
        # 连同精灵下标也归零
        self.spirits_index = 0
        # 敌机出现时左侧坐标
        self.rect.left = randint(0, self.width - self.rect.width)
        # 敌机出现时顶部坐标
        self.rect.top = randint(-5 * self.height, -self.height)

# 大型敌机类
class LargeEnemy(pygame.sprite.Sprite):
    hp = 15

    # 初始化类
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 加载大型敌机素材
        self.enemy3_n1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.enemy3_n2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.enemy = self.enemy3_n1
        # 加载被击中素材
        self.enemy_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        # 设置是否被击中的参数
        self.hit = False
        # 获取敌机实际像素区域
        self.mask = pygame.mask.from_surface(self.enemy)
        # 设置精灵列表
        self.death_spirits = list()
        # 加载精灵素材
        self.spirit1 = pygame.image.load("images/enemy3_down1.png").convert_alpha()
        self.spirit2 = pygame.image.load("images/enemy3_down2.png").convert_alpha()
        self.spirit3 = pygame.image.load("images/enemy3_down3.png").convert_alpha()
        self.spirit4 = pygame.image.load("images/enemy3_down4.png").convert_alpha()
        self.spirit5 = pygame.image.load("images/enemy3_down5.png").convert_alpha()
        self.spirit6 = pygame.image.load("images/enemy3_down6.png").convert_alpha()
        # # 将精灵存放进精灵列表中
        self.death_spirits.extend([self.spirit1, self.spirit2, self.spirit3, self.spirit4, self.spirit5, self.spirit6])
        # 设置精灵列表播放下标
        self.spirits_index = 0
        # 切换参数
        self.switch = True
        # 计数器总数
        self.count = 5
        # 计数器
        self.scaler = self.count
        # 敌机尺寸
        self.rect = self.enemy3_n1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 敌机速度
        self.speed = 1
        # 初始化位置
        self.set_position()

    # 敌机移动类
    def move(self):
        # 控制敌机移动
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.set_position()
        # 控制图片切换
        if self.switch:
            self.enemy = self.enemy3_n1
        else:
            self.enemy = self.enemy3_n2
        # 计数器判定
        if self.scaler == 0:
            self.switch = not self.switch
            self.scaler = self.count
        # 计数器计数
        self.scaler -= 1

    # 定义敌机初始位置
    def set_position(self):
        # 设置存活属性
        self.survival = True
        # 设置血量
        self.hp = LargeEnemy.hp
        # 连同精灵下标也归零
        self.spirits_index = 0
        # 敌机出现时左侧坐标
        self.rect.left = randint(0, self.width - self.rect.width)
        # 敌机出现时顶部坐标
        self.rect.top = randint(-6 * self.height, -3 * self.height)

# 添加敌机组（敌机类型，背景大小，敌机组1，敌机组2，生成敌机数量）
def add_enemies(size,bg_size,group1,group2,num):
    for i in range(num):
        if(size == 'mini'):
            enemy = MiniEnemy(bg_size)
        if(size == 'medium'):
            enemy = MediumEnemy(bg_size)
        if(size == 'large'):
            enemy = LargeEnemy(bg_size)
        group1.add(enemy)
        group2.add(enemy)

# 提示敌机速度
def up_speed(group, index):
    for each in group:
        each.speed += index

# 开幂
def get_level(num):
    result = 0
    if num >= 4092:
        num2 = 1
        while num2 < num:
            num2 *= 2
            result += 1
        result -= 12
    return result
