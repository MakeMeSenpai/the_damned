# game.py
import pygame
import sys
import math
import os
import time
import random
# Menues
from Components.Menues.menu import Button
from Components.Menues.menu import PlayPauseButton
from Components.Menues.menu import VerticalButton
from Components.Menues.menu import VerticalMenu
from Components.Menues.menu import Menu
# imports Heroes
from Components.Heroes.hero import Hero
from Components.Heroes.angel import Angel
from Components.Heroes.demon import Demon
from Components.Heroes.werewolf import Werewolf
from Components.Heroes.vampire import Vampire
# imports Enemies
from Components.Enemies.enemy import Enemy
from Components.Enemies.peasant import Peasant
from Components.Enemies.knight import Knight
from Components.Enemies.archer import Archer
from Components.Enemies.murauder import Murauder
# imports Towers
from Components.Towers.tower import Tower
from Components.Towers.Base.base import Base
from Components.Towers.Shooters.pebble_shooter import Pebble_Shooter
from Components.Towers.Shooters.mage import Mage
from Components.Towers.Roadblocks.blockade_burgade import Blockade_Burgade
from Components.Towers.Support.harvester import Harvester
#from Components. import


# Initiation
pygame.font.init()
"""Level selection: load levels background, and paths"""
# by default demo-level should be selected, we will impliment level selection later
# level = ["lvl-1", "lvl 2", "lvl 3"...]
# Level name asset
# lvl_name = background that will hold our lvl text - maybe add wave too
bg = pygame.image.load(os.path.join("Assets/Backgrounds", "demo-level.png")) #.convert()
path = [(-10, 169), (999, 170), (999, 327), (871, 371), (699, 412), (220, 454), (149, 465), (101, 514), (96, 708), (124, 760), (189, 794), (722, 799), (778, 766), (808, 699), (816, 597)]
# pygame.mixer.music.load(os.path.join("game_assets", "music.mp3"))
# wave selector based on level -maybe need a database lvl.db||waves.db
# Demo level waves (15 waves)
waves = [
    #demo demo wave lol
    [25, 50, 25, 10]
    # [1, 0, 0, 0],
    # [25, 1, 0, 0],
    # [0, 25, 1, 0],
    # [25, 0, 25, 1],
    # [50, 25, 0, 25],
    # [50, 50, 25, 0],
    # [50, 50, 50, 25],
    # [50, 50, 50, 50],
    # [100, 50, 50, 50],
    # [150, 100, 50, 50],
    # [200, 150, 100, 50],
    # [250, 200, 150, 100],
]

"""needed assets = pygame.transform.scale(pygame.image.load(os.path.join("Assets",".PNG")).convert_alpha(), (75, 75))"""
# Health bar asset
# stamina bar asset
# special move asset

"""buy menu assets - temp icons"""
buy_icon = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Icons","temp_buy.PNG")).convert(), (75, 75))
locked_icon = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Icons","empty_slot.PNG")).convert(), (75, 75))
temp_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Icons","temp_img.PNG")).convert(), (75, 75))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Icons","temp_pause.PNG")).convert(), (75, 75))

"""pause assets: a pause menu should appear with settings when clicked"""
# music settings
# exiting to level select 
# saving and quiting game



