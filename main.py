import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock() 
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    # In your game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen instance, not the class
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)

        ast_to_remove = []
        shot_to_remove = []
        for ast in asteroids:
            if player.is_colliding(ast):
                print("Game over!")
                return

            for shot in shots:
                if shot.is_colliding(ast):
                    ast_to_remove.append(ast)
                    shot_to_remove.append(shot)
        
        for obj in shot_to_remove:
            obj.kill()
        
        for obj in ast_to_remove:
            obj.split()

        pygame.display.flip()
        dt = clock.tick(SCREEN_FPS)/1000


        
if __name__ == "__main__":
    main()
