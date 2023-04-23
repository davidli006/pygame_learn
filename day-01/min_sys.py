"""
@DATE: 2023/4/23
@Author  : ld
"""
import time

import pygame

# 1. 初始化操作
pygame.init()


# 2. 创建游戏窗口
# set_mode(大小)
window = pygame.display.set_mode((400, 600))

# 设置游戏标题
pygame.display.set_caption("我的游戏")
# 设置背景颜色
window.fill((255, 255, 255))


# 3. 游戏保持运行状态
# game loop (游戏循环)
while True:
    for event in pygame.event.get():
        print(event, event.type)
        if event.type == pygame.QUIT:
            exit()