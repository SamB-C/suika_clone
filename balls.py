from typing import List
from dict_types import BallType
from pygame import Rect


DARK_RED1: BallType = {
    "colour": (139, 0, 0),
    "radius": 10
}
LIGHT_RED2: BallType = {
    "colour": (255, 102, 102),
    "radius": 20
}
PURPLE3: BallType = {
    "colour": (128, 0, 128),
    "radius": 30
}
ORANGE4: BallType = {
    "colour": (255, 165, 0),
    "radius": 40
}
DARK_ORANGE5: BallType = {
    "colour": (255, 140, 0),
    "radius": 50
}
LIGHT_RED6: BallType = {
    "colour": (255, 102, 102),
    "radius": 60
}
MOUDLY_YELLOW7: BallType = {
    "colour": (204, 204, 0),
    "radius": 70
}
PINK8: BallType = {
    "colour": (255, 102, 102),
    "radius": 80
}
LEMON_YELLOW9: BallType = {
    "colour": (255, 255, 224),
    "radius": 90
}
LIME_GREEN10: BallType = {
    "colour": (50, 205, 50),
    "radius": 100
}
DARK_GREEN11: BallType = {
    "colour": (0, 100, 0),
    "radius": 110
}


BALLS: List[BallType] = [
    DARK_RED1,
    LIGHT_RED2,
    PURPLE3,
    ORANGE4,
    DARK_ORANGE5,
    LIGHT_RED6,
    MOUDLY_YELLOW7,
    PINK8,
    LEMON_YELLOW9,
    LIME_GREEN10,
    DARK_GREEN11
]


def create_ball(ball_number, screen_width, screen_height, initial_speed):
    ball = BALLS[ball_number - 1]
    ballrect = Rect(screen_width // 2 - ball["radius"], screen_height //
                    2 - ball["radius"], ball["radius"] * 2, ball["radius"] * 2)
    return {"ball_constants": ball, "ballrect": ballrect, "speed": initial_speed}
