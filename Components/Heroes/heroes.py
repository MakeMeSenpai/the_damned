# Components/Heroes/heroes.py
import pygame

class Heroes:
    imgs = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.stamina = 5
        self.path = []

    def draw(self, win):
        """ Draws our heroes using assets
        :param win: surface
        :return None"""
        # # Right now we don't have assets, but this will be implimented
        # # in future development
        # self.animation_count += 1
        # self.image = self.imgs[self.animation_count]
        # win.blit(self.image, (self.x, self.y))
        # # resets our animation
        # if self.animation_count >= len(self.imgs) - 1:
        #     self.animation_count = 0
        # moves our badies!
        self.move()

    def collision(self, X, Y):
        """ Returns if heroes collides with an object
        :param X: int
        :param Y: int
        :return None"""
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self):
        """ Moves our heroes
        :return: None """
        pass

    def hit(self, damage):
        """ Enemies loses stamina and returns if hero needs a break
        :param damage: int
        :return: Bool"""
        self.stamina -= damage
        if self.stamina <= 0:
            return True