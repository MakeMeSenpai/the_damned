#Components/Towers/Shooters/pebble_shooter.py
import pygame
import os
import math
from ..tower import Tower
from ...Menues.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Icons", "temp_img.PNG")).convert_alpha(), (120, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Icons", "temp_img.PNG")).convert_alpha(), (50, 50))


tower_imgs = []
shooter_imgs = []

# load tower images
for x in range(1):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Towers/Shooters/pebble_shooter/tower_0" + str(x) + ".PNG")).convert_alpha(),
        (90, 90)))

# load shooter images
for x in range(1):
    shooter_imgs.append(
        pygame.transform.scale(pygame.image.load(os.path.join("Assets/Towers/Shooters/pebble_shooter/shooter_0" + str(x) + ".PNG")).convert_alpha(), 
        (50, 50)))

class Pebble_Shooter(Tower):
    """A shabby hut of allies thowing rocks
    lvl1:hay lvl2: sticks lvl3: rock"""
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.shooter_imgs = shooter_imgs[:]
        self.shooter_count = 0
        self.range = 150
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 15
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "archer"
        self.price = [2000, 4000, 8000]
        self.sell_price = [1500, 3000, 6000]
        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, 5000,"MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()

    def draw(self, win):
        """
        draw the shooter tower and animated shooter
        :param win: surface
        :return: int
        """
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving:
            self.shooter_count += 1
            if self.shooter_count >= len(self.shooter_imgs) * 10:
                self.shooter_count = 0
        else:
            self.shooter_count = 0

        shooter = self.shooter_imgs[self.shooter_count // 10]
        if self.left == True:
            add = -25
        else:
            add = -shooter.get_width() + 10
        win.blit(shooter, ((self.x + add), (self.y - shooter.get_height() - 25)))

    def change_range(self, r):
        """
        change range of shooter tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        points = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - enemy.img.get_width()/2 - x)**2 + (self.y -enemy.img.get_height()/2 - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.shooter_count == 0: # sets when the shooter fires
                if first_enemy.hit(self.damage) == True:
                    points = first_enemy.points * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.shooter_imgs):
                    self.shooter_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.shooter_imgs):
                    self.shooter_imgs[x] = pygame.transform.flip(img, True, False)

        return points


"""Concept radius growth due to support towers"""
# class Long(Pebble_Shooter):
#     def __init__(self, x,y):
#         super().__init__(x, y)
#         self.tower_imgs = tower_imgs[:]
#         self.shooter_imgs = shooter_imgs[:]
#         self.shooter_count = 0
#         self.range = 200
#         self.original_range = self.range
#         self.inRange = False
#         self.left = True
#         self.damage = 2
#         self.original_damage = self.damage

#         self.menu = Menu(self, self.x, self.y, menu_bg, [2500, 5500, "MAX"])
#         self.menu.add_btn(upgrade_btn, "Upgrade")
#         self.name = "shooter2"
