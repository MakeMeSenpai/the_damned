# Components/Enemies/knight.py
import pygame
import os
from .enemies import Enemies

# sets our animated sprites
imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Enemies/knight", "walking_" + add_str + ".png")).convert_alpha(),
        (100, 100))) # for an image name like Assests/Enemies/name.animation-name_03.png

class Knight(Enemies):
    """Armored foes who seek to bring the head of the beast back to 
    the Princess."""
    def __init__(self):
        super().__init__()
        self.name = "knight"
        self.points = 100
        self.imgs = imgs[:]
        self.max_health = 100
        self.health = self.max_health