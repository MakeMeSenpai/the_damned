# Components/Enemies/archer.py
import pygame
import os
from .enemy import Enemy

# sets our animated sprites
imgs = []
for x in range(1): # number of sprites for animation
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Enemies/archer", "walking_" + add_str + ".PNG")).convert_alpha(),
        (100, 100))) # for an image name like Assests/Enemies/name.animation-name_03.PNG

class Archer(Enemy):
    """Steady Aimers, who shoot anything in their range! Including
    Towers!"""
    def __init__(self):
        super().__init__()
        self.name = "archer"
        self.points = 50
        self.imgs = imgs[:]
        self.max_health = 100
        self.health = self.max_health
        