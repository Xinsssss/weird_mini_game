import pygame
from game_settings import *
from pygame.locals import *

class Farmer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((FARMER_SIZE, FARMER_SIZE))
        self.sprite_sheet = pygame.image.load('pics/P1.png')
        
        # Assuming your sprite frames are 16x16 as before
        self.walk_frames = [
            self.get_image(0, 0, FARMER_SIZE, FARMER_SIZE),
            self.get_image(FARMER_SIZE, 0, FARMER_SIZE, FARMER_SIZE)
        ]

    def move(self, keys_pressed):
        if keys_pressed[K_w] or keys_pressed[K_UP]:
            self.y -= FARMER_SPEED
        if keys_pressed[K_s] or keys_pressed[K_DOWN]:
            self.y += FARMER_SPEED
        if keys_pressed[K_a] or keys_pressed[K_LEFT]:
            self.x -= FARMER_SPEED
        if keys_pressed[K_d] or keys_pressed[K_RIGHT]:
            self.x += FARMER_SPEED

        # Keep the farmer within the screen
        self.x = max(0, min(WIDTH - FARMER_SIZE, self.x))
        self.y = max(0, min(HEIGHT - FARMER_SIZE, self.y))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))