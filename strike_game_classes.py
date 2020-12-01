import pygame


class Game:
    def __init__(self):
        self.GameRun = True
        # idk what to set here
        pass


class Screen:
    def __init__(self):
        self.width = 600
        self.height = 500
        # change color and add background pictures
        self.color = (0, 0, 0)

    def set_screen(self):
        self.scr = pygame.display.set_mode((self.width, self.height))
    #def set_surface(self):
     #   self.surf =


class GameObject:
    def __init__(self, x, y, width, height):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.shape = None
        self.sur = None
        self.direction = None

    def make_rect(self):
        self.shape = pygame.Rect(self.x, self.y,  self.width, self.height)

    def make_surface(self, sur_x, sur_y):
        self.sur = pygame.Surface((sur_x, sur_y))

    # for objects like bullet
    # check if works with reversed direction
    def move_obj(self, speed):
        self.shape = self.shape.move(speed, 0)
        self.x = self.shape.x
        if speed > 0:
            self.direction = "right"
        if speed < 0:
            self.direction = "left"
        # maybe change to up or down dir
        if speed == 0:
            self.direction = "no"


class Player(GameObject):
    def __init__(self, speed):
        self.fall = True # changed to True
        self.jumpHighConst = 8
        self.jumpHigh = self.jumpHighConst
        self.jumpMaxHigh = self.jumpHigh**2
        self.jumpStatus = False
        self.speed = speed
        self.fall_par = 0
        self.direction = ''

    def set_pars(self, x, y, width, height):
        self.y = y
        self.x = x
        self.width = width
        self.height = height

    def jump(self):
        if abs(self.jumpHigh) <= self.jumpHighConst:
            # use player.y or temporary var?
            # Now i use player.y
            if self.jumpHigh > 0:
                self.y -= (-(self.jumpHigh ** 2) + self.jumpMaxHigh) // 2
            if self.jumpHigh < 0:
                self.y += (-(self.jumpHigh ** 2) + self.jumpMaxHigh) // 2
                # fall must be changed when collision to false
                self.fall = True
            self.jumpStatus = True
            self.jumpHigh -= 1
        else:
            self.jumpStatus = False
            self.jumpHigh = self.jumpHighConst

    def player_fall(self):
        self.fall_par += 1
        self.y += (self.fall_par ** 2) // 2
