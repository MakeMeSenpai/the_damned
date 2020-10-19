# Components/Heroes/demon.py
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
        pygame.image.load(os.path.join("Assets/Heroes/demon", "walking_" + add_str + ".PNG")).convert_alpha(),
        (100, 100))) # for an image name like Assests/Heroes/name.animation-name_03.PNG

class Demon(Hero):
    """Your will is your own. They will feel your wrath as you
    take over the land. Special: Temporary Damage boost"""
    def __init__(self):
        super().__init__()
        self.name = "demon"
        self.imgs = imgs[:]
        self.max_stamina = 500
        self.stamina = self.max_stamina
        self.special = "Firey Wrath"
        self.activate_special = 500 #level up stuff should make this more expensive
