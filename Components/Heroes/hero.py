# Components/Heroes/heroes.py
import pygame
import math
import os

class Hero:
    imgs = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.stamina = 5
        #TODO: concept path for demo-level, needs to have wider width for players to move on
        self.path = [(14, 124), (943, 193), (951, 387), (833, 448), (691, 451), (239, 484), (156, 499), (135, 540), (149, 758), (214, 807), (736, 806), (784, 761), (803, 683), (838, 636)]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False
        self.max_stamina = 0
        self.special = ""
        # ability_points = 0
        # activate_special = a certain number of ability_points

    def draw(self, win):
        """ Draws our enemies using assets
        :param win: surface
        :return None"""
        self.img = self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))

    def collision(self, X, Y):
        """ Returns if enemies collides with an object
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self):
        """
        Move hero using key inputs (wasd, or arrow keys, and spacebar to attack)
        :return: None
        """
        pass

    def hit(self, damage):
        """
        Returns if an enemy has died and removes one health
        each call
        :return: Bool
        """
        self.stamina -= damage
        if self.stamina <= 0:
            return True
        return False

        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False
        self.max_stamina = 0