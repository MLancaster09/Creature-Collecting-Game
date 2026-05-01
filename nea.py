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
class Player():
    def __init__(self, x, y, name, creatures):
        self.name = name
        self.x = x
        self.image = pygame.image.load("player.png")
        self.journal = {}
        for c in creatures:
            self.journal[c]=False
    def updateJournal(self, creature):
        self.journal[creature]=True
    def move(self, x, y):
        pass
    
class Map():
    pass

class main():
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
    player = Player("player")
    creatures = initialiseCreatures()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.Key == pygame.K_s:
                    pass
                elif event.Key == pygame.K_w:
                    pass
                elif event.Key == pygame.K_a:
                    pass
                elif event.Key == pygame.K_d:
                    pass
            elif event.type == pygame.KEYUP:
                pass
        

        screen.fill("purple")
        pygame.display.flip()
        clock.tick(60) 

pygame.quit()


