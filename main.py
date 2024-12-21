import sys
import pygame
from balls import BALLS, create_ball
from typing import List
from dict_types import BallRectType

from ballmotion import close_to_floor, calc_speed

pygame.init()

# Sets width and height of the screen
size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0

# Creates a screen
screen = pygame.display.set_mode(size)

# Creates game clock and sets target frames per second
clock = pygame.time.Clock()
fps = 60

# Defines acceleration due to gravity
gravity = 9.8

#  Creates the balls
balls: List[BallRectType] = []
for i in range(len(BALLS)):
    balls.append(create_ball(i+1, width, height, speed))

# Box
wallleft = pygame.Surface((20, height))
wallleft.fill((255, 255, 255))
wallright = pygame.Surface((20, height))
wallright.fill((255, 255, 255))
wallbottom = pygame.Surface((width, 20))
wallbottom.fill((255, 255, 255))

wallleftrect = wallleft.get_rect(topleft=(0, 0))
wallrightrect = wallright.get_rect(topright=(width, 0))
wallbottomrect = wallbottom.get_rect(bottomleft=(0, height))

walls = [wallleftrect, wallrightrect, wallbottomrect]


# Main loop
while True:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Checks whether ball should be accelerated then accelerates ball

    # Fills the screen with black
    screen.fill(black)
    # Draws the ball and walls

    screen.blit(wallleft, wallleftrect)
    screen.blit(wallright, wallrightrect)
    screen.blit(wallbottom, wallbottomrect)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Moves the balls to next positions and renders them
    for ball in balls:
        colour = ball["ball_constants"]["colour"]
        radius = ball["ball_constants"]["radius"]

        # Moves the ball
        ball["ballrect"] = ball["ballrect"].move(ball["speed"])
        if ball["ballrect"].left < 0 or ball["ballrect"].right > width:
            ball["speed"][0] = -ball["speed"][0]
        if ball["ballrect"].top < 0 or ball["ballrect"].bottom > height:
            ball["speed"][1] = -ball["speed"][1]

        # Accelerates ball
        if not ballmotion.close_to_bottom(ball["ballrect"], wallbottomrect.top):
            ball["speed"] = ballmotion.calc_speed(ball["speed"], gravity, fps)

        pygame.draw.circle(
            screen, colour, ball["ballrect"].center, radius)

    # Updates the screen
    pygame.display.flip()
    # Waits for next frame
    clock.tick(fps)
