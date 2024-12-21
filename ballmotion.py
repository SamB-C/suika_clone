def close_to_floor(ball, boundary):
    '''Returns whether or not a ball is close to the bottom of the screen'''
    # Calculates distance between ball and wall
    difference = boundary - ball.bottom

    # Checks if difference is small and returns boolean
    return difference <= 1


def calc_speed(speed, acceleration, fps, walls, ballrect):
    '''Calculates the ball's new speed and returns it'''
    # Calculates change in speed per frame then accelerates ball
    change = acceleration / fps
    new_speed = speed[1] + change

    return [speed[0], new_speed]


def calc_friction(speed):
    speed[0] *=  0.95
    return speed


def on_floor(ball, boundary):
    return ball == boundary
