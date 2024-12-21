import sys
import pygame
from balls import BALLS
pygame.init()

# Sets width and height of the screen
size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0

# Creates a screen
screen = pygame.display.set_mode(size)

# Loads the image
ball = BALLS[0]
radius = ball["radius"]
ballrect = pygame.Rect(width // 2 - radius, height //
                       2 - radius, radius * 2, radius * 2)

# Box
wallleft = pygame.Surface((10, height))
wallleft.fill((255, 255, 255))
wallright = pygame.Surface((10, height))
wallright.fill((255, 255, 255))
wallbottom = pygame.Surface((width, 10))
wallbottom.fill((255, 255, 255))

wallleftrect = wallleft.get_rect(topleft=(0, 0))
wallrightrect = wallright.get_rect(topright=(width, 0))
wallbottomrect = wallbottom.get_rect(bottomleft=(0, height))

# Main loop
while True:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Moves the ball
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # Fills the screen with black
    screen.fill(black)
    # Draws the ball and walls

    screen.blit(wallleft, wallleftrect)
    screen.blit(wallright, wallrightrect)
    screen.blit(wallbottom, wallbottomrect)

    pygame.draw.circle(screen, ball["colour"], ballrect.center, radius)

    # Updates the screen
    pygame.display.flip()
