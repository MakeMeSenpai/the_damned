# Componenets/Enemies/muraunder.py
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
        pygame.image.load(os.path.join("Assets/Enemies/muraunder", "walking_" + add_str + ".png")).convert_alpha(),
        (100, 100))) # for an image name like Assests/Enemies/name.animation-name_03.png

class Murauder(Enemy):
    """Nasty little buggers who destroy everything in
    their path! They also attack towers if in short range"""
    def __init__(self):
        super().__init__()
        self.name = "muraunder"
        self.points = 250
        self.imgs = imgs[:]
        self.max_health = 250
        self.health = self.max_health