import pygame
import strike_game_classes


pygame.init()

run = True
screen = strike_game_classes.Screen()
screen.set_screen()

floor_rect_width = 20
floor_surf_width = 10
vertical_border_width = 1
player_height = 60
player_width = 40
brick_width = 90

# the position difference : rectpos - surfpos
# player start position depends on connection queue
player = strike_game_classes.Player(10)
floor_border = strike_game_classes.GameObject(
    0, screen.height - floor_rect_width,
    screen.width, floor_rect_width)
vertical_left_border = strike_game_classes.GameObject(
    0, 0,
    vertical_border_width, screen.height)
vertical_right_border = strike_game_classes.GameObject(
    screen.width - vertical_border_width,
    0, vertical_border_width, screen.height)
shelf1 = strike_game_classes.GameObject(
    0, 400, brick_width, floor_rect_width
)
shelf2 = strike_game_classes.GameObject(
    70, 300, brick_width, floor_rect_width
)

# replace with surfaces
shelf2.make_rect()
shelf1.make_rect()
vertical_right_border.make_rect()
vertical_left_border.make_rect()
floor_border.make_rect()

floor_border_surface = pygame.Surface((screen.width, floor_surf_width))
shelf1_surface = pygame.Surface((brick_width, floor_surf_width))
shelf2_surface = pygame.Surface((brick_width, floor_surf_width))

floor_borders = []

floor_borders.append([floor_border_surface, floor_border.shape])
floor_borders.append([shelf1_surface, shelf1.shape])
floor_borders.append([shelf2_surface, shelf2.shape])

vertical_borders = [vertical_left_border, vertical_right_border]

player.set_pars(
    400, screen.height - (floor_rect_width + player_height),
    player_width, player_height)
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
    if keys[pygame.K_DOWN]:
        player.fall = True
    if keys[pygame.K_UP]:
        player.jump_status = True
    if player.jump_status:
        player.jump()

    # collisions
    # using iteration is not a good idea
    for border in floor_borders:
        testrect = pygame.Rect(player.x, player.y, player_width, player_height)
        if testrect.colliderect(border[1]):
            if player.fall:
                player.fall = False
                player.jump_status = False
                player.y = border[1].bottom - border[0].get_height() - player.height
                print(border[1].top, border[1].bottom)

    if testrect.colliderect(vertical_left_border.shape):
        player.x = 0
    if testrect.colliderect(vertical_right_border.shape):
        player.x = screen.width - player.width

    if player.fall:
        player.player_fall()
    else:
        player.fall_par = 0

    player.make_rect()
    screen.scr.fill((0, 0, 0))
    pygame.draw.rect(screen.scr, (0, 0, 250), player.shape)
    pygame.draw.rect(
        screen.scr,
        (0, 250, 0),
        (0, 410, shelf1_surface.get_width(),
         shelf1_surface.get_height()))
    pygame.draw.rect(
        screen.scr,
        (250, 0, 0),
        (0, screen.height - floor_surf_width,
         floor_border_surface.get_width(),
         floor_border_surface.get_height()))
    pygame.draw.rect(
        screen.scr,
        (0, 250, 0),
        (70, 310, shelf2_surface.get_width(),
         shelf2_surface.get_height())
    )
    pygame.display.update()
