import pygame


class Ship(object):
    """docstring for Ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('rocket3.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #store a decimal value for the ship's horizontal position
        self.x=float(self.rect.x)

        #movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #update the ship's position based on movement flad
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        #update rect object from self.x
        self.rect.x=self.x    



    def blitme(self):
        # Draw the ship at the current location
        self.screen.blit(self.image, self.rect)
