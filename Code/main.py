#-*-coding:utf-8-*-

'''Create by Sheldon on 2018/2/18.
   Description :
   游戏主函数
   记录游戏初始化、碰撞判定、游戏规则划定等功能
'''

import pygame
from pygame.locals import *
import sys
import os
import traceback
import plane
import enemy
import bullet
import supply
from enemy import *

# 初始化
pygame.init()
pygame.mixer.init()

# 设置尺寸参数
bg_size = width,height = 480,800
# 设置窗口
screen = pygame.display.set_mode(bg_size)
# 设置标题
pygame.display.set_caption("飞机大战")
# 加载窗体图标
icon = pygame.image.load("images/icon.ico").convert_alpha()
# 设置窗体图标
pygame.display.set_icon(icon)
# 加载背景图片
background = pygame.image.load("images/bg.png").convert()
# 加载游戏开始图片
game_start = pygame.image.load("images/game_start.png").convert_alpha()
# 加载游戏重新开始图片
game_restart = pygame.image.load("images/game_restart.png").convert_alpha()
game_restart_rect = game_restart.get_rect()
game_restart_rect.left, game_restart_rect.top = width - game_restart_rect.width - 160, 520
# 加载游戏准备图片
game_loading1 = pygame.image.load("images/game_loading1.png").convert_alpha()
game_loading2 = pygame.image.load("images/game_loading2.png").convert_alpha()
game_loading3 = pygame.image.load("images/game_loading3.png").convert_alpha()
game_loading_rect = game_loading1.get_rect()
# 加载暂停图片
game_stop = pygame.image.load("images/game_stop.png").convert_alpha()
game_stop_rect = game_stop.get_rect()
# 加载游戏结束图片
game_over = pygame.image.load("images/game_over.png").convert()
# 加载暂停键图片
game_pause_nor = pygame.image.load("images/game_pause_nor.png").convert_alpha()
game_pause_pressed = pygame.image.load("images/game_pause_pressed.png").convert_alpha()
# 加载继续键图片
game_resume_nor = pygame.image.load("images/game_resume_nor.png").convert_alpha()
game_resume_pressed = pygame.image.load("images/game_resume_pressed.png").convert_alpha()
# 暂停键按钮范围值
paused_rect = game_pause_nor.get_rect()
paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
paused_image = game_pause_nor
resume_image = game_resume_nor
# 加载炸弹图片
bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
bomb_rect = bomb_image.get_rect()
bomb_font = pygame.font.Font("font/font.ttf",45)
bomb_num = 3
# 加载'生命'数量图片
life_image = pygame.image.load("images/life.png").convert_alpha()
life_rect = life_image.get_rect()
life_num = 3

# 设置音乐变量
bg_music = pygame.mixer.music
game_achievement_sound = pygame.mixer
game_over_sound = pygame.mixer
bullet_sound = pygame.mixer
enemy1_down_sound = pygame.mixer
enemy2_out_sound = pygame.mixer
enemy2_down_sound = pygame.mixer
enemy3_out_sound = pygame.mixer
enemy3_down_sound = pygame.mixer
pygame.mixer.set_num_channels(15)      # 设置音轨通道
volume = 0.6                           # 音量

# 加载游戏音乐,设置音量
bg_music.load("music/game_music.mp3")
game_achievement_sound = game_achievement_sound.Sound("music/game_achievement.wav")
game_over_sound = game_over_sound.Sound("music/game_over.wav")
bullet_sound = bullet_sound.Sound("music/bullet.wav")
enemy1_down_sound = enemy1_down_sound.Sound("music/enemy1_down.wav")
enemy2_out_sound = enemy2_out_sound.Sound("music/enemy2_out.wav")
enemy2_down_sound = enemy2_down_sound.Sound("music/enemy2_down.wav")
enemy3_out_sound = enemy3_out_sound.Sound("music/enemy3_out.wav")
enemy3_down_sound = enemy3_down_sound.Sound("music/enemy3_down.wav")
bg_music.set_volume(volume)
game_achievement_sound.set_volume(volume)
game_over_sound.set_volume(volume)
bullet_sound.set_volume(volume)
enemy1_down_sound.set_volume(volume)
enemy2_out_sound.set_volume(volume)
enemy2_down_sound.set_volume(volume)
enemy3_out_sound.set_volume(volume)
enemy3_down_sound.set_volume(volume)

