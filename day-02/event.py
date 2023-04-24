"""
@DATE: 2023/4/24
@Author  : ld
"""
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("事件")
window.fill((255, 255, 255))
pygame.display.flip()

font = pygame.font.Font("../files/font/simkai.ttf", 30)


flag = True
x_, y_ = 0, 0
x_text = 0
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出
            flag = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_, y_ = event.pos
            pygame.draw.circle(window, (255, 0,  0), (x_, y_), 25)
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.draw.circle(window, (255, 255,255), (x_, y_), 25)

        elif event.type == pygame.KEYDOWN:
            text = chr(event.key)
            tx = font.render(text, True, (255, 0, 0))
            window.blit(tx, (x_text, 0))
            x_text += 15


        pygame.display.update()
