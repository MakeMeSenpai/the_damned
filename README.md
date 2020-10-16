# The Damned V.0.0.6
This is a Tower Defence Game, based on an old childhood favorite. Pick a Hero(/Monster) and fend off the wretched humans! (In Very beggining stages)

## Index:
1. [Checklist](#checklist)
    1. [MVP Todo:](#mvp-todo)
    2. [Potential Features:](#potential-features)
    3. [Previous Updates:](#previous-updates)
2. [Tutorial](#tutorial)
    1. [Enviroment Setup:](#enviroment-setup)
    2. [How To Play:](#how-to-play)
3. [Conclusion](#conclusion)

___
## Checklist

### MVP TODO:
- Setup 
    - [x] Name it
    - [x] Make a repo
    - [x] Setup enviroment
    - [x] install requirements + create requirements.txt
    - [x] **Stretch:** organize files in folders
- Create Basic Map
    - [x] Complete Research on your topic
    - [x] Create Wireframe for demo level
    - [x] Setup PyGame Window
    - [] Impliment Demo Level design into Pygame Background
- Create Objects
    - [x] Create Heroes Class
    - [ ] Create Sub-Hero Classes
    - [x] Create Enemies Class
    - [ ] Create Sub-Enemy Classes
    - [ ] Create Towers Class
    - [ ] Create Sub-Tower Classes
    - [ ] **Stretch:** Create Specials Class
    - [ ] **Stretch:** Create Sub-Special Class
- Functionality 
    - [ ] Heros must be able to move on the path
    - [ ] Enemies must follow the path and attack Home base. Bringing down Hero's Health
    - [ ] Enemies should stop if they run into the Hero
    - Heroes and Enemies should be able to attack one another. Thus killing Enemies and bringing down a Hero's Stamina
- Towers and CRUD
    - [ ] Players should be able to create towers by drag and drop.
    - [ ] Players should be able to Read what level a tower is, after clicking it
    - [ ] Towers should damage Enemies within it's personal range
    - [ ] Players should be able to Upgrade towers by clicking it in a the mini-menu
    - [ ] Players should be able to sell their towers by clicking it in a mini-menu
    - [ ] **Stretch:** Towers can only be placed in places that aren't blocked by the enviroment or other towers.
    - [ ] **Stretch:** Towers should be able to be destroyed by special enemies.

### Potential Features:
- Level-up
    - [ ] Create a level-up system for the hero
    - [ ] let players upgrade their hero or potetailly unlock new towers!
- Lively Enviroment
    - [ ] Create Items Class
    - [ ] Create Sub-Item Class
    - [ ] Display Items to give off a more lively background for the game.
- Special Towers
    - [ ] Create the Blockade Burgade! (tower sub-class)
- Special Ability
    - [ ] Create a special ability for each hero
    - [ ] let players select between special abilities based on their level


### Previous Updates:
{Last Update: 10/15/20}
- 0.0.2
    - An empty window now displays when you run the application. Which isn't very exciting but its defenitly a start. Code is being augmented and prepped for game creation! 
___
## Tutorial

### Enviroment Setup
    - You will need Python3 and git downloaded onto your computer
    - Open your computers terminal and go into a folder you would like this game to stay in. 
    - Once this is found use 
    ```$git clone https://github.com/MakeMeSenpai/the_damned```
    to install the game locally
    - Next, you will go inside that folder and use 
    ```$pip3 install requirements.txt```
    grabbing the game's necessary packages
    - Finally, you can run the game using ```$python3 main.py```

### How To Play
    - There's no game to play quite yet! I've been having touble with Pygames blit functions.

___
## Conclusion
If you'd like to learn more about how to make a Tower Defence game, check out this video by TechwithTim. https://www.youtube.com/watch?v=iLHAKXQBOoA&list=PL0JD8YOK85RoSodvtsgYIgwoBkZF6MHr3&index=17&app=desktop
Thanks for checking this out. Feel free to leave feedback, and share!