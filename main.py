import pygame
import gameClasses
import sys


pygame.init()
screen = pygame.display.set_mode((600, 500))

topBorder = gameClasses.GameObject(600, 10, 0, 0)
bottomBorder = gameClasses.GameObject(600, 10, 0, 490)
rightBorder = gameClasses.GameObject(10, 480, 0, 10)
leftBorder = gameClasses.GameObject(10, 480, 590, 10)

brick = gameClasses.GameObject(80, 10, 30, 370)

borders = [topBorder.shape, bottomBorder.shape, rightBorder.shape, leftBorder.shape]
playerX = 10
playerY = 430
jumpH = 8
jumpSt = False
falling = False

step = 10
gameRun = True

player = gameClasses.GameObject(60, 60, playerX, playerY)


# edit func with consequences
def player_enter(num_mas, step, x, status):
    if num_mas[pygame.K_RIGHT]:
        x += step
    if num_mas[pygame.K_LEFT]:
        x -= step
    if keys[pygame.K_UP]:
        status = True
    return x, status


def player_jump(y, high, x, jumpstat, fall):
    x -= 1
    if abs(x) <= 8:
        if x > 0:
            y -= (-(x**2) + high)//2
        if x < 0:
            y += (-(x**2) + high)//2
            fall = True
        return y, x, jumpstat, fall
    else:
        fall = False
        jumpstatus = False
        return y, x, jumpstatus, fall


while gameRun:
    pygame.time.delay(40)
    playerPos = (player.x, player.y)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        if keys[pygame.K_ESCAPE]:
            gameRun = False

    player.x, jumpSt = player_enter(keys, step, player.x, jumpSt)

    if jumpSt:
        player.y, jumpH, jumpSt, falling = player_jump(player.y, 64, jumpH, jumpSt, falling)
    else:
        jumpH = 10
    print(falling)
    for border in borders:
        testRect = pygame.Rect(player.x, player.y, 60, 60)
        if testRect.colliderect(border):
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                player.x = playerPos[0]
    if player.shape.colliderect(brick.shape):
        if falling:
            jumpSt = False
            player.y = brick.height + 300
    print(player.y)
    player.shape = pygame.Rect(player.x, player.y, 60, 60)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (40, 240, 250), player.shape)
    pygame.draw.rect(screen, (250, 250, 0), brick.shape)
    pygame.draw.rect(screen, (20, 100, 50), topBorder.shape)
    pygame.draw.rect(screen, (20, 100, 20), bottomBorder.shape)
    pygame.draw.rect(screen, (50, 130, 60), rightBorder.shape)
    pygame.draw.rect(screen, (10, 230, 90), leftBorder.shape)
    pygame.display.update()