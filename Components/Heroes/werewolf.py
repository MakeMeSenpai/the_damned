# Components/Heroes/werewolf.py
import pygame
import os
from .heroes import Heroes

# sets our animated sprites
imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Heroes/werewolf", "walking_" + add_str + ".png")).convert_alpha(),
        (100, 100))) # for an image name like Assests/Heroes/name.animation-name_03.png

class Werewolf(Heroes):
    """You just wanted to be like everybody else. But time and time again they take.
    May vengence be yours. Special: summons Werewolf pack to fight at your aid"""
    def __init__(self):
        super().__init__()
        self.name = "werewolf"
        self.imgs = imgs[:]
        self.max_stamina = 500
        self.stamina = self.max_health
        self.special = "Beastly Howl"