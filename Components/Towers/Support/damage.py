"""Concept damage tower - Weaponizer?"""
# import pygame
# import os
# import math
# import time
# from .range import Range
# # from menu.menu import Menu

# # menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.PNG")).convert_alpha(), (120, 70))
# # upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.PNG")).convert_alpha(), (50, 50))


# tower_imgs = []
# shooter_imgs = []
# # load tower images
# for x in range(1):
#     tower_imgs.append(pygame.transform.scale(
#         pygame.image.load(os.path.join("Assets/Towers/damage/tower_0" + str(x) + ".PNG")).convert_alpha(),
#         (90, 90)))

# # load shooter images
# for x in range(1):
#     shooter_imgs.append(
#         pygame.image.load(os.path.join("Assets/Towers/damage/shooter_0" + str(x) + ".PNG")).convert_alpha())

# class DamageTower(range):
#     """
#     add damage to surrounding towers
#     """
#     def __init__(self, x, y):
#         super().__init__(x,y)
#         self.range = 100
#         self.tower_imgs = tower_imgs[:]
#         self.shooter_imgs = shooter_imgs[:]
#         self.effect = [0.5, 1]
#         self.name = "damage"
#         self.price = [2000]

#     def support(self, towers):
#         """
#         will modify towers according to ability
#         :param towers: list
#         :return: None
#         """
#         effected = []
#         for tower in towers:
#             x = tower.x
#             y = tower.y

#             dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

#             if dis <= self.range + tower.width/2:
#                 effected.append(tower)

#         for tower in effected:
#             tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level -1])