class Game:
    def __init__(self, win):
        self.width = 1250
        self.height = 845
        self.win = win
        # everything will spawn in demo level, but enemies should spawn based on lvl
        self.enemies = [] # "peasant", "knight", "archer", "murauder"]
        # Demo-level will auto select. But players will be able to choose their hero in future development.
        # these lines should definitly look better
        self.heroes = [Angel(808, 699, 70, 70), Demon(808, 699, 70, 70), Vampire(808, 699, 70, 70), Werewolf(808, 699, 70, 70)]
        self.hero = random.choice(self.heroes)
        # all our towers
        self.towers = []
        # and of course our main base
        self.base = Base(816, 597)
        self.health = 150
        self.points = 5000
        self.bg = pygame.image.load(os.path.join("Assets/Backgrounds", "demo-level.png"))
        self.clicks = [] #mouse positions
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - 100 + 70, 250, temp_img)# [some-asset].get_width() + 70, 250, [some-asset])
        self.menu.add_btn(buy_icon, "buy_pebble_shooter", 2000)
        self.menu.add_btn(buy_icon, "buy_mage", 2000)
        self.menu.add_btn(buy_icon, "buy_harvester", 2000)
        self.menu.add_btn(locked_icon, "empty_slot", 0)
        self.moving_object = None
        self.lvl_name = 250 #this should be an image but for now will be a int for sizing
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.wave_bg = temp_img
        """pause menu"""
        self.pause = True
        # self.music_on = True
        self.playPauseButton = PlayPauseButton(pause_btn, 10, self.height - 85)
        # self.soundButton = PlayPauseButton(sound_btn, sound_btn_off, 90, self.height - 85)

    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
        else:
            wave_enemies = [Peasant(), Knight(), Archer(), Murauder()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def run(self):
        """Runs our PyGame Window
        run: Bool
        bg: background image
        :returns: None"""
        # pygame.mixer.music.play(loops=-1)
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(4) #FPS - youll get faster fps once you optimize this code!
            if self.pause == False:
                # gen monsters
                if time.time() - self.timer >= random.randrange(1,6)/3:
                    self.timer = time.time()
                    self.gen_enemies()

            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                collide = False
                for tower in self.towers:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
    
                """ used for path_creator() """
                # pos = pygame.mouse.get_pos()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.clicks.append(pos)
                #     print(self.clicks)
                """ Concept functions - impliments later """
                # self.path_creator(event)
                # self.level_selector()

                """ moves the player around and controls all our keyboard commands"""
                # TODO: should move if held down -should be smaller but whatever
                if event.type == pygame.KEYDOWN:
                    # ord changes key input into ints
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        print('up')
                        self.hero.move(0, -1)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        print('down')
                        self.hero.move(0, 1)
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        print('left')
                        self.hero.move(-1, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        print('right')
                        self.hero.move(1, 0)
                    if event.key == pygame.K_SPACE or event.key == 32:
                        print('attack')
                        # future development

                """ if no key is being pressed """
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        print('stop up')
                        self.hero.move(0, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        print('stop down')
                        self.hero.move(0, 0)
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        print('stop left')
                        self.hero.move(0, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        print('stop right')
                        self.hero.move(0, 0)
                    if event.key == pygame.K_SPACE or event.key == 32:
                        print('stop attack')
                        # future development
                    if event.key == ord('q'):
                        pygame.quit()
                        sys.exit()
                        run = False

                """ For drag & Drop """
                if event.type == pygame.MOUSEBUTTONUP:
                    # if you're moving an object and click
                    if self.moving_object:
                        not_allowed = False
                        for tower in self.towers:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            self.towers.append(self.moving_object)
                            # elif self.moving_object.name in support_tower_names:
                            #     self.support_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    """buy tower from buy menu concept"""
                else:
                    # look if you click on side menu
                    side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                    if side_menu_button:
                        cost = self.menu.get_item_cost(side_menu_button)
                        if self.points >= cost:
                            self.points -= cost
                            self.add_tower(side_menu_button)

                    # look if you clicked on a tower
                    btn_clicked = None
                    if self.selected_tower:
                        btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                        if btn_clicked:
                            if btn_clicked == "Upgrade":
                                cost = self.selected_tower.get_upgrade_cost()
                                if self.points >= cost:
                                    self.points -= cost
                                    self.selected_tower.upgrade()
                    
                    # check for play or pause
                    if self.playPauseButton.click(pos[0], pos[1]):
                        self.pause = not(self.pause)
                        self.playPauseButton.paused = self.pause

                    # if self.soundButton.click(pos[0], pos[1]):
                    #     self.music_on = not(self.music_on)
                    #     self.soundButton.paused = self.music_on
                    #     if self.music_on:
                    #         pygame.mixer.music.unpause()
                    #     else:
                    #         pygame.mixer.music.pause()

                    if not(btn_clicked):
                        # look if you clicked on a tower
                        for tw in self.towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False

            # loop through enemies
            if not self.pause:
                to_del = []
                for en in self.enemies:
                    en.move()
                    if self.base.collision(en.x, en.y):
                        to_del.append(en)

                # delete all enemies off the screen
                for d in to_del:
                    self.health -= 1
                    self.enemies.remove(d)

                # loop through attack towers
                for tw in self.towers:
                    self.points += tw.attack(self.enemies)

                # if you lose
                if self.health <= 0:
                    print("You Lose")
                    run = False

            self.draw()
        pygame.quit()


    def point_to_line(self, tower):
        """
        returns if you can place tower based on distance from
        path. Might also help us move player only on path.
        :param tower: Tower
        :return: Bool
        """
        # find two closest points
        return True
    


    def level_selector(self, selected):
        """ Sets path and background based on previously created
        levels!
        <concept>
        :param level: int
        :return: None"""
        # demo-level: 
        #   bg: demo-level.png 
        #   clicks: []
        pass
    
    def draw(self):
        """ Creates our background
        :returns: None"""
        self.win.blit(self.bg, (0, 0))

        """ used for path_creator() """
        # for p in self.clicks:
        #     pygame.draw.circle(self.win, (155, 0, 155), (p[0], p[1]), 5, 0)

        # draw our home base -should change base on lvl
        self.base.draw(self.win)
        self.hero.draw(self.win)

        # draw placement rings
        if self.moving_object:
            for tower in self.towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

        # draw towers
        for tw in self.towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemies:
            en.draw(self.win)

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        self.menu.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

        # # draw music toggle button
        # self.soundButton.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.health), 1, (255,255,255))
        life = pygame.transform.scale(temp_img,(50,50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        # draw points
        text = self.life_font.render(str(self.points), 1, (255, 255, 255))
        points = pygame.transform.scale(temp_img, (50, 50))
        start_x = self.width - 40 # life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(points, (start_x, 65))

        # # draw lvl
        # self.win.blit(bg, (10,10))
        # text = self.life_font.render("Wave #" + str(self.wave), 1, (255,255,255))
        # self.win.blit(text, (10 + self.wave_bg.get_width()/2 - text.get_width()/2, 25))
        # # maybe we don't need self.lvl_name, just lvl_name. Check for duplicating and useless code.

        pygame.display.update()
    

    def path_creator(self, event):
        """ Helps us create enemies paths by creating visual and 
        printed feedback, in console.
        event: pygame.event.get()
        :returns: Bool"""
        #** make a function that checks if this function is in use
        #** maybe make it so that players can create custom lvls
        #** but that's way way future. 
        # if event != None:
        #     pos = pygame.mouse.get_pos()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         self.clicks.append(pos)
        #         print(self.clicks)
        #     return True
        # else:
        #     return False

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_pebble_shooter", "buy_mage", "buy_harvester", "empty_slot"] # "buy_blockade_burgade"]
        object_list = [Pebble_Shooter(x,y), Mage(x,y), Harvester(x,y), None] # Blockade_Burgade(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")
