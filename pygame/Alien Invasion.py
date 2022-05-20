import sys
import pygame
import settings
import time

pygame.init()

# 主窗口
screen_image = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  # FULLSCREEN代表全屏
screen_rect = screen_image.get_rect()

# 标题栏
pygame.display.set_caption('Alien Invasion')

# 飞船
ship_image = pygame.image.load('images/ship.bmp')
ship_rect = ship_image.get_rect()
ship_rect.midbottom = screen_rect.midbottom  # 用center函数让中心点重合，让图像位于窗口中心

# 设置移动开关
moving_left = False  # 设置左键的'开关'
moving_right =False  # 设置右键的'开关'

# # 子弹
bullets = pygame.sprite.Group()  # 生成一个装精灵的空盒子(列表),只能装精灵
# bullets = []


# 死循环
while True:
    # 捕获所有操作
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:  # 当输入空格时产生子弹
                if len(bullets) < settings.bullet_allowed:
                    # 精灵对象可以拥有image和rect属性
                    new_bullet = pygame.sprite.Sprite()  # 生成一个精灵对象
                    new_bullet.rect = pygame.Rect(0,0,3,15)  # 注意使用rect方法,而不是赋值
                    new_bullet.rect.midbottom = ship_rect.midbottom
                    bullets.add(new_bullet)  # add只能添加精灵,不能加别的东西
            # if len(bullets) < 5:  # 当子弹数目小于5时才被创建
            #     if event.key == pygame.K_SPACE:  # 当输入空格时产生子弹
            #         new_bullet_rect = pygame.Rect(0,0,3,15)
            #         new_bullet_rect.midbottom = ship_rect.midbottom
            #         bullets.append(new_bullet_rect)

        elif event.type == pygame.KEYUP:  # 当松开按键时触发开关关闭
            print(event)
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    if moving_left and ship_rect.left>0:  # 增加边界条件,在屏幕内运动
        ship_rect.x -= settings.ship_speed
    if moving_right and ship_rect.right < screen_rect.right:
        ship_rect.x += settings.ship_speed


    # 绘制图像
    screen_image.fill(settings.bg_color1)  # 绘制背景

    for bullet in bullets:
        pygame.draw.rect(screen_image,settings.bg_color2,bullet.rect)  # 画的是rect
        bullet.rect.y -= 1
        print(bullet.rect.bottom,bullet.rect.midbottom)  # bottom底部的y一维坐标,而midbottom是一个二维坐标
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # 绘制飞船
    screen_image.blit(ship_image, (ship_rect))



    # for bullet_rect in bullets:
    #     # draw.rect三个参数,(画在哪,什么颜色,画的什么)
    #     pygame.draw.rect(screen_image,settings.bg_color2,bullet_rect)
    #     bullet_rect.y -= 1
    #     if bullet_rect.bottom < 0:
    #         bullets.remove(bullet_rect)

    pygame.display.flip()
