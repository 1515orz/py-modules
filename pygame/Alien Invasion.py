import sys
import pygame
import settings
import time
import os
pygame.init()

# 主窗口
screen_image = pygame.display.set_mode((800,600))  # FULLSCREEN代表全屏
screen_rect = screen_image.get_rect()

# 标题栏
pygame.display.set_caption('Alien Invasion')

# 飞船
ship_image = pygame.image.load('images/ship.bmp')
ship_rect = ship_image.get_rect()
ship_rect.midbottom = screen_rect.midbottom  # 用center函数让中心点重合，让图像位于窗口中心
ship_left = 3  # 飞船的命数

# 设置移动开关
moving_left = False  # 设置左键的'开关'
moving_right =False  # 设置右键的'开关'
shot_bullet = False

# 子弹
bullets = pygame.sprite.Group()  # 生成一个装精灵的空盒子(列表),只能装精灵
# bullets = []

# 数学计算,为了阵列表示敌人位置
enemy_image = pygame.image.load('images/enemy.bmp')
enemy_image_rect = enemy_image.get_rect()
enemy_width = enemy_image_rect.width
enemy_height = enemy_image_rect.height
# 将屏幕,敌人,飞船大小赋值计算,设计合理大小
screen_width, screen_height = screen_rect.size
ship_width ,ship_height = ship_rect.size
space_x = screen_width - 2 * enemy_width
space_y = screen_height - 4 * enemy_height
column_number = space_x // (5 * enemy_width)
line_number = space_y // (4 * enemy_height)

# 敌人

# enemies = {}
# for y in range(line_number):
#     for x in range(column_number):
#         enemy_image = pygame.image.load('images/enemy.bmp')
#         enemy_rect = enemy_image.get_rect()
#         enemy_rect.x = enemy_width + 2 * enemy_width * x
#         enemy_rect.y = enemy_height + 2 * enemy_width * y
#         enemies[enemy_image] = enemy_rect
#
# 使用精灵实现
enemies = pygame.sprite.Group()
# 创建敌人方阵
for y in range(line_number):
    for x in range(column_number):
        enemy_sprite = pygame.sprite.Sprite()
        enemy_sprite.image = pygame.image.load('images/enemy.bmp')
        enemy_sprite.rect = enemy_sprite.image.get_rect()
        enemy_sprite.rect.x = enemy_width + 5 * enemy_width * x
        enemy_sprite.rect.y = enemy_height + 2 * enemy_width * y
        enemies.add(enemy_sprite)

enemy_direction = settings.enemy_x_speed

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
                    new_bullet.rect = pygame.Rect(settings.bullet_set)  # 注意使用rect方法,而不是赋值
                    new_bullet.rect.midbottom = ship_rect.midbottom
                    bullets.add(new_bullet)  # add只能添加精灵,不能加别的东西


        elif event.type == pygame.KEYUP:  # 当松开按键时触发开关关闭
            # print(event)
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    # 添加飞船移动的边界条件
    if moving_left and ship_rect.left>0:  # 增加边界条件,在屏幕内运动
        ship_rect.x -= settings.ship_speed
    if moving_right and ship_rect.right < screen_rect.right:
        ship_rect.x += settings.ship_speed

    ship_sprite = pygame.sprite.Sprite()
    ship_sprite.image = ship_image
    ship_sprite.rect = ship_rect
    ship_sprite.image = pygame.Surface([100, 100])
    # 绘制图像
    screen_image.fill(settings.bg_color1)  # 绘制背景

    for bullet in bullets:
        pygame.draw.rect(screen_image,settings.bg_color2,bullet.rect)  # 画的是rect
        bullet.rect.y -= 1
        # print(bullet.rect.bottom,bullet.rect.midbottom)  # bottom底部的y一维坐标,而midbottom是一个二维坐标
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


    # 设置敌人碰到边界时的行为
    for enemy in enemies:
        ship_left -= 1
        if enemy.rect.right >= screen_rect.right or enemy.rect.left <= screen_rect.left:
            enemy_direction *= -1
            for enemy in enemies:
                enemy.rect.y += settings.enemy_y_speed
            break

    for enemy in enemies:
        enemy.rect.x += 1 *enemy_direction


    # # 绘制敌人
    # for key_image,value_image in enemies.items():
    #     screen_image.blit(key_image,value_image)

    # 精灵盒子自带draw方法,不需要for循环,只需要一个参数就可以绘制
    enemies.draw(screen_image)

    # 添加精灵模块的群组碰撞功能,四个参数(哪两个,群组碰撞,谁被,消灭)
    pygame.sprite.groupcollide(bullets,enemies,False,True)

    # 当敌人碰到飞船
    if pygame.sprite.spritecollideany(ship_sprite,enemies):  # spritecollideany判断如果碰撞
        ship_left -= 1
        enemies.empty()
        bullets.empty()
        for y in range(line_number):
            for x in range(column_number):
                enemy_sprite = pygame.sprite.Sprite()
                enemy_sprite.image = pygame.image.load('images/enemy.bmp')
                enemy_sprite.rect = enemy_sprite.image.get_rect()
                enemy_sprite.rect.x = enemy_width + 5 * enemy_width * x
                enemy_sprite.rect.y = enemy_height + 2 * enemy_width * y
                enemies.add(enemy_sprite)
        time.sleep(0.5)
        ship_rect.midbottom = screen_rect.midbottom

    # 敌人触底怎么办
    for enemy in enemies:
        if enemy.rect.bottom >= screen_rect.bottom:
            enemies.empty()
            bullets.empty()
            for y in range(line_number):
                for x in range(column_number):
                    enemy_sprite = pygame.sprite.Sprite()
                    enemy_sprite.image = pygame.image.load('images/enemy.bmp')
                    enemy_sprite.rect = enemy_sprite.image.get_rect()
                    enemy_sprite.rect.x = enemy_width + 5 * enemy_width * x
                    enemy_sprite.rect.y = enemy_height + 2 * enemy_width * y
                    enemies.add(enemy_sprite)
            time.sleep(0.5)
            ship_rect.midbottom = screen_rect.midbottom
            break # 这个break的意思时,只要检测到一个,就算玩家输,退出循环



    # 当敌人被消灭完之后
    if not enemies:  # 如果enemies列表为空,False
        bullets.empty()  # 清空当前子弹
        # 创建敌人方阵
        for y in range(line_number):
            for x in range(column_number):
                enemy_sprite = pygame.sprite.Sprite()
                enemy_sprite.image = pygame.image.load('images/enemy.bmp')
                enemy_sprite.rect = enemy_sprite.image.get_rect()
                enemy_sprite.rect.x = enemy_width + 5 * enemy_width * x
                enemy_sprite.rect.y = enemy_height + 2 * enemy_width * y
                enemies.add(enemy_sprite)

    # 绘制飞船
    screen_image.blit(ship_image, (ship_rect))



    # for bullet_rect in bullets:
    #     # draw.rect三个参数,(画在哪,什么颜色,画的什么)
    #     pygame.draw.rect(screen_image,settings.bg_color2,bullet_rect)
    #     bullet_rect.y -= 1
    #     if bullet_rect.bottom < 0:
    #         bullets.remove(bullet_rect)

    pygame.display.flip()
