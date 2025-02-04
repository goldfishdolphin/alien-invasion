import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()


            pygame.display.flip()

if __name__ == '__main__':
    ai= AlienInvasion()
    ai.run_game()