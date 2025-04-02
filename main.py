import pygame

from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock() 
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)





    # In your game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill((0, 0, 0))  # Fill the screen instance, not the class
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(SCREEN_FPS)/1000



        
if __name__ == "__main__":
    main()
