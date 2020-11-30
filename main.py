import pygame
import gameClasses

pygame.init()
screen = pygame.display.set_mode((600, 500))

topBorder = gameClasses.GameObject(600, 10, 0, 0)
bottomBorder = gameClasses.GameObject(600, 10, 0, 490)
rightBorder = gameClasses.GameObject(10, 480, 0, 10)
leftBorder = gameClasses.GameObject(10, 480, 590, 10)

borders = [topBorder.shape, bottomBorder.shape, rightBorder.shape, leftBorder.shape]
playerX = 40
playerY = 40

step = 10
gameRun = True


def player_enter(num_mas, step, x, y):
    if num_mas[pygame.K_UP]:
        y -= step
    if num_mas[pygame.K_DOWN]:
        y += step
    if num_mas[pygame.K_RIGHT]:
        x += step
    if num_mas[pygame.K_LEFT]:
        x -= step
    return x, y


while gameRun:
    pygame.time.delay(50)
    playerPos = (playerX, playerY)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        if keys[pygame.K_ESCAPE]:
            gameRun = False

    playerX, playerY = player_enter(keys, step, playerX, playerY)
    for border in borders:
        testRect = pygame.Rect(playerX, playerY, 60, 60)
        if testRect.colliderect(border):
            playerX, playerY = playerPos

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (40, 240, 250), (playerX, playerY, 60, 60 ))
    pygame.draw.rect(screen, (20, 100, 50), topBorder.shape)
    pygame.draw.rect(screen, (20, 100, 20), bottomBorder.shape)
    pygame.draw.rect(screen, (50, 130, 60), rightBorder.shape)
    pygame.draw.rect(screen, (10, 230, 90), leftBorder.shape)
    pygame.display.update()