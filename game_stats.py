class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_status()
        self.game_active = False
        self.score = 0
        self.high_score = 0

    def reset_status(self):
        self.ships_left = self.settings.ship_limit
