import pygame, sys

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))

# Set FPS so CPU doesn't execute blazingly fast
FPS = 30
fpsClock = pygame.time.Clock()

GUY = pygame.image.load('dood.png')
# Resize
GUY = pygame.transform.scale(GUY, (100, 100))

guy_x = 200
guy_y = 200

moveDirection = "None"

while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()

        # Keep track of movement direction
        # TODO: Place in a function
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_RIGHT]:
            moveDirection = "right"
        elif keysPressed[pygame.K_LEFT]:
            moveDirection = "left"
        elif keysPressed[pygame.K_UP]:
            moveDirection = "up"
        elif keysPressed[pygame.K_DOWN]:
            moveDirection = "down"

        # If a key has been let go, stop movement
        if event.type is pygame.KEYUP:
            moveDirection = "None"

    # Change pixel location based on movement type
    # TODO: place in function
    if moveDirection == "right":
        guy_x += 10
    elif moveDirection == "left":
        guy_x -= 10
    elif moveDirection == "up":
        guy_y -= 10
    elif moveDirection == "down":
        guy_y += 10

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(GUY, (guy_x, guy_y))
    pygame.display.update()

    # Keep FPS at 30 so CPU does go nuts and
    # make the sprite shoot off in a blaze of fire
    fpsClock.tick(FPS)