#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo1.py
   @author:zl
   @time: 2025/7/25 17:05
   @software:PyCharm
   @desc:
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 小球属性

ball_radius = 20
ball_x, ball_y = 400, 300
ball_speed_x, ball_speed_y = 5, 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 按键检测
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 移动逻辑
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed_x

    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed_x

    if keys[pygame.K_UP]:
        ball_y -= ball_speed_y

    if keys[pygame.K_DOWN]:
        ball_y += ball_speed_y

    # 边界碰撞检测
    if ball_x - ball_radius < 0 or ball_x + ball_radius > screen.get_width():
        ball_speed_x *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > screen.get_height():
        ball_speed_y *= -1
    # 渲染
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
























