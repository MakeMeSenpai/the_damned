"""Concept range tower - observatory? crystal ball? fortune teller?"""
# import pygame
# import os
# import math
# import time
# from ..tower import Tower
# # from menu.menu import Menu

# # menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")).convert_alpha(), (120, 70))
# # upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")).convert_alpha(), (50, 50))


# tower_imgs = []
# shooter_imgs = []
# # load tower images
# for x in range(1):
#     tower_imgs.append(pygame.transform.scale(
#         pygame.image.load(os.path.join("Assets/Towers/Support/range/tower_0" + str(x) + ".png")).convert_alpha(),
#         (90, 90)))

# # load shooter images
# for x in range(1):
#     shooter_imgs.append(
#         pygame.image.load(os.path.join("Assets/Towers/Support/range/shooter_0 + str(x) + ".png")).convert_alpha())

# class Range(Tower):
#     """Collects materials for the cuase! (give players extra points)
#     lvl1:famers lvl2:miners lvl3:mana collectors """
#     def __init__(self, x, y):
#         super().__init__(x,y)
#         self.range = 75
#         self.effect = [0.2, 0.4]
#         self.tower_imgs = tower_imgs[:]
#         self.shooter_imgs = shooter_imgs[:]
#         self.width = self.height = 90
#         self.name = "range"
#         self.price = [2000]

#     def draw(self, win):
#         super().draw_radius(win)
#         super().draw(win)

#     def support(self, towers):
#         """
#         will modify towers according to abillity
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
#             tower.range = tower.original_range + round(tower.range * self.effect[self.level -1])