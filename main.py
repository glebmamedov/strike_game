import pygame
import strike_game_classes as scls


pygame.init()

run = True
screen = scls.Screen()
screen.set_screen()

floorBorderWidth = 10
verticalBorderWidth = 1
playerHeight = 60
playerWidth = 40

# player start position depends on connection queue
player = scls.Player(10)
floorBorder = scls.GameObject(
    0, screen.height - floorBorderWidth,
    screen.width, floorBorderWidth)
verticalLeftBorder = scls.GameObject(
    0, 0,
    verticalBorderWidth, screen.height)
verticalRightBorder = scls.GameObject(
    screen.width - verticalBorderWidth,
    0, verticalBorderWidth, screen.height)

borders = [floorBorder, verticalRightBorder, verticalLeftBorder]

# replace with surfaces
verticalRightBorder.make_rect()
verticalLeftBorder.make_rect()
floorBorder.make_rect()

player.set_pars(
    490, screen.height - (floorBorderWidth + playerHeight),
    playerWidth, playerHeight)
player.make_rect()

while run:
    pygame.time.delay(40)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False

    if keys[pygame.K_LEFT]:
        player.move_obj(-player.speed)
    if keys[pygame.K_RIGHT]:
        player.move_obj(player.speed)
    if keys[pygame.K_UP]:
        player.jumpStatus = True
    if player.jumpStatus:
        player.jump()

    if player.fall:
        player.player_fall()

    # collisions
    # fix border space
    for border in borders:
        testrect = pygame.Rect(player.x, player.y, playerWidth, playerHeight)
        if testrect.colliderect(border.shape):
            if border.shape == floorBorder.shape:
                # for start is None
                player.fall = False
            if player.direction == "right":
                player.x -= player.speed
            if player.direction == "left":
                player.x += player.speed

    print(player.fall)

    player.make_rect()
    screen.scr.fill((0, 0, 0))
    pygame.draw.rect(screen.scr, (0, 0, 250), player.shape)
    pygame.draw.rect(screen.scr, (0, 250, 0), verticalRightBorder.shape)
    pygame.draw.rect(screen.scr, (0, 250, 0), verticalLeftBorder.shape)
    pygame.draw.rect(screen.scr, (250, 0, 0), floorBorder.shape)
    pygame.display.update()