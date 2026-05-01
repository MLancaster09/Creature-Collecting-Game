import pygame
import random
import json

class Item():
    def __init__(self, n, d, q):
        self.name = n
        self.description = d
        self.quantity = q
class Creature():
    def __init__(self, name,type, HP, attack, defence, speed, CATCH_RATE):
        self.name = name
        self. type = type
        self.HP = HP
        self. attack = attack
        self.defence = defence
        self.speed = speed
        self.CATCH_RATE = CATCH_RATE
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
    def initialiseCreatures():
        with open("creatures.json", "r") as file:
            data = json.load(file) #load the data stored in the json file as a dictionary of dictionaries
        creatures=[] #empty list as we are going to create a list of creatures using the data from file
        for name, stats in data.items(): #stats refers to the dictionary of stats. we are using each key to access the data
            creatures.append(Creature(name, stats["type"], stats["HP"], stats["attack"], stats["defence"], stats["speed"], stats["catch_rate"]))
        return creatures
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    creatures = initialiseCreatures()
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


