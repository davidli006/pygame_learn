"""
@DATE: 2023/4/24
@Author  : ld
"""
import pygame


# 变量
win_width = 400
win_height = 600
cir_R = 25

pygame.init()

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("事件")
window.fill((255, 255, 255))
# 1. 显示一个静态的球
x, y = 50, 50
ball = pygame.draw.circle(window, (255, 0, 0), (x, y), cir_R)



pygame.display.flip()

print(ball)

flag = True
num = 1
x_speed = 1
y_speed = 1
while flag:
    num += 1
    if num % 3000 == 0:
        pygame.draw.circle(window, (255, 255, 255), (x, y), 25)
        x, y = x + x_speed, y + y_speed
        if x < cir_R or x > win_width - cir_R:
            x_speed = -x_speed
        if y < cir_R or y > win_height - cir_R:
            y_speed = -y_speed
        pygame.draw.circle(window, (255, 0, 0), (x, y), 25)

        pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False


