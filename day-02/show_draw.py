"""
@DATE: 2023/4/24
@Author  : ld
"""
import pygame


pygame.init()



window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("图形展示")
window.fill((255, 255, 255))

# ================显示图形====================
# 1. 画直线
## line(画在哪， 线的颜色， 起点， 终点, 线宽)
pygame.draw.line(window, (255, 0, 0), (0, 0), (400, 50), 5)

# 2. 画折线
## lines(画在哪， 线的颜色， 是否闭合)
points = [(0, 50), (150, 100), (300, 50), (400, 100)]
pygame.draw.lines(window, (0, 255, 0), False, points, 3)

# 3. 画圆
# circle(画在哪， 线的颜色， 圆心坐标， 半径， 线宽)
pygame.draw.circle(window, (0, 0, 255), (110, 150), 50, 2)

# 4. 画矩形
# rect(画在哪， 线的颜色， 矩形范围， 线宽)
pygame.draw.rect(window, (90, 90, 90), (10, 210, 100, 50), 3)

# 5. 画椭圆
# ellipse(画在哪， 线的颜色， 矩形范围， 线宽)
pygame.draw.ellipse(window, (255, 90, 90), (120, 210, 100, 50), 3)

# 6. 画弧线
# arc(画在哪， 线的颜色， 矩形范围， 起始弧度， 终止弧度）
pygame.draw.arc(window, (90, 255, 90), (0, 280, 100, 50), 0, 3.14/1.5, 5)


pygame.display.flip()

flag = True
while flag:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
