import pygame, sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    fps = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    plyr = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asts = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with(plyr):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if obj.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    obj.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        #print(f"Delta Time: {dt}")


if __name__ == "__main__":
    main()
