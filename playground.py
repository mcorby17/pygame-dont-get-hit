import pygame, sys, time

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))

# Set FPS so CPU doesn't execute blazingly fast
FPS = 30
fpsClock = pygame.time.Clock()

GUY = pygame.image.load('dood.png')
# Resize
GUY = pygame.transform.scale(GUY, (100, 100))
GUY_RECT = GUY.get_rect()

# Create square obstacle
Square_X = 0
Square_Y = 0
Square_Width = 100
Square_Height = 100
SQUARE = pygame.Rect(Square_X, Square_Y, Square_Width, Square_Height)

GUY_RECT.x = 200
GUY_RECT.y = 200

moveIncriment = 10

moveDirection = "None"

#for font in pygame.font.get_fonts():
#    print(str(font))

if pygame.font.get_init():
    ComicSans = pygame.font.SysFont(None, 200)
    GameOverText = ComicSans.render('WASTED', False, (255, 0, 0))
    print("Font initialized")

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
        GUY_RECT.x += 10
    elif moveDirection == "left":
        GUY_RECT.x -= 10
    elif moveDirection == "up":
        GUY_RECT.y -= 10
    elif moveDirection == "down":
        GUY_RECT.y += 10

    # Invert the incriment value whenever the square touches the edge of the screen
    SQUARE.x += moveIncriment
    if SQUARE.x > (SCREEN.get_width() - SQUARE.width) or \
    SQUARE.x <= -1:
        moveIncriment = -moveIncriment

    #print("SQUARE: " + str(SQUARE))

    SCREEN.fill((255, 255, 255))
    pygame.draw.rect(SCREEN, (255, 255, 0), SQUARE)
    SCREEN.blit(GUY, (GUY_RECT.x, GUY_RECT.y))

    #print("GUY RECT: " + str(GUY_RECT))

    if GUY_RECT.colliderect(SQUARE):
        SCREEN.blit(GameOverText, (200, 200))

    pygame.display.update()

    # Keep FPS at 30 so CPU does go nuts and
    # make the sprite shoot off in a blaze of fire
    fpsClock.tick(FPS)