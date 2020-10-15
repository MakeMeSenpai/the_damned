# main.py
import pygame
import sys
import math
import os
import time
import random

class Game:
    def __init__(self):
        """ Setup out game vars
        width: int
        height: int
        win: window display
        heroes: []
        enemies: []
        health: int
        points: int"""
        self.width = 1250
        self.height = 845
        self.win = pygame.display.set_mode((self.width, self.height))
        self.level = ["Demo-Level"] #, "Level 1", "Level 2"...]
        self.heroes = ["Demon"] #, "Wearwolf", "Vampire"]
        self.enemies = ["Knight"] # Other human enemies
        self.health = 150
        self.points = 150

    def run(self):
        """Runs our PyGame Window
        run: Bool"""
        pygame.display.set_caption('The Damned')
        # attempts to show background -TypeError: invalid color argument
        # self.win.blit(pygame.image.load("./Assets/Backgrounds/The_Damned-demo_level.png"), (0, 0))
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quite()

new_game = Game()
new_game.run()