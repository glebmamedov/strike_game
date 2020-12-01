import pygame


class Screen:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color


class Game:
    def __init__(self):
        self.gameRun = True


class GameObject:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.shape = pygame.Rect(x, y, width, height)
        self.top = self.shape.top
        self.bottom = self.shape.bottom

    def obj_draw(self):
        pass

    def obj_move(self, newX, newY):
        self.shape = self.shape.move(newX, newY)

    def obj_step(self, step, num_mas, x):
        if num_mas[pygame.K_RIGHT]:
            x += step
        if num_mas[pygame.K_LEFT]:
            x -= step
        # self.shape = pygame.Rect(x, self.y, self.width, self.height)
        return x


class Player(GameObject):
    def __init__(self, step):
        self.step = step

# edit jump
    def player_jump(self):
        self.y = y**2 - 12