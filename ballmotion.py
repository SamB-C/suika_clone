def calc_speed(speed, acceleration, fps):
    new_speed = speed[0]

    # Calculates change in speed per frame
    change = acceleration / fps

    # Ensures ball won't fall through speed
    if abs(new_speed) > change:
        new_speed = speed[1] + change

    # Returns speed with acceleration applied
    return [speed[0], new_speed]