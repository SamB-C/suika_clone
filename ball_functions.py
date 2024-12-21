from constants import BALLS, WALL_WIDTH
from pygame import Rect
from random import randint


def coordinates_of_ball_in_center_of_screen(screen_width, screen_height, ball_radius):
    '''Returns the x and y coordinates of a ball in the center of the screen'''
    return screen_width // 2 - ball_radius, screen_height // 2 - ball_radius


def get_random_top_position(screen_width, screen_height, ball_radius):
    '''Returns the x and y coordinates of a ball at the top of the screen'''
    margin = ball_radius + WALL_WIDTH + 5
    x = margin + randint(0, screen_width - (2 * (margin)))
    return x, 0


def get_random_speed():
    '''Returns a random speed for the ball'''
    return [randint(-5, 5), randint(0, 5)]


def create_ball(ball_number, x, y, initial_speed):
    '''Creates a ball (using data from the given ball number) and returns a dictionary containing the ball's constants, the ball's rectangle and the ball's speed'''
    ball = BALLS[ball_number - 1]
    ballrect = Rect(x, y, ball["radius"] * 2, ball["radius"] * 2)
    return {"ball_constants": ball, "ballrect": ballrect, "speed": initial_speed}
