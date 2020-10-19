# Components/Heroes/vampire.py
import pygame
import os
from .hero import Hero

# sets our animated sprites
imgs = []
for x in range(1): # number of sprites for animation
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Heroes/vampire", "walking_" + add_str + ".PNG")).convert_alpha(),
        (70, 70))) # for an image name like Assests/Heroes/name.animation-name_03.PNG

class Vampire(Hero):
    """The daywalkers are nothing but insolent cattle, and now you must
    put them in their place. Special: takes away health and gives you half back"""
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = "vampire"
        self.imgs = imgs[:]
        self.max_stamina = 150
        self.stamina = self.max_stamina
        self.special = "Life Drain"
        self.activate_special = 500 #level up stuff should make this more expensive
