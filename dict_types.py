from typing import TypedDict
from pygame import Rect


class BallType(TypedDict):
    colour: tuple
    radius: int


class BallRectType(TypedDict):
    id: int
    ball_constants: BallType
    ballrect: Rect
    speed: list
