def close_to_bottom(ball, boundary):
    # Calculates distance between ball and wall
    difference = boundary - ball.bottom
    print(difference, boundary)

    # Checks if difference is small and returns boolean
    return difference <= 1

def calc_speed(speed, acceleration, fps):
    # Calculates change in speed per frame then accelerates ball
    change = acceleration / fps
    new_speed = speed[1] + change

    # Returns speed with acceleration applied
    return [speed[0], new_speed]