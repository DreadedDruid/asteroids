import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
 
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroid_group, update_group, draw_group)
    AsteroidField.containers = (update_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for obj in update_group:
            obj.update(dt)
        
        for obj in draw_group:
            obj.draw(screen)

        pygame.display.flip()

        dt = (game_clock.tick(60) / 1000)

if __name__ == "__main__":
    main()