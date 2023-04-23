"""
@DATE: 2023/4/23
@Author  : ld
"""

# 游戏资源加载位置：
import pygame


pygame.init()

window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("加载图片")
window.fill((255, 255, 255))

# 1. 游戏启动页面静态图
## a. 加载图片
image1 = pygame.image.load("../files/images/background.jpg")
## b. 渲染图片  blit(渲染对象， 坐标系)
window.blit(image1, (0, 0))

## c. 操作图片
## （1） 获取大小
## blit(图片对象， 位置)
w, h = image1.get_size()
window.blit(image1, (400-w, 600-h))

## （2） 选装和缩放
## scale(图片对象， 目标大小)
scal_image = pygame.transform.scale(image1, (100, 200))
window.blit(scal_image, (w, 0))
## rotozoom(缩放/旋转对象， 旋转角度， 缩放比例)  旋转和缩放一起
roto_image = pygame.transform.rotozoom(image1, 0, 0.75)
window.blit(roto_image, (0, h))

## d. 刷新显示页面
## flip()  第一次刷新使用
## update() 第二次和以后的刷新
## pygame.display.update()
pygame.display.flip()


flag = True
while flag:
    # 2. 游戏帧刷新

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False



