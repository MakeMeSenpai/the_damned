# Components/Enemies/peasant.py
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
        pygame.image.load(os.path.join("Assets/Enemies/peasant", "walking_" + add_str + ".PNG")).convert_alpha(),
        (100, 100))) # for an image name like Assests/Enemies/name.animation-name_03.PNG

class Peasant(Enemy):
    """Farmers, Townsmen, and pitchfork owners who want to get rid
    of the monster!""" 
    def __init__(self):
        super().__init__()
        self.name = "peasant"
        self.points = 50
        self.imgs = imgs[:]
        self.max_health = 15
        self.health = self.max_health
