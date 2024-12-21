from typing import List
from dict_types import BallType

WALL_WIDTH = 20


DARK_RED1: BallType = {
    "id": 1,
    "colour": (139, 0, 0),
    "radius": 10,
    "score": 2
}
LIGHT_RED2: BallType = {
    "id": 2,
    "colour": (255, 102, 102),
    "radius": 20,
    "score": 4
}
PURPLE3: BallType = {
    "id": 3,
    "colour": (128, 0, 128),
    "radius": 30,
    "score": 6
}
ORANGE4: BallType = {
    "id": 4,
    "colour": (255, 165, 0),
    "radius": 40,
    "score": 8
}
DARK_ORANGE5: BallType = {
    "id": 5,
    "colour": (255, 140, 0),
    "radius": 50,
    "score": 10
}
LIGHT_RED6: BallType = {
    "id": 6,
    "colour": (255, 102, 102),
    "radius": 60,
    "score": 12
}
MOUDLY_YELLOW7: BallType = {
    "id": 7,
    "colour": (204, 204, 0),
    "radius": 70,
    "score": 14
}
PINK8: BallType = {
    "id": 8,
    "colour": (255, 102, 102),
    "radius": 80,
    "score": 16
}
LEMON_YELLOW9: BallType = {
    "id": 9,
    "colour": (255, 255, 224),
    "radius": 90,
    "score": 18
}
LIME_GREEN10: BallType = {
    "id": 10,
    "colour": (50, 205, 50),
    "radius": 100,
    "score": 20
}
DARK_GREEN11: BallType = {
    "id": 11,
    "colour": (0, 100, 0),
    "radius": 110,
    "score": 22
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
