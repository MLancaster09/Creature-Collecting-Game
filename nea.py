import pygame
import tiles
import player
import Creatures

class Item():
    def __init__(self, n, d, q):
        self.name = n
        self.description = d
        self.quantity = q
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name, creatures):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load("girlFront.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.journal = {}
        for c in creatures:
            self.journal[c]=False
    def updateJournal(self, creature):
        self.journal[creature]=True
    def getSurface(self):
        return self.image
    def getRect(self):
        return self.rect
    def move(self, x, y):
        pass
    
class Map():
    pass

def main():

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    creatures = Creatures.initialiseCreatures()
    player = Player(0, 0,"player", creatures)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_w:
                    pass
                elif event.key == pygame.K_a:
                    pass
                elif event.key == pygame.K_d:
                    pass
            elif event.type == pygame.KEYUP:
                pass
        screen.fill("purple")
        screen.blit(player.getSurface(), player.getRect())
        pygame.display.flip()
        clock.tick(60) 
if __name__ == "__main__":
    main()
pygame.quit()


