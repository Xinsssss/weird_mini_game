import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000
FARMER_SIZE = 16
FARMER_SPEED = 5
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Farmer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite_sheet = pygame.image.load('pics/P1.png')
        
        # Assuming your sprite frames are 16x16 as before
        self.walk_frames = [
            self.get_image(0, 0, 32, 32),
            self.get_image(32, 0, 32, 32)
        ]
        
        self.current_frame = 0
        self.image = self.walk_frames[self.current_frame]
        self.walking = False

    def get_image(self, x, y, width, height):
        """Extract a specific image from a sprite sheet."""
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

    def move(self, keys_pressed):
        self.walking = False
        if keys_pressed[K_w] or keys_pressed[K_UP]:
            self.y -= FARMER_SPEED
            self.walking = True
        if keys_pressed[K_s] or keys_pressed[K_DOWN]:
            self.y += FARMER_SPEED
            self.walking = True
        if keys_pressed[K_a] or keys_pressed[K_LEFT]:
            self.x -= FARMER_SPEED
            self.walking = True
        if keys_pressed[K_d] or keys_pressed[K_RIGHT]:
            self.x += FARMER_SPEED
            self.walking = True

        if self.walking:
            self.current_frame = (self.current_frame + 1) % len(self.walk_frames)
            self.image = self.walk_frames[self.current_frame]

        # Keep the farmer within the screen
        self.x = max(0, min(SCREEN_WIDTH - FARMER_SIZE, self.x))
        self.y = max(0, min(SCREEN_HEIGHT - FARMER_SIZE, self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Farmer Defense")
    clock = pygame.time.Clock()

    # Initialize farmer in the middle of the screen
    farmer = Farmer(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        farmer.move(keys_pressed)

        # Draw everything
        screen.fill(WHITE)
        farmer.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
