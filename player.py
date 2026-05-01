import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name, creatures):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load("girlFront.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
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
    