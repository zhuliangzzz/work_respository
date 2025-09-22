#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo3.py
   @author:zl
   @time: 2025/8/23 16:24
   @software:PyCharm
   @desc:
"""
import sys

import pygame



pygame.init()
clock = pygame.time.Clock()
size = width, height = 1000, 900
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

ball = pygame.image.load('images/earth.png')
ball_rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ball_rect = ball_rect.move(speed)
    # if ball_rect.left < 0 or ball_rect.right > width:
    #     speed[0] = -speed[0]
    # if ball_rect.top < 0 or ball_rect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
    clock.tick(60)
