import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    """docstring for AlienInvasion"""
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)

        self.bullet=pygame.sprite.Group()
        #set the background color
        self.bg_color=self.settings.bg_color

    def run_game(self):
        # start the main loop for the game
        while True:
            # watch the keyboard and mouse event
            self._check_events()
            self.ship.update()
            
            self._update_bullet()
            self._update_screen()
            
            
    def _check_events(self):
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type==pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
             #MOVE THE SHIP TO THE RIGHT
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
                        #MOVE THE SHIP TO THE RIGHT
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key ==pygame.K_SPACE:
            self.fire_bullet()      
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
             #MOVE THE SHIP TO THE RIGHT
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            #MOVE THE SHIP TO THE RIGHT
            self.ship.moving_left=False
        

    def fire_bullet(self):
        #create a new bullet and add it to bullets group
        if len(self.bullet)<self.settings.bullet_allowed:
           new_bullet=Bullet(self)
           self.bullet.add(new_bullet)

    def _update_bullet(self):
        self.bullet.update()
    
       # get rid of bullets that have disappeared
        for bulet in self.bullet.copy():
           if bulet.rect.bottom <= 0:
                self.bullet.remove(bulet)
                print(len(self.bullet))


    def _update_screen(self):
      #update images on screen and flip the new screen
      #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bulet in self.bullet.sprites():
                bulet.draw_bullet()

            # make recently drawn screen visible
            pygame.display.flip()
    


             

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
