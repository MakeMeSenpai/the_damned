# main.py
import pygame
import sys
import math
import os
import time
import random
#imports our files

class Game:
    def __init__(self):
        self.width = 1250
        self.height = 845
        self.win = pygame.display.set_mode((self.width, self.height))
        self.level = ["Demo-Level"] #, "Level 1", "Level 2"...]
        self.heroes = ["Demon"] #, "Wearwolf", "Vampire"]
        self.enemies = ["Knight"] # Other human enemies
        self.health = 150
        self.points = 150
        # TODO: background image does not show up!
        self.bg = pygame.image.load("demo-level.png") # "./Assests/Backgrounds/demo-level.png") # os.path.join("Assets/Backgrounds", "demo-level.png")) #.convert()
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
                # used for path_creator()
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
                # Concept functions - impliments later
                # self.path_creator(event)
                # self.level_selector()
            self.draw()
        pygame.quit()
    
    def draw(self):
        """ Creates our background
        :returns: None"""
        # TODO: Nothing seems to be drawing
        self.win.blit(self.bg, (0, 0))
        # used for path_creator()
        # if self.path_creator() == True:
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

    def level_selector(self):
        """ Sets path and background based on previously created
        levels!
        <concept>
        :param level: int
        :return: None"""
        # demo-level: 
        #   bg: demo-level.png 
        #   clicks: []
        pass


new_game = Game()
new_game.run()