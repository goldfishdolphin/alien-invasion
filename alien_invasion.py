import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (0, 50, 98)
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()


            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai= AlienInvasion()
    ai.run_game()