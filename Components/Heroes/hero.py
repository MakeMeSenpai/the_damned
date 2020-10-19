# Components/Heroes/heroes.py
import pygame
import random
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
        # special ability
        self.special = ""
        self.ability_points = 0
        self.activate_special = 0

    def draw(self, win):
        """ Draws our hero using assets
        :param win: surface
        :return None"""
        self.img = self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))

    def collision(self, X, Y):
        """ Returns if hero collides with an object
        :param x: int
        :param y: int
        :return: Bool
        """
        # note that a player can collide with many things
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self, x_change=0, y_change=0):
        """
        Move hero using key inputs (wasd, or arrow keys, and spacebar to attack)
        :return: None
        """
        # we moved functions into game.py becuase it's simpler
        # it needed .event, which is not availible in this file
        # but this should now update the heros position based on those movements
        speed = 5
        if x_change != 0 or y_change != 0:
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0
            # up 
            if y_change > 0:
                self.y += speed
            # down 
            if y_change < 0:
                self.y -= speed
            # left
            if x_change < 0:
                self.x -= speed
            # right 
            if x_change > 0:
                self.x += speed
                

    def hit(self, damage):
        """
        Returns if the hero has no more energy and removes stamina
        each call
        :return: Bool
        """
        self.stamina -= damage
        if self.stamina <= 0:
            return True
        return False
