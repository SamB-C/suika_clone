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
    '''Calculates the speed of the balls after a collision and adjusts their positions to prevent clipping'''
    # Get the centers of the balls
    ball1_center = ball1["ballrect"].center
    ball2_center = ball2["ballrect"].center

    # Calculate the distance between the centers
    distance = sqrt((ball2_center[0] - ball1_center[0]) ** 2 + (ball2_center[1] - ball1_center[1]) ** 2)

    # Avoid division by zero
    if distance == 0:
        return ball1["speed"], ball2["speed"]

    # Calculate the direction of the collision
    direction = [(ball2_center[0] - ball1_center[0]) / distance, (ball2_center[1] - ball1_center[1]) / distance]

    # Calculate the overlap
    overlap = ball1["ball_constants"]["radius"] + ball2["ball_constants"]["radius"] - distance

    # Adjust positions to prevent clipping
    ball1["ballrect"].x -= direction[0] * overlap / 2
    ball1["ballrect"].y -= direction[1] * overlap / 2
    ball2["ballrect"].x += direction[0] * overlap / 2
    ball2["ballrect"].y += direction[1] * overlap / 2

    # Calculate the new speeds
    speed1 = ball1["speed"]
    speed2 = ball2["speed"]

    new_speed1 = [speed1[0] - direction[0], speed1[1] - direction[1]]
    new_speed2 = [speed2[0] + direction[0], speed2[1] + direction[1]]

    return new_speed1, new_speed2


def calculate_merge_speed(ball1: BallRectType, ball2: BallRectType):
    ball1_speed = ball1["speed"]
    ball2_speed = ball2["speed"]

    ball1_mass = ball1["ball_constants"]["radius"]
    ball2_mass = ball2["ball_constants"]["radius"]

    ball1_momentum = [ball1_speed[0] * ball1_mass, ball1_speed[1] * ball1_mass]
    ball2_momentum = [ball2_speed[0] * ball2_mass, ball2_speed[1] * ball2_mass]

    total_momentum = [ball1_momentum[0] + ball2_momentum[0],
                      ball1_momentum[1] + ball2_momentum[1]]
    total_mass = ball1_mass + ball2_mass
    final_speed = [total_momentum[0] / total_mass,
                   total_momentum[1] / total_mass]

    return final_speed


def reduce_speed(speed: list[int]) -> list[int]:
    '''Reduces the speed of the ball by 1 in the x and y direction'''
    return [0.8 * speed[0], 0.8 * speed[1]]


def create_ball(ball_number, x, y, initial_speed):
    '''Creates a ball (using data from the given ball number) and returns a dictionary containing the ball's constants, the ball's rectangle and the ball's speed'''
    ball = BALLS[ball_number]
    ballrect = Rect(x, y, ball["radius"] * 2, ball["radius"] * 2)
    return {"ball_constants": ball, "ballrect": ballrect, "speed": initial_speed}
