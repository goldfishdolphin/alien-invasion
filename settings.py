class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(0, 50, 98)
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3
        self.alien_speed =1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1