# 基础参数
WHITE = (255,255,255)  # 白色
GREEN = (0, 255, 0)    # 绿色
RED = (255, 0, 0)      # 红色
destroy_speed = 2      # 销毁速度
bullet_speed = 10      # 子弹初始射速
msec = 45 * 1000       # 毫秒数

def main():
    run = True                      # 循环控制参数
    start = False                   # 游戏开始参数
    paussed = True                  # 暂停标志参数
    clock = pygame.time.Clock()     # 帧率控制
    delay = 100                     # 延迟设置
    score = 0                       # 设置得分
    grade1 = 50                     # 小型敌机分数
    grade2 = 300                    # 中型敌机分数
    grade3 = 600                    # 大型敌机分数
    level = 1                       # 等级水平
    life_num = 3                    # 生命数
    # 字体设置
    score_font = pygame.font.Font("font/font.ttf",35)
    game_over_font = pygame.font.Font("font/font.ttf",30)
    # 设置"游戏准备"图片精灵
    game_loadings = list()
    game_loadings_index = 0
    game_loadings_num = 3
    game_loadings.append(game_loading1)
    game_loadings.append(game_loading2)
    game_loadings.append(game_loading3)
    # 背景音乐播放
    bg_music.play(-1)
    # 实例化我方飞机
    hero = plane.Plane(bg_size)
    # 实例化敌机组
    enemies = pygame.sprite.Group()
    # 实例化小型敌机
    mini_enemise = pygame.sprite.Group()
    add_enemies('mini',bg_size,mini_enemise,enemies,16)
    # 实例化中型敌机
    medium_enemise = pygame.sprite.Group()
    add_enemies('medium', bg_size, medium_enemise, enemies, 8)
    # 实例化大型敌机
    large_enemise = pygame.sprite.Group()
    add_enemies('large',bg_size,large_enemise,enemies,4)
    # 实例化子弹
    bullets = []
    # 子弹索引下标
    bullets_index = 0
    # 子弹数目
    bullet_num = 4
    # 炮弹数目
    bomb_num = 3
    for i in range(bullet_num):
        bullets.append(bullet.Bullet(hero.rect.midtop))
    # 实例化补给
    bomb_supply = supply.Bomb_Supply(bg_size)
    # 设置一个定时事件
    supply_time =  USEREVENT
    pygame.time.set_timer(supply_time, msec)

    # 游戏循环
    while run:
        # 事件检测
        for event in pygame.event.get():
            # 右上角关闭按钮检测
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标点击检测
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    # 游戏开始
                    start = True
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paussed = not paussed
                    if not paussed:
                        pygame.time.set_timer(supply_time, 0)
                        # 暂停音效
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(supply_time, msec)
                        # 恢复音效
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                if event.button == 1 and game_restart_rect.collidepoint(event.pos):
                    # 重新开始
                    main()


            # 鼠标放置坐标检测
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paussed:
                        paused_image = game_resume_pressed
                    else:
                        paused_image = game_pause_pressed
                else:
                    if paussed:
                        paused_image = game_resume_nor
                    else:
                        paused_image = game_pause_nor
            # 键盘按键检测
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        enemy3_down_sound.play()
                        # 按下空格后，销毁屏幕内所有敌机
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.survival = False
            # 定时时间检测
            elif event.type == supply_time:
                bomb_supply.set_position()

        # 视情况提升等级
        if level < get_level(score) + 1:
            level += 1
            game_achievement_sound.play()
            # 增加一定批次的敌机
            add_enemies('mini', bg_size, mini_enemise, enemies, 3)
            add_enemies('medium', bg_size, medium_enemise, enemies, 2)
            add_enemies('large', bg_size, large_enemise, enemies, 1)
            # 提升小型敌机速度
            up_speed(mini_enemise, 1)
            print('等级提升')
            if not (level % 2) and bullet_num < 6:
                # 每提升两次敌机数量，就加一发子弹，上限是6
                print('子弹数目增加')
                bullet_num += 1
                bullets.append(bullet.Bullet(hero.rect.midtop))

        # 游戏开始
        if start:
            # 绘制背景图像
            screen.blit(background, (0, 0))
            # 绘制分数
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10,5))
            # 绘制炸弹
            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image,(10,height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))
            # 绘制暂停按钮
            screen.blit(paused_image, paused_rect)

            if life_num and paussed:
                # 碰撞检测
                enemies_down = pygame.sprite.spritecollide(hero,enemies, False, pygame.sprite.collide_mask)
                if enemies_down:
                    hero.survival = False
                    for enemy_down in enemies_down:
                        enemy_down.survival = False

                # 发射子弹
                if not(delay % bullet_speed):
                    bullets[bullets_index].set_position(hero.rect.midtop)
                    bullets_index = (bullets_index + 1) % bullet_num

                # 子弹碰撞检测
                for b in bullets:
                    if b.survival:
                        b.move()
                        screen.blit(b.bullet, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        # 被击中后
                        if enemy_hit:
                            b.survival = False
                            for e in enemy_hit:
                                if e in medium_enemise or e in large_enemise:
                                    e.hp -= 1
                                    e.hit = True
                                    if e.hp == 0: e.survival = False
                                else: e.survival = False

                # 绘制炸弹补给
                if bomb_supply.survival:
                    bomb_supply.move()
                    screen.blit(bomb_supply.bomb, bomb_supply.rect)
                    # 炸弹补给碰撞检测
                    if pygame.sprite.collide_mask(bomb_supply, hero):
                        if bomb_num < 3:
                            bomb_num += 1
                        # 销毁炸弹补给
                        bomb_supply.survival = False

                # 绘制小型敌机图像
                for mini_enemy in mini_enemise:
                    # 存活判断
                    if mini_enemy.survival:
                        # 小型敌机移动
                        mini_enemy.move()
                        # 绘制图像
                        screen.blit(mini_enemy.enemy,mini_enemy.rect)
                    else:
                        # 销毁敌机
                        if not(delay % destroy_speed):
                            if mini_enemy.spirits_index == 0:
                                # 播放敌机销毁声音
                                enemy1_down_sound.play()
                            # 绘制销毁动画
                            screen.blit(mini_enemy.death_spirits[mini_enemy.spirits_index], mini_enemy.rect)
                            mini_enemy.spirits_index = mini_enemy.spirits_index + 1
                            if mini_enemy.spirits_index == 4:
                                # 增加分数
                                score += grade1
                                # 重新设置敌机
                                mini_enemy.set_position()

                # 绘制中型敌机图像
                for medium_enemy in medium_enemise:
                    # 存活判断
                    if medium_enemy.survival:
                        # 中型敌机移动
                        medium_enemy.move()
                        # 被击中判定
                        if medium_enemy.hit:
                            screen.blit(medium_enemy.enemy_hit,medium_enemy.rect)
                            medium_enemy.hit = False
                        else:
                            # 绘制图像
                            screen.blit(medium_enemy.enemy,medium_enemy.rect)
                        # 绘制血槽
                        draw_start = (medium_enemy.rect.left, medium_enemy.rect.top - 5)
                        draw_end = (medium_enemy.rect.right, medium_enemy.rect.top - 5)
                        pygame.draw.line(screen, RED, draw_start, draw_end, 2)
                        # 计算剩余血量
                        surplus_hp = medium_enemy.hp / enemy.MediumEnemy.hp
                        draw_end = (medium_enemy.rect.left + medium_enemy.rect.width * surplus_hp, medium_enemy.rect.top - 5)
                        pygame.draw.line(screen, GREEN, draw_start, draw_end, 2)
                    else:
                        # 销毁敌机
                        if not(delay % destroy_speed):
                            if medium_enemy.spirits_index == 0:
                                # 播放敌机销毁声音
                                enemy2_down_sound.play()
                            # 绘制销毁动画
                            screen.blit(medium_enemy.death_spirits[medium_enemy.spirits_index], medium_enemy.rect)
                            medium_enemy.spirits_index = medium_enemy.spirits_index + 1
                            if medium_enemy.spirits_index == 4:
                                # 增加分数
                                score += grade2
                                # 重新设置敌机
                                medium_enemy.set_position()


                # 绘制大型敌机图像
                for large_enemy in large_enemise:
                    # 存活判断
                    if large_enemy.survival:
                        # 大型敌机移动
                        large_enemy.move()
                        # 被击中判定
                        if large_enemy.hit:
                            screen.blit(large_enemy.enemy_hit,large_enemy.rect)
                            large_enemy.hit = False
                        else:
                            # 绘制敌机图形
                            screen.blit(large_enemy.enemy,large_enemy.rect)
                        # 绘制血槽
                        draw_start = (large_enemy.rect.left,large_enemy.rect.top - 5)
                        draw_end = (large_enemy.rect.right,large_enemy.rect.top - 5)
                        pygame.draw.line(screen,RED, draw_start, draw_end,2)
                        # 计算剩余血量
                        surplus_hp = large_enemy.hp / enemy.LargeEnemy.hp
                        draw_end = (large_enemy.rect.left + large_enemy.rect.width * surplus_hp, large_enemy.rect.top - 5)
                        pygame.draw.line(screen,GREEN, draw_start, draw_end, 2)
                        if large_enemy.rect.bottom > -50:
                            # 播放敌机飞行声音
                            enemy3_out_sound.play(-1)
                    else:
                        # 销毁敌机
                        if not(delay % destroy_speed):
                            if large_enemy.spirits_index == 0:
                                # 播放敌机销毁声音
                                enemy3_down_sound.play()
                            # 绘制销毁动画
                            screen.blit(large_enemy.death_spirits[large_enemy.spirits_index],large_enemy.rect)
                            large_enemy.spirits_index = large_enemy.spirits_index + 1
                            if large_enemy.spirits_index == 6:
                                # 增加分数
                                score += grade3
                                # 关闭音效
                                enemy3_out_sound.stop()
                                # 重新设置敌机
                                large_enemy.set_position()

                # 绘制飞机图像
                if hero.survival:
                    # 检测键盘，控制我方飞机移动
                    hero.move()
                    screen.blit(hero.plane,hero.rect)
                else:
                    enemy2_down_sound.play()
                    if not(delay % destroy_speed):
                        # 绘制销毁动画
                        screen.blit(hero.death_spirits[hero.spirits_index], hero.rect)
                        hero.spirits_index = hero.spirits_index + 1
                        if hero.spirits_index == 3:
                            print("Code Over")
                            life_num -= 1
                            # 重新设置战机
                            hero.set_position()

                # 绘制飞机生命数量
                if life_num:
                    for i in range(life_num):
                        life_left = width - 10 - (i + 1) * life_rect.width
                        life_top = height - 10 - life_rect.height
                        screen.blit(life_image, (life_left, life_top))
            elif life_num == 0:
                # 读取历史最高分
                highest_score = int()
                # 判断记录文件是否存在，不存在则创建
                if not os.path.exists("score.txt"):
                    #os.mknod("score.txt")
                    highest_score = 0
                else:
                    # 文件存在着进行读取
                    with open("score.txt","r") as f:
                        highest_score = int(f.read())
                        f.close()
                # 若打破记录，则重新写入分数
                if score > highest_score:
                    with open("score.txt","w+") as f:
                        f.write(str(score))
                        f.close()
                # 绘制游戏结束背景图
                screen.blit(game_over, (0, 0))
                # 绘制最终得分
                if score < highest_score:
                    game_over_text = game_over_font.render("%s" % str(score), True, WHITE)
                else:
                    game_over_text = game_over_font.render("%s" % str(score), True, WHITE)
                over_text_width = str(score).__len__() + 50
                screen.blit(game_over_text, ((width - over_text_width) / 2, height / 2 ))
                # 绘制历史记录
                game_over_text = game_over_font.render("%s" % "Highest Score: " + str(highest_score), True, WHITE)
                over_text_width = (str(highest_score).__len__() + 15) * 12
                screen.blit(game_over_text, ((width - over_text_width) / 2, height / 2 + 60))
                # 绘制重新开始按钮
                screen.blit(game_restart, game_restart_rect)
                # 停止背景音乐
                pygame.mixer.music.pause()
                # 停止音效
                pygame.mixer.pause()
            else:
                # 绘制游戏停止标志图
                screen.blit(game_stop, ((width - game_stop_rect.width) / 2, (height - game_stop_rect.height) / 2))
        else:
            # 绘制背景图像
            screen.blit(background, (0, 0))
            # 绘制游戏名称
            screen.blit(game_start, (0, 0))
            # 绘制 loading 图像
            game_loading_X = (width - game_loading_rect.width) / 2
            game_loading_Y = (height - game_loading_rect.height) / 2 + 50
            screen.blit(game_loadings[game_loadings_index], (game_loading_X, game_loading_Y))
            # loding 下标变更
            if not (delay % 8):
                game_loadings_index = (game_loadings_index + 1) % game_loadings_num

        # 绘制界面（双缓冲）
        pygame.display.flip()
        # 帧率设置
        clock.tick(30)
        delay -= 1
        if delay == 0:delay = 10

if __name__ == '__main__':
    main()
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
