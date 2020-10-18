# game.py
import pygame
import sys
import math
import os
import time
import random
# imports Heroes
from Components.Heroes import hero
from Components.Heroes import angel
from Components.Heroes import demon
from Components.Heroes import werewolf
from Components.Heroes import vampire
# imports Enemies
from Components.Enemies import enemy
from Components.Enemies import peasant
from Components.Enemies import knight
from Components.Enemies import archer
from Components.Enemies import murauder
# imports Towers
from Components.Towers import tower
from Components.Towers.Shooters import pebble_shooter
from Components.Towers.Shooters import mage
from Components.Towers.Roadblocks import  blockade_burgade
from Components.Towers.Support import harvester
#from Components. import

class Game:
    def __init__(self, win):
        self.win = win
        # by default demo-level should be selected, we will impliment level selection later
        # self.level = ["lvl-1", "lvl 2", "lvl 3"...]
        # Demo-level will auto select. But players will be able to choose their hero in future development.
        self.heroes = ["demon", "angle", "werewolf", "vampire"]
        # everything will spawn in demo level, but enemies should spawn based on lvl
        self.enemies = ["peasant", "knight", "archer", "murauder"]
        self.health = 150
        self.points = 250
        # TODO: background image does not show up!
        self.bg = pygame.image.load(os.path.join("Assets/Backgrounds", "demo-level.png")) # "demo-level.png") # "./Assests/Backgrounds/demo-level.png") #.convert()
        self.clicks = [] #mouse positions

    def run(self):
        """Runs our PyGame Window
        run: Bool
        bg: background image
        :returns: None"""
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60) #FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                """ used for path_creator() """
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
                """ Concept functions - impliments later """
                # self.path_creator(event)
                # self.level_selector()
            self.draw()
        pygame.quit()
    
    def draw(self):
        """ Creates our background
        :returns: None"""
        # TODO: Nothing seems to be drawing
        self.win.fill((0, 255, 0))
        self.win.blit(self.bg, (0, 0)) # (self.width, self.height))
        """ used for path_creator() """
        for p in self.clicks:
            pygame.draw.circle(self.win, (155, 0, 155), (p[0], p[1]), 5, 0)
        pygame.display.update()
    
    def path_creator(self, event):
        """ Helps us create enemies paths by creating visual and 
        printed feedback, in console.
        event: pygame.event.get()
        :returns: Bool"""
        # checks if function is in use
        pass
        # if event != None:
        #     pos = pygame.mouse.get_pos()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         self.clicks.append(pos)
        #         print(self.clicks)
        #     return True
        # else:
        #     return False

    def level_selector(self, selected):
        """ Sets path and background based on previously created
        levels!
        <concept>
        :param level: int
        :return: None"""
        # demo-level: 
        #   bg: demo-level.png 
        #   clicks: []
        pass
