import pygame


class Ship:
    """ A class to manage the ship."""

    def __init__(self, ai_game):
        """ Initialize the ship"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image an get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship image and get its rect.
        self.rect.midbottom = self.screen_rect.midbottom


        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the ship's position based on the movement flag. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0: # TADA limit ship movement < top screen
            self.y -= self.settings.ship_speed
            
        
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """ Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

        
