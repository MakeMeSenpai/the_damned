# Components/Towers/Support/harvester.py
import pygame
import os
import math
import time
from .tower import Towers

#TODO: SPRITES DON"T EXIST! this goes for many other files that need to be created
imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "4.png")).convert_alpha(), (90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "5.png")).convert_alpha(), (90, 90))]

class Harvester(Towers):
    """Collects materials for the cuase! (give players extra points)
    lvl1:famers lvl2:miners lvl3:mana collectors """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 0
        self.effect = [0.2, 0.4]
        self.tower_imgs = imgs[:]
        self.width = self.height = 90
        self.name = "harvester"
        self.price = [2000]

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    def support(self, points):
        """
        will give players more points
        :param points: int
        :return: None
        """
        while points != 99999:
            time.sleep(5)
            points += 321