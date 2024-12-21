import pygame

# Initialises fonts in pygame
pygame.font.init()
game_font = pygame.font.SysFont('Comic Sans MS', 20)

class ScoreBoard:
    board: pygame.surface.Surface

    # Assigns class attributes
    def __init__(self, bg_colour=(255, 255, 255), txt_colour=(0, 0, 0), size=(120, 30), score=0, text="Score"):
        self.bg_colour = bg_colour
        self.txt_colour = txt_colour
        self.size = size
        self.score = score
        self.text = text

        self.create_board()

    # Creates pygame surface for score board
    def create_board(self):
        self.board = pygame.surface.Surface(size=self.size)
        self.board.fill(self.bg_colour)

        score_text = game_font.render(f"{self.text}: {self.score}", False, self.txt_colour)
        self.board.blit(score_text, (0, 0))

    # Changes score
    def set_score(self, new_score):
        self.score = new_score
        self.create_board()

    # Increments score
    def add_to_score(self, amount):
        self.score += amount
        self.create_board()
