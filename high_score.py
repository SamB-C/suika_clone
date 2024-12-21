# Fetches high score from file
def load_high_score():
    with open("high_score.txt", "r") as file:
        score = file.read()
        score = int(score)
    return score

# Updates file with new high score
def update_high_score(score):
    score = str(score)
    with open("high_score.txt", "w") as file:
        file.write(score)

# Sets high score to zero
def reset_high_score():
    with open("high_score.txt", "w") as file:
        file.write("0")