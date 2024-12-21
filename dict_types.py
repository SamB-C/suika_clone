from typing import TypedDict
from pygame import Rect


class BallType(TypedDict):
    id: int
    colour: tuple
    radius: int
    score: int


class BallRectType(TypedDict):
    id: int
    ball_constants: BallType
    ballrect: Rect
    speed: list
    pass_count: int
