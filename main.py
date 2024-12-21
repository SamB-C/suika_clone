import sys
import pygame
from constants import BALLS, WALL_WIDTH
from typing import List
from dict_types import BallRectType
from ball_functions import create_ball, coordinates_of_ball_in_center_of_screen, get_random_top_position, get_random_speed

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
for i in range(20):
    # Get coordinates of where to place top left corner of ball
    x, y = get_random_top_position(
        width, height, BALLS[0]["radius"])
    speed = get_random_speed()
    # Create ball and add to the list of balls
    balls.append(create_ball(1, x, y, speed))

# Box
wallleft = pygame.Surface((WALL_WIDTH, height))
wallleft.fill((255, 255, 255))
wallright = pygame.Surface((WALL_WIDTH, height))
wallright.fill((255, 255, 255))
wallbottom = pygame.Surface((width, WALL_WIDTH))
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

        # Checks collisions
        ball["ballrect"] = ball["ballrect"].move(ball["speed"])
        if ball["ballrect"].left < wallleftrect.right or ball["ballrect"].right > wallrightrect.left:
            ball["speed"][0] = -ball["speed"][0]
        if ball["ballrect"].top < 0 or ball["ballrect"].bottom > wallbottomrect.top:
            ball["speed"][1] = -0.8 * ball["speed"][1]

        # Snaps after collision
        if ball["ballrect"].left < wallleftrect.right:
            ball["ballrect"].left = wallleftrect.right
        if ball["ballrect"].right > wallrightrect.left:
            ball["ballrect"].right = wallrightrect.left
        if ball["ballrect"].bottom > wallbottomrect.top:
            ball["ballrect"].bottom = wallbottomrect.top

        # Checks whether ball should be accelerated then accelerates ball
        if not close_to_floor(ball["ballrect"], wallbottomrect.top):
            ball["speed"] = calc_speed(
                ball["speed"], gravity, fps, walls, ball["ballrect"])

        pygame.draw.circle(
            screen, colour, ball["ballrect"].center, radius)

    # Updates the screen
    pygame.display.flip()
    # Waits for next frame
    clock.tick(fps)
