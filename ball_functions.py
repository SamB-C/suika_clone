from constants import BALLS, WALL_WIDTH
from pygame import Rect
from random import randint
from dict_types import BallRectType
from math import sqrt


def get_distance_between_ball_centers(ball1: BallRectType, ball2: BallRectType):
    ball1_center = ball1["ballrect"].center
    ball2_center = ball2["ballrect"].center
    return sqrt((ball1_center[0] - ball2_center[0]) **
                2 + (ball1_center[1] - ball2_center[1]) ** 2)


def get_speed_magnitude(speed):
    '''Returns the magnitude of the speed vector'''
    return sqrt(speed[0] ** 2 + speed[1] ** 2)


def get_random_speed():
    '''Returns a random speed for the ball'''
    return [randint(-5, 5), randint(0, 5)]


def calculate_speed_after_collision(ball1: BallRectType, ball2: BallRectType):
    '''Calculates the speed of the balls after a collision'''
    # Get the speed of the balls
    speed1 = ball1["speed"]
    speed2 = ball2["speed"]

    # Get the mass of the balls
    mass1 = ball1["ball_constants"]["radius"]
    mass2 = ball2["ball_constants"]["radius"]

    # Get the distance between the centers of the balls
    distance = get_distance_between_ball_centers(ball1, ball2)

    if distance == 0:
        return [-speed1[0], -speed1[1]], [-speed2[0], -speed2[1]]

    # Get the unit vector of the direction of the collision
    direction = [(ball2["ballrect"].center[0] - ball1["ballrect"].center[0]) /
                 distance, (ball2["ballrect"].center[1] - ball1["ballrect"].center[1]) / distance]

    # Get the speed of the balls in the direction of the collision
    speed1_in_direction = speed1[0] * direction[0] + speed1[1] * direction[1]
    speed2_in_direction = speed2[0] * direction[0] + speed2[1] * direction[1]

    # Calculate the new speed of the balls in the direction of the collision
    new_speed1_in_direction = (speed1_in_direction * (mass1 - mass2) +
                               2 * mass2 * speed2_in_direction) / (mass1 + mass2)
    new_speed2_in_direction = (speed2_in_direction * (mass2 - mass1) +
                               2 * mass1 * speed1_in_direction) / (mass1 + mass2)

    # Calculate the new speed of the balls
    new_speed1 = [speed1[0] - speed1_in_direction * direction[0] + new_speed1_in_direction * direction[0],
                  speed1[1] - speed1_in_direction * direction[1] + new_speed1_in_direction * direction[1]]
    new_speed2 = [speed2[0] - speed2_in_direction * direction[0] + new_speed2_in_direction * direction[0],
                  speed2[1] - speed2_in_direction * direction[1] + new_speed2_in_direction * direction[1]]

    return new_speed1, new_speed2


def reduce_speed(speed: list[int]) -> list[int]:
    '''Reduces the speed of the ball by 1 in the x and y direction'''
    return [0.8 * speed[0], 0.8 * speed[1]]


ball_id = 0


def create_ball(ball_number, x, y, initial_speed):
    '''Creates a ball (using data from the given ball number) and returns a dictionary containing the ball's constants, the ball's rectangle and the ball's speed'''
    global ball_id
    ball_id += 1
    ball = BALLS[ball_number]
    ballrect = Rect(x, y, ball["radius"] * 2, ball["radius"] * 2)
    return {"id": ball_id, "ball_constants": ball, "ballrect": ballrect, "speed": initial_speed}
