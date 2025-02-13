import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()           

    def _check_events(self):
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                   self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                        
    def _check_keydown_events(self,event):
          if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
          elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
          elif event.key == pygame.K_q:
               sys.exit()
          elif event.key == pygame.K_SPACE:
               self._fire_bullet()
      
    def _check_keyup_events(self,event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                        
    def _fire_bullet(self):
         if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  

    def _update_bullets(self):
          self.bullets.update()
          for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)  
          collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) 
          if not self.aliens:
               self.bullets.empty()
               self._create_fleet()           
                 
    def _update_aliens(self):
         self._check_fleet_edges()
         self.aliens.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.bltime()
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    
    def _create_fleet(self):
         alien = Alien(self)
         alien_width, alien_height = alien.rect.width, alien.rect.height
         current_x, current_y = alien_width, alien_height
         while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width ):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            current_x = alien_width
            current_y += 2 * alien_height 

    def _create_alien(self, x_position, y_position):
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _check_fleet_edges(self):
         for alien in self.aliens.sprites():
              if alien._check_edges():
                   self._change_fleet_direction()
                   break
         
    def _change_fleet_direction(self):
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1      
        

if __name__ == '__main__':
    ai= AlienInvasion()
    ai.run_game()