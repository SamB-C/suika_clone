from ball_functions import get_distance_between_ball_centers
from dict_types import BallRectType
from math import sqrt
from pygame import Rect


def check_wall_collisions(ball: BallRectType, wallleftrect: Rect, wallrightrect: Rect, wallbottomrect: Rect):
    '''Checks for collisions between the ball and the walls'''
    if ball["ballrect"].left < wallleftrect.right:
        ball["ballrect"].left = wallleftrect.right
        ball["speed"][0] = -ball["speed"][0]
    if ball["ballrect"].right > wallrightrect.left:
        ball["ballrect"].right = wallrightrect.left
        ball["speed"][0] = -ball["speed"][0]
    if ball["ballrect"].bottom > wallbottomrect.top:
        ball["ballrect"].bottom = wallbottomrect.top
        ball["speed"][1] = -0.8 * ball["speed"][1]


def balls_colliding(ball1: BallRectType, ball2: BallRectType) -> bool:
    distance = get_distance_between_ball_centers(ball1, ball2)
    sum_of_radii = ball1["ball_constants"]["radius"] + \
        ball2["ball_constants"]["radius"]
    return distance <= sum_of_radii


def calculate_speed_after_collision(ball1: BallRectType, ball2: BallRectType):
    '''Calculates the speed of the balls after a collision and adjusts their positions to prevent clipping'''
    # Get the centers of the balls
    ball1_center = ball1["ballrect"].center
    ball2_center = ball2["ballrect"].center

    # Calculate the distance between the centers
    distance = sqrt((ball2_center[0] - ball1_center[0])
                    ** 2 + (ball2_center[1] - ball1_center[1]) ** 2)

    # Avoid division by zero
    if distance == 0:
        return ball1["speed"], ball2["speed"]

    # Calculate the direction of the collision
    direction = [(ball2_center[0] - ball1_center[0]) / distance,
                 (ball2_center[1] - ball1_center[1]) / distance]

    # Calculate the overlap
    overlap = ball1["ball_constants"]["radius"] + \
        ball2["ball_constants"]["radius"] - distance

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
