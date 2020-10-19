# Components/Towers/Base/base.py
import pygame
import os
import math
import time
from ..tower import Tower
# from menu.menu import Menu

# menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.PNG")).convert_alpha(), (120, 70))
# upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.PNG")).convert_alpha(), (50, 50))


tower_imgs = []
# base does not have shooter imgs but can in future dev
# shooter_imgs = [] 

# load tower images
for x in range(1):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Towers/Base/tower_0" + str(x) + ".PNG")).convert_alpha(),
        (120, 120)))

# load shooter images
# for x in range(1):
#     shooter_imgs.append(
#         pygame.image.load(os.path.join("Assets/Towers/Support/harvester/shooter_0" + str(x) + ".png")).convert_alpha())

class Base(Tower):
    """Collects materials for the cuase! (give players extra points)
    lvl1:famers lvl2:miners lvl3:mana collectors """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 0
        self.effect = [0.2, 0.4]
        self.tower_imgs = tower_imgs[:]
        # self.shooter_imgs = shooter_imgs[:]
        self.width = self.height = 90
        self.name = "base"
        self.max_health = 150
        self.health = self.max_health

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    """For now whenever anything collides with base, you lose health"""
    def collision(self, X, Y):
        """ Returns if enemies collides with an object
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    """figure out how getting hit will work later for all other towers"""
    # def hit(self, damage):
    #     """
    #     Returns if the hero has no more energy and removes stamina
    #     each call
    #     :return: Bool
    #     """
    #     self.health -= damage
    #     if self.health <= 0:
    #         return True
    #     return False
