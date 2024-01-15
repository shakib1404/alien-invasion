import sys
import pygame

class AlienInvasion:
    """docstring for AlienInvasion"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        #set the background color
        self.bg_color=(230,230,230)

    def run_game(self):
        # start the main loop for the game
        while True:
            # watch the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)        
            # make recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
