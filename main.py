import sys
import pygame
pygame.init()

# Sets width and height of the screen
size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0

# Creates a screen
screen = pygame.display.set_mode(size)

# Loads the image
radius = 20
ballrect = pygame.Rect(width // 2 - radius, height //
                       2 - radius, radius * 2, radius * 2)

# Main loop
while True:
    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Moves the ball
    ballrect = ballrect.move(speed)

    # Logic for ball to bounce
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # Fills the screen with black
    screen.fill(black)
    # Draws the ball
    pygame.draw.circle(screen, (255, 255, 255), ballrect.center, radius)
    # Updates the screen
    pygame.display.flip()
