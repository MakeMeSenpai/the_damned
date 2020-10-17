# Components/Enemies/enemies.py
import pygame

"""May have to change this into pathfinders for allies to also
take use of in the future. (remember to reverse path for allies)"""
class Enemies:
    imgs = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 5
        self.img = None
        # concept path for demo-level
        self.path = [(14, 124), (943, 193), (951, 387), (833, 448), (691, 451), (239, 484), (156, 499), (135, 540), (149, 758), (214, 807), (736, 806), (784, 761), (803, 683), (838, 636)]
        self.path_pos = 0
        self.move_count = 0

    def draw(self, win):
        """ Draws our enemies using assets
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
        """ Returns if enemies collides with an object
        :param X: int
        :param Y: int
        :return None"""
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self):
        """ Moves enemies by path points, and postion
        :return: None """
        x1, y1 = self.path[self.path_pos]
        x2, y2 = self.path[self.path_pos + 1]
        
        self.move_count += 1
        dirn = (x2-x1, y2-y1)
        pos = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        pass

    def hit(self, damage):
        """ Enemies lose health and returns if enemy dies
        :param damage: int
        :return: Bool"""
        self.health -= damage
        if self.health <= 0:
            return True