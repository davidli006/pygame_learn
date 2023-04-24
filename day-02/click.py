"""
@DATE: 2023/4/24
@Author  : ld
"""
import pygame

WIDTH = 400
HEIGHT = 600

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("点击事件")
window.fill((255, 255, 255))

font = pygame.font.Font("../files/font/simkai.ttf", 30)

# 1. 确定按钮
bx1, by1, bw1, bh1 = 30, 100, 100, 50
pygame.draw.rect(window, (0, 255, 0), (bx1, by1, bw1, bh1))
text1 = font.render("确定", True, (255, 255, 255))
w, h = text1.get_size()
tx1 = bx1 + (bw1-w)/2
ty1 = by1 + (bh1-h)/2
window.blit(text1, (tx1, ty1))

# 2. 取消按钮
bx2, by2, bw2, bh2 = 30, 200, 100, 50
pygame.draw.rect(window, (255, 0, 0), (bx2, by2, bw2, bh2))
text2 = font.render("取消", True, (255, 255, 255))
w, h = text1.get_size()
tx2 = bx2 + (bw2-w)/2
ty2 = by2 + (bh2-h)/2
window.blit(text2, (tx2, ty2))


pygame.display.flip()
flg = True
while flg:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flg = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if bx1 <= mx <= bx1+bw1 and by1<= my <= by1+bh1:
                pygame.draw.rect(window, (200, 200, 200), (bx1, by1, bw1, bh1))
                window.blit(text1, (tx1, ty1))

                print("确定")
            elif bx2 <= mx <= bx2+bw2 and by2<= my <= by2+bh2:
                pygame.draw.rect(window, (200, 200, 200), (bx2, by2, bw2, bh2))
                window.blit(text2, (tx2, ty2))
                print("取消")

        if event.type == pygame.MOUSEBUTTONUP:
            pygame.draw.rect(window, (0, 255, 0), (bx1, by1, bw1, bh1))
            window.blit(text1, (tx1, ty1))
            pygame.draw.rect(window, (255, 0, 0), (bx2, by2, bw2, bh2))
            window.blit(text2, (tx2, ty2))

        pygame.display.update()




