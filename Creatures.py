import pygame
import json

class Creature():
    def __init__(self, name,type, HP, attack, defence, speed, CATCH_RATE):
        self.name = name
        self. type = type
        self.HP = HP
        self. attack = attack
        self.defence = defence
        self.speed = speed
        self.CATCH_RATE = CATCH_RATE

def initialiseCreatures():
        with open("creatures.json", "r") as file:
            data = json.load(file) #load the data stored in the json file as a dictionary of dictionaries
        creatures=[] #empty list as we are going to create a list of creatures using the data from file
        for name, stats in data.items(): #stats refers to the dictionary of stats. we are using each key to access the data
            creatures.append(Creature(name, stats["type"], stats["HP"], stats["attack"], stats["defence"], stats["speed"], stats["catch_rate"]))
        return creatures
