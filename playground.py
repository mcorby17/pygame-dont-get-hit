import pygame, sys, random, os

# Control where the game window appears on startup
screen_xy = (100, 0)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % screen_xy

pygame.init()
random.seed()

# Set FPS so CPU doesn't execute blazingly fast
FPS = 30
fpsClock = pygame.time.Clock()

# Initialize font
Font = pygame.font.SysFont(None, 100)
GameOverText = Font.render('GAME OVER', False, (255, 0, 0))
GAME_OVER_RECT = GameOverText.get_rect()

# A Score font
ScoreFont = pygame.font.SysFont(None, 100)
SCORE = 0

SCREEN = pygame.display.set_mode((650, 650))
SCREEN_RECT = SCREEN.get_rect()

GAME_OVER_RECT.center = SCREEN_RECT.center

SPRITE = pygame.image.load('dood.png')

# Resize
SPRITE_IMAGE = pygame.transform.scale(SPRITE, (100, 120))
SPRITE_RECT = SPRITE_IMAGE.get_rect()

SPRITE_RECT.y = SCREEN_RECT.height - SPRITE_RECT.height
SPRITE_RECT.x = SCREEN_RECT.centerx

Square_Width = 100
Square_Height = 100

# Create square obstacle
Square_X = random.randrange(0, SCREEN.get_width() - Square_Width)
Square_Y = 0

# Get rect object so we can draw it more easily
SQUARE = pygame.Rect(Square_X, Square_Y, Square_Width, Square_Height)

SQUARE_MOVEMENT = 10
PIXELS_TO_MOVE = 10
GAME_OVER = False

while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()

    # Sprite movement
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_RIGHT]:
        SPRITE_RECT.x += PIXELS_TO_MOVE
    elif keysPressed[pygame.K_LEFT]:
        SPRITE_RECT.x -= PIXELS_TO_MOVE
    elif keysPressed[pygame.K_UP]:
        SPRITE_RECT.y -= PIXELS_TO_MOVE
    elif keysPressed[pygame.K_DOWN]:
        SPRITE_RECT.y += PIXELS_TO_MOVE

    # Square movement
    SQUARE.y += SQUARE_MOVEMENT

    # Regenerate another square
    if SQUARE.y >= SCREEN.get_height():
        SQUARE.y = 0
        SQUARE.x = random.randrange(0, SCREEN.get_width() - Square_Width)
        SQUARE_MOVEMENT += 1
        SCORE += 1

    # Check for a collision
    if SPRITE_RECT.colliderect(SQUARE):
        # Stop square and sprite
        SQUARE_MOVEMENT = 0
        PIXELS_TO_MOVE = 0
        GAME_OVER = True

    # Show Square and Sprite
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(SPRITE_IMAGE, SPRITE_RECT)
    pygame.draw.rect(SCREEN, (255, 255, 0), SQUARE)

    # Render score
    ScoreText = Font.render("Score: " + str(SCORE), False, (0, 0, 255))
    SCREEN.blit(ScoreText, (0, 0))

    # Only show game over message if the game is over... duh
    if GAME_OVER:
        SCREEN.blit(GameOverText, GAME_OVER_RECT)

    pygame.display.update()

    fpsClock.tick(FPS)
