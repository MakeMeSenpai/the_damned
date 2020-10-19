# Components/Enemies/knight.py
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
        pygame.image.load(os.path.join("Assets/Enemies/knight", "walking_" + add_str + ".PNG")).convert_alpha(),
        (60, 60))) # for an image name like Assests/Enemies/name.animation-name_03.PNG

class Knight(Enemy):
    """Armored foes who seek to bring the head of the beast back to 
    the Princess."""
    def __init__(self):
        super().__init__()
        self.name = "knight"
        self.points = 100
        self.imgs = imgs[:]
        self.max_health = 100
        self.health = self.max_health
        