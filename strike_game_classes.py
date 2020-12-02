import pygame

# one class - one file
class Game:
    def __init__(self):
        self.game_run = True
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


class Player(GameObject):
    def __init__(self, speed):

        # changed to True
        self.fall = True

        self.jump_high_const = 8
        self.jump_high = self.jump_high_const
        self.jump_max_high = self.jump_high ** 2
        self.jump_status = False
        self.speed = speed
        self.fall_par = 0
        self.direction = None

    def set_pars(self, x, y, width, height):
        self.y = y
        self.x = x
        self.width = width
        self.height = height

    def jump(self):
        if self.jump_status: # added
            if abs(self.jump_high) <= self.jump_high_const:
                # use player.y or temporary var?
                # Now i use player.y
                if self.jump_high > 0:
                    self.y -= (-(self.jump_high ** 2) + self.jump_max_high) // 2
                if self.jump_high < 0:
                    self.y += (-(self.jump_high ** 2) + self.jump_max_high) // 2
                    # fall must be changed when collision to false
                    self.fall = True
                self.jump_status = True
                self.jump_high -= 1
            else:
                self.jump_status = False
                self.jump_high = self.jump_high_const

    def player_fall(self):
        self.fall_par += 1
        self.y += (self.fall_par ** 2)
