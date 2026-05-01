import pygame
import tiles
import Player
import Creatures

class Item():
    def __init__(self, n, d, q):
        self.name = n
        self.description = d
        self.quantity = q
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    creatures = Creatures.initialiseCreatures()
    player = Player.Player(0, 0,"player", creatures, SCREEN_WIDTH, SCREEN_HEIGHT)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player.move(0,1)
                elif event.key == pygame.K_w:
                    player.move(0,-1)
                elif event.key == pygame.K_a:
                    player.move(-1,0)
                elif event.key == pygame.K_d:
                    player.move(1,0)
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                    player.move(0,0)
        screen.fill("purple")
        player.update()
        screen.blit(player.getSurface(), player.getRect())
        pygame.display.flip()
        clock.tick(60) 
if __name__ == "__main__":
    main()
pygame.quit()


