#!/usr/bin/python3
import pygame
import random

BLACK = (0, 0, 0)
BG = (230, 255, 230)
SNAKE = (127, 96, 51)
APPLE = (255, 40, 0)

FELD_H = 800
FELD_B = 800
QUADRAT_S_L = 20



pygame.init()
screen = pygame.display.set_mode ([FELD_B, FELD_H])
clock = pygame.time.Clock()


stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    screen.fill(BG)
    pygame.display.flip()
    clock.tick(25)

pygame.QUIT()
