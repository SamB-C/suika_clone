import sys
import pygame
from constants import BALLS, WALL_WIDTH
from typing import List
from dict_types import BallRectType
from ball_functions import get_random_ball, reduce_speed, create_ball, get_distance_between_ball_centers, get_speed_magnitude
from settings import fps
from collisions import balls_colliding, calculate_speed_after_collision, calculate_merge_speed, check_wall_collisions
from ui import ScoreBoard
from ballmotion import close_to_floor, calc_speed, calc_friction, on_floor
from random import randint
from high_score import load_high_score, update_high_score

pygame.init()

# Sets width and height of the screen
size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0

# Creates a screen
screen = pygame.display.set_mode(size)

# Creates game clock and sets target frames per second
clock = pygame.time.Clock()

# Defines acceleration due to gravity
gravity = 9.8

#  Creates the balls
balls: List[BallRectType] = []


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

# Fetches high score from file
high_score_value = load_high_score()

# Creates score boards
score_board = ScoreBoard()
high_score_board = ScoreBoard(text="High score", size=[
                              150, 30], score=high_score_value)


def add_ball():
    '''Adds a ball to the screen and increases the score'''
    mouse_x, _ = pygame.mouse.get_pos()
    x = mouse_x
    y = 0
    speed = [randint(-1, 1), 0]

    # Sets type of ball
    ball_num = get_random_ball()
    balls.append(create_ball(ball_num, x, y, speed))

    # Finds score associated with ball and adds to score
    score_to_add = BALLS[ball_num]["score"]
    score_board.add_to_score(score_to_add)


def event_handler():
    '''Handles events such as quitting the game and adding balls'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            add_ball()


def draw_background(wallleft, wallleftrect, wallright, wallrightrect, wallbottom, wallbottomrect):
    '''Fills in background as black and draws walls'''
    screen.fill(black)
    screen.blit(wallleft, wallleftrect)
    screen.blit(wallright, wallrightrect)
    screen.blit(wallbottom, wallbottomrect)

# Main loop


def main_loop():
    # Event Handler
    event_handler()

    draw_background(wallleft, wallleftrect, wallright,
                    wallrightrect, wallbottom, wallbottomrect)

    collisions = []

    # Moves the balls to next positions and renders them
    for ball in balls:
        colour = ball["ball_constants"]["colour"]
        radius = ball["ball_constants"]["radius"]

        # Move ball
        ball["ballrect"] = ball["ballrect"].move(ball["speed"])

        # Check for collisions with walls
        check_wall_collisions(ball, wallleftrect,
                              wallrightrect, wallbottomrect)

        # Ball collisions wuth other balls
        for index, other_ball in enumerate(balls):
            if other_ball != ball:
                if balls_colliding(ball, other_ball):
                    if ball["ball_constants"]["radius"] == other_ball["ball_constants"]["radius"] and not ball["ball_constants"]["radius"] == BALLS[-1]["radius"]:
                        balls.pop(index)
                        ball_id = ball["ball_constants"]["id"]
                        initial_radius = ball["ball_constants"]["radius"]
                        ball["ball_constants"] = BALLS[ball_id]
                        final_radius = ball["ball_constants"]["radius"]
                        size_increase = 2 * (final_radius - initial_radius)
                        ball["ballrect"] = ball["ballrect"].inflate(
                            size_increase, size_increase)
                        ball["speed"] = calculate_merge_speed(ball, other_ball)
                        score_board.add_to_score(BALLS[ball_id]["score"])
                    else:
                        if not [ball["id"], other_ball["id"]] in collisions:
                            collisions.append([ball["id"], other_ball["id"]])
                            ball["speed"], other_ball["speed"] = calculate_speed_after_collision(
                                ball, other_ball)
                            #  Reduce the speed of the balls after a collision
                            ball["speed"] = reduce_speed(ball["speed"])
                            other_ball["speed"] = reduce_speed(
                                other_ball["speed"])
                            # Get distance between ball centers
                            diff_centres = get_distance_between_ball_centers(
                                ball, other_ball)
                            # Get speed of other ball
                            other_ball_speed = get_speed_magnitude(
                                ball["speed"])
                            # If the balls are too close, move them apart
                            if other_ball_speed < 2 * diff_centres:
                                other_ball["ballrect"] = other_ball["ballrect"].move(
                                    other_ball["speed"][0] * 2, other_ball["speed"][1] * 2)

        # Checks whether ball should be accelerated then accelerates ball
        if not close_to_floor(ball["ballrect"], wallbottomrect.top):
            ball["speed"] = calc_speed(
                ball["speed"], gravity, fps, walls, ball["ballrect"])

        if on_floor(ball["ballrect"].bottom, wallbottomrect.top):
            ball["speed"] = calc_friction(ball["speed"])

        pygame.draw.circle(screen, colour, ball["ballrect"].center, radius)

    # Gets current score
    score = score_board.score

    # Checks for new high score
    if score > high_score_value:
        high_score_value = score
        update_high_score(score)
        high_score_board.set_score(score)

    # Updates score boards on screen
    screen.blit(high_score_board.board, (10, 10))
    screen.blit(score_board.board, (10, 50))

    # Updates the screen
    pygame.display.flip()
    # Waits for next frame
    clock.tick(fps)


while True:
    main_loop()
