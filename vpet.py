
"""Criando uma classe onde possa receber um nome da escolha do usuário"""
from logging import warning
import random

class Virtual_Pet:
    
    __life = True
    __age = 'baby'
    __type =['aqua','ground','fly']
    __skill={'physical': 0, 'intelligent': 0, 'social':0}
    __attribute=[]
    __level=0
    __feed = random.randint(1,99)
    __happiness = random.randint(1,99)
    __stamina = random.randint(1,99)
    __health = int((__feed + __happiness + __stamina)/3)
        
    def __init__(self,name=input('Name of the pet:')):
        self.name = name
        self.life = Virtual_Pet.__life
        self.age = Virtual_Pet.__age
        self.type = Virtual_Pet.__type
        self.skill = Virtual_Pet.__skill
        self.feed = Virtual_Pet.__feed
        self.happiness = Virtual_Pet.__happiness
        self.stamina = Virtual_Pet.__stamina
        self.level = Virtual_Pet.__level
        self.health = Virtual_Pet.__health
        print(f'The {name.title()} just born! He/she is level {self.level}, is a {self.age} and their health is at {self.health} percent.')

    def give_food(self):
        while self.feed < 100:
            print('I need to eat something!')
            self.feed + 10
            self.stamina + 5

    def wake_up(self):
        while self.stamina < 50:
            print('I am tired!')
            self.stamina +=10
        
    def play_strong(self):
        while self.happiness <= 75:
            self.happiness += 25
            self.skill['physical'] =+ 1

    def play_intelligent(self):
        while self.happiness <= 75:
            self.happiness += 25
            self.skill['intelligent'] =+ 1
    
    def play_social(self):
        while self.happiness <= 75:
            self.happiness += 25
            self.skill['social'] =+ 1

    def level_increment(self):
        if self.health == 100:
            return self.level + 1
        elif self.health <=99 or self.health >=50:
            return self.level + 0.5
        else:
            return 

    def growth(self):
        if self.level <= 5:
            self.age = 'baby'
        elif self.level == 10:
            self.age = 'kid'
        elif self.level == 20:
            self.age == 'teen'
        elif self.level == 35:
            self.age == 'adult'
        elif self.level == 60:
            self.age =='elder'
        elif self.level <= 100 and self.health <= 90:
            self.age == 'fabulous'
        elif self.level >= 150 and self.health == 100:
            self.age == 'mythical'
        else:
            return

    def have_type(self):
        if self.level == 5:
            print(f"You obtained a {random(Virtual_Pet.__type)} type for your buddy now!!")
            return self.type
    
    def new_skill(self):
        if self.skill['social'] > 30:
            self.attribute = 'Stealth!'
        elif self.skill['physical'] > 30:
            self.attribute = 'Strong!'
        elif self.skill['intelligent']>30:
            self.attribute = 'Smart!'  
        else:
            return

    def death_alert(self):
        if self.health < 15:
            warning ('You must do something right now!!!')
        elif self.health == 0:
            self.life = False
            print(f'So sorry! But {self.name} has died!')
        else:
            return

    def clock_tick(self):
        self.feed =-1
        self.happiness =-1
        self.stamina =-1

Virtual_Pet()