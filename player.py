import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name, creatures, SCREEN_WIDTH, SCREEN_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.changeX = 0
        self.changeY = 0
        self.image = pygame.image.load("girlFront.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.journal = {}
        for c in creatures:
            self.journal[c]=False
    def updateJournal(self, creature):
        self.journal[creature]=True
    def getSurface(self):
        return self.image
    def getRect(self):
        return self.rect
    def setXY(self, x, y):
        self.x = x
        self.y=y
        self.rect.x = x
        self.rect.y = y
    def move(self, x, y):
        moveSize = 5
        self.changeX = x*moveSize
        self.changeY = y*moveSize
    def update(self):
        if self.changeX+self.x>self.SCREEN_WIDTH-(self.rect.width) or self.changeX+self.x<0:
           self.changeX = 0
        if self.changeY+self.y<0 or self.changeY+self.y>self.SCREEN_HEIGHT-(self.rect.height):
           self.changeY = 0
        self.setXY(self.x+self.changeX, self.y+self.changeY)