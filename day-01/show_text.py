"""
@DATE: 2023/4/23
@Author  : ld
"""
import pygame

pygame.init()

window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("加载文字")
window.fill((255, 255, 255))


# =============显示文字==============
# 1. 创建字体对象
## Font(字体文件路径， 字号)
font = pygame.font.Font("../files/font/turok.ttf", 30)

# 2. 创建文字对象
## render(文字内容， True, 字体颜色， 背景颜色)
text = font.render("hello word， 你好世界", True, (90,90,90), (255, 0, 0))
# 3. 渲染到窗口上
window.blit(text, (0, 0))

# 4. 文字的操作




pygame.display.flip()

flag = True
while flag:
    # 帧刷新渲染

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
