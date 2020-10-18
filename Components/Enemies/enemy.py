# Components/Enemies/enemies.py
import pygame
import math
import os

"""May have to change this into pathfinders for allies to also
take use of in the future. (remember to reverse path for allies)"""
class Enemy:
    def __init__(self):
        # if needed: add width/height params later
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        # concept path for demo-level
        self.path = [(0, 169), (999, 170), (999, 327), (871, 371), (699, 412), (220, 454), (149, 465), (101, 514), (96, 708), (124, 760), (189, 794), (722, 799), (778, 766), (808, 699), (816, 597)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False
        self.max_health = 0
        self.speed_increase = 1.2

    def draw(self, win):
        """ Draws our enemies using assets
        :param win: surface
        :return None"""
        self.img = self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))
        # maybe add boss health bar in future
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-30, self.y - 75, health_bar, 10), 0)  

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
        Move enemy
        :return: None
        """
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos+1]

        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)

        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y

        # Go to next point
        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else: # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1

    def hit(self, damage):
        """
        Returns if an enemy has died and removes health
        each call
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False
""" Used to delete item? """
# self.x = self.path[0][0]
# self.y = self.path[0][1]
# self.img = None
# self.dis = 0
# self.path_pos = 0
# self.move_count = 0
# self.move_dis = 0
# self.imgs = []
# self.flipped = False
# self.max_health = 0
 