# Components/Towers/Support/harvester.py
import pygame
import os
import math
import time
from ..tower import Tower
# from menu.menu import Menu

# menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.PNG")).convert_alpha(), (120, 70))
# upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.PNG")).convert_alpha(), (50, 50))


tower_imgs = []
# shooter_imgs = []

# load tower images
for x in range(1):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Towers/Support/harvester/tower_0" + str(x) + ".PNG")).convert_alpha(),
        (90, 90)))

# load shooter images
# for x in range(1):
#     shooter_imgs.append(
#         pygame.image.load(os.path.join("Assets/Towers/Support/harvester/shooter_0" + str(x) + ".png")).convert_alpha())

class Harvester(Tower):
    """Collects materials for the cuase! (give players extra points)
    lvl1:famers lvl2:miners lvl3:mana collectors """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 0
        self.effect = [0.2, 0.4]
        self.tower_imgs = tower_imgs[:]
        # self.shooter_imgs = shooter_imgs[:]
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
            # sleep is unusable in this setting
            # time.sleep(5) 
            points += 321
