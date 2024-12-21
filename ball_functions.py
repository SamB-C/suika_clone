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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    return {"id": ball_id, "ball_constants": ball, "ballrect": ballrect, "speed": initial_speed}
=======
    return {"ball_constants": ball, "ballrect": ballrect, "speed": initial_speed, "pass_count": 0}
>>>>>>> Stashed changes
=======
    return {"ball_constants": ball, "ballrect": ballrect, "speed": initial_speed, "pass_count": 0}
>>>>>>> Stashed changes


def get_random_ball() -> int:
    '''Returns a random ball number'''
    n = randint(0, 100)
    if n < 50:
        return 0
    elif n < 75:
        return 1
    elif n < 87:
        return 2
    elif n < 94:
        return 3
    elif n < 98:
        return 4
    else:
        return 5
