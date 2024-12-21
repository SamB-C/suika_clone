from ball_functions import get_distance_between_ball_centers
from dict_types import BallRectType


def balls_colliding(ball1: BallRectType, ball2: BallRectType) -> bool:
    distance = get_distance_between_ball_centers(ball1, ball2)
    sum_of_radii = ball1["ball_constants"]["radius"] + \
        ball2["ball_constants"]["radius"]
    return distance <= sum_of_radii
