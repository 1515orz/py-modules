import pygame
import time
import sys
import bg_color


pygame.init()


screen_image = pygame.display.set_mode((800,600))


# 菜单
pygame.display.set_caption('Alien Invasion')  # 设置程序标题
screen_image.fill(bg_color.bg_color1)
screen_rect = screen_image.get_rect()

# 飞船
ship_image = pygame.image.load('images/round.bmp')
ship_rect = ship_image.get_rect()
ship_rect.center = screen_rect.center

screen_image.blit(ship_image,ship_rect)


pygame.display.flip()





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 假如输入指令为关闭按钮
            sys.exit()  # 则退出程序

