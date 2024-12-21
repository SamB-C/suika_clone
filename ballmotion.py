def close_to_floor(ball, boundary):
    # Calculates distance between ball and wall
    difference = boundary - ball.bottom

    # Checks if difference is small and returns boolean
    return difference <= 1

def calc_speed(speed, acceleration, fps, walls, ballrect):
    # Calculates change in speed per frame then accelerates ball
    change = acceleration / fps
    new_speed = speed[1] + change

    for wall in walls:
        if ballrect.colliderect(wall):
            if wall == walls[2]:
                pass
            else:
                speed[0] = -0.8 * speed[0]

    # Returns speed with acceleration applied
    return [speed[0], new_speed]