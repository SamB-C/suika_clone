import sys
import pygame

import ballmotion

pygame.init()

# Sets width and height of the screen
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

# Creates a screen
screen = pygame.display.set_mode(size)

# Creates game clock and sets target frames per second
clock = pygame.time.Clock()
fps = 60

# Defines acceleration due to gravity
gravity = 9.8

# Loads the image
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# Main loop
while True:
    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    # Moves the ball
    ballrect = ballrect.move(speed)
    print(ballrect.bottom, speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # Accelerates ball
    speed = ballmotion.calc_speed(speed, gravity, fps)

    # Fills the screen with black
    screen.fill(black)
    # Draws the ball
    screen.blit(ball, ballrect)
    # Updates the screen
    pygame.display.flip()
    # Waits for next frame
    clock.tick(fps)
