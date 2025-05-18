import pygame
import random
from circle import Circle

screen = pygame.display.set_mode((800, 600))
circles = [] 
for i in range(100):
    crl = Circle(i * 800 // 100 * 2, i * 600 // 100, 50, color=(i*2.55, i*2.55, i*2.55))

    circles.append(crl)
clock = pygame.time.Clock()
FPS = 200


YELLOW = (255, 255, 0)
RED  = (255, 0, 0)
color = YELLOW
speed = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressed = pygame.mouse.get_pressed() 
    if pressed[0] == True:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
    if pressed[2] == True:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 4, 4))
    pygame.display.update()
    clock.tick(FPS)