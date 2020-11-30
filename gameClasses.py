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
        self.shape = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y

    def obj_draw(self):
        pass

    def obj_move(self, newX, newY):
        if __name__ == '__main__':
            self.shape = self.shape.move(newX, newY)


class Player(GameObject):
    def __init__(self, step):
        self.step = step

    def player_move(self, num_mas, step):
        if num_mas[pygame.K_UP]:
            y -= step
        if num_mas[pygame.K_DOWN]:
            y += step
        if num_mas[pygame.K_RIGHT]:
            x += step
        if num_mas[pygame.K_LEFT]:
            x -= step
        return x, y
