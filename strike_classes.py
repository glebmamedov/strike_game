import pygame


class GameObject:
    def __init__(self, x, y, width, height):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.shape = None
        self.sur = None
        self.speed = None  # or zero

    def make_rect(self):
        self.shape = pygame.Rect(self.x, self.y, self.height, self.width)

    def make_surface(self, sur_x, sur_y):
        self.sur = pygame.Surface((sur_x, sur_y))

    # for objects like bullet
    # check if works with reversed direction
    def move_obj(self, speed):
        self.speed = speed
        self.shape = self.shape.move(speed, 0)


class Player(GameObject):
    def __init__(self, speed):
        self.fall = None
        self.jumpHigh = 8
        self.jumpMaxHigh = self.jumpHigh**2
        self.jumpStatus = False
        self.speed = speed

    def jump(self, jump_x):
        if abs(jump_x) <= self.jumpHigh:
            # use player.y or temporary var?
            # Now i use player.y
            if jump_x > 0:
                self.y -= (-(jump_x ** 2) + self.jumpMaxHigh) // 2
            if jump_x < 0:
                self.y += (-(jump_x ** 2) + self.jumpMaxHigh) // 2
                # fall must be changed when collision to false
                self.fall = True
            self.jumpStatus = True
        else:
            self.jumpStatus = False

