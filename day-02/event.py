"""
@DATE: 2023/4/24
@Author  : ld
"""
import pygame


pygame.init()


window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("事件")

window.fill((255, 255, 255))





pygame.display.flip()

flag = True
while flag:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            flag = False


