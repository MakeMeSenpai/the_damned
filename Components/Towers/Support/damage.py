"""Concept damage tower - Weaponizer?"""
# import pygame
# import os
# import math
# import time
# from .tower import Towers

# imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "8.png")).convert_alpha(), (90,90)),
#               pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "9.png")).convert_alpha(), (90,90))]

# class DamageTower(RangeTower):
#     """
#     add damage to surrounding towers
#     """
#     def __init__(self, x, y):
#         super().__init__(x,y)
#         self.range = 100
#         self.tower_imgs = damage_imgs[:]
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