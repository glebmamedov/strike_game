import  pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
x = 50
y = 50
width = 60
height = 90
speed = 10
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_DOWN]:
        y += speed
    if pressed_keys[pygame.K_LEFT]:
        x -= speed
    if pressed_keys[pygame.K_RIGHT]:
        x += speed
    if pressed_keys[pygame.K_UP]:
        y -= speed
    pygame.draw.rect(screen, (0, 0, 250), (x, y, width, height))
    pygame.display.update()
    pygame.displa

