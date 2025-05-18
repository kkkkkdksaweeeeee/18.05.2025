import pygame

class Circle: 
    
    # конструктор для инициализации параметров
    def __init__(self, x, y, r, color):
        # self - имя каждого обьекта
        self.x = x
        self.y = y
        self.r = r
        self.dir = "right"
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        
    def move_by_keys(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] == True:
            self.y -= 3
        if pressed[pygame.K_DOWN] == True:
            self.y += 3
        if pressed[pygame.K_LEFT] == True:
            self.x -= 3
        if pressed[pygame.K_RIGHT] == True:
            self.x += 3 

    def horizontal_movement(self, WIDTH):
        if self.dir == "right":
            self.x += 1
        elif self.dir == "left":
            self.x -= 1

        if self.x > WIDTH:
            self.dir = "left"
        elif self.x < 0:
            self.dir = "right"