import pygame
import random
from circle import Circle

screen = pygame.display.set_mode((800, 600))
circles = [] 
for i in range(100):
    crl = Circle(i * 800 // 100 * 2, i * 600 // 100, 50, color=(i*2.55, i*2.55, i*2.55))

    circles.append(crl)

YELLOW = (255, 255, 0)
RED  = (255, 0, 0)
color = YELLOW
speed = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((255, 255, 255))
    for c in circles:
        c.horizontal_movement(800)
        c.draw(screen)

    pygame.display.update()