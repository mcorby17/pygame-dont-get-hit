import pygame, sys

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))

FPS = 30
fpsClock = pygame.time.Clock()

GUY = pygame.image.load('dood.png')

guy_x = 200
guy_y = 200

moveDirection = "None"

while True:
    for event in pygame.event.get():
        #print(str(event))
        if event.type is pygame.QUIT:
            sys.exit()

        keysPressed = pygame.key.get_pressed()
        #print(str(keysPressed))
        if keysPressed[pygame.K_RIGHT]:
            moveDirection = "right"
        elif keysPressed[pygame.K_LEFT]:
            moveDirection = "left"

        if event.type is pygame.KEYUP:
            moveDirection = "None"

    if moveDirection == "right":
        guy_x += 10
    elif moveDirection == "left":
        guy_x -= 10

    SCREEN.fill((0, 0, 0))
    SCREEN.blit(GUY, (guy_x, guy_y))
    pygame.display.update()
    fpsClock.tick(FPS)