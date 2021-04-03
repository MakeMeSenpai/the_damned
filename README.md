# The Damned V.0.2.3
This is a Tower Defence Game, based on an old childhood favorite. Pick a Hero(/Monster) and fend off the wretched humans! This game is still in early development. Check out "More Lore" for a deeper description.

## Index:
1. [Checklist](#checklist)
    1. [MVP Todo:](#mvp-todo)
    2. [Potential Features:](#potential-features)
    3. [Previous Updates:](#previous-updates)
2. [Info](#info)
    1. [Enviroment Setup:](#enviroment-setup)
    2. [How To Play:](#how-to-play)
    3. [More Lore:](#more-lore)
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
    - [x] Create Wireframe for the demo level
    - [x] Setup PyGame Window
    - [x] Implement Demo Level design into Pygame Background
- Create Objects
    - [x] Create Heroes Class
    - [x] Create Sub-Hero Classes
    - [x] Create Enemies Class
    - [x] Create Sub-Enemy Classes
    - [x] Create Towers Class
    - [x] Create Sub-Tower Classes
    - [x] **Stretch:** Create Specials Class
    - [x] **Stretch:** Create Sub-Special Class
- Functionality 
    - [x] Enemies must follow the path
    - [x] Enemies attack the Home base. Bringing down Hero's Health
    - [x] Heros must be able to move on the path
    - [ ] **Stretch:** Enemies should stop if they run into the Hero
    - [ ] **Stretch:**Heroes and Enemies should be able to attack one another. Thus killing Enemies and bringing down a Hero's Stamina
- Towers and CRUD
    - [x] Players should be able to create towers by drag and drop.
    - [ ] Players should be able to Read what level a tower is, after clicking it
    - [ ] Towers should damage Enemies within its personal range
    - [ ] Players should be able to Upgrade towers by clicking it in the mini-menu
    - [ ] Players should be able to sell their towers by clicking it in a mini-menu
    - [ ] **Stretch:** Towers can only be placed in places that aren't blocked by the environment or other towers.
    - [ ] **Stretch:** Towers should be able to be destroyed by special enemies.

### Potential Features:
- GitMaster
    - [x] Set up tester branch -for expirements (such as a Feature request)
    - [x] Set up developer branch -for actual development
    - [x] Set up demo branch -for prereleases and bug fixing (such as a hotfix branch)
- Level-up
    - [ ] Create a level-up system for the hero
    - [ ] let players upgrade their hero or potentially unlock new towers!
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
{Last Update: 10/19/20}
- 0.2.3
    - You can now drag and drop towers! This is... extremely glitchy, and crashes when no enemies are on the screen. But hey! one step at a time, right?

- 0.2.1
    - The monster has been born! The Hero, -for now- will be chosen randomly until we get a character selection page going. You can now see and move your character threw out the map... even though it's pretty slow-moving.

- 0.1.9
    - A house is displayed! And with that, the player can now lose the game if too many enemies get into a collision with it.

___
## Info

### Environment Setup
- You will need Python3 and git downloaded onto your computer
- Open your computer’s terminal and go into a folder you would like this game to stay in. 
- Once this is found use 
```$git clone https://github.com/MakeMeSenpai/the_damned```
to install the game locally
- Next, you will go inside that folder and use 
```$pip3 install -r requirements.txt```
grabbing the game's necessary packages
- Finally, you can run the game using 
```$python3 main.py```

### How To Play
- There's no game to play quite yet! I've been having trouble with Pygames blit functions.

### More Lore
- In a world that is blind to the good of magic, mid-evil kingdoms set to vanquish all "evils". You have been mistreated, and forced into hiding time and time again.  It seems that other magical beings are starting to detest the humans as well...
- The Angel:
    - Coming to this place to help those in need. You have been long appreciated by those who had fallen deathly ill. This was until they saw your wings... the kingdom has now claimed you guilty of witchcraft! Infecting the poor souls, and the sick you have once helped now want you dead. Even the righteous can be considered monsters. Your goal is to reclaim the land for the Holy Father.
- The Demon:
    - Escaping from hell is no easy task. You find joy in slaughtering the weak. Damn them all! But now everyone knows about the monster you really are, and now wants you dead. Your will is your own. Too much pride isn't always a bad thing and neither is greed. They will feel your wrath as you take over the land.
- The Vampire:
    - You have been around for longer than you can remember. Must have been 4, or even 500 years since you first sank your teeth into that widow's neck. You spent most of your time reading and enjoying elegancy. But the townsfolk started to realize that people were disappearing. The night watch became more and more difficult to hide from, and you were caught in the act. Now the impertinent humans want you dead. The daywalkers are nothing but insolent cattle, and now you must put them in their place.
- The WereWolf:
    - You found out when you were 10 just what you are... blacking out and killing your childhood best friend. Werewolves have a lack of control, especially when young. Every full moon the transformation period lasting longer, fur growing longer, and teeth growing sharper. It's not your fault you were born this way. You just wanted to be like everybody else. The last full moon -as always- changed you into your form, and you have learned how to control it better. However, now you just won't turn back. Stuck in your howling state, some nosey kids had peeped into your window and had sworn to have seen a monster. Now the townsmen want you dead. You tried to be friends with them, and you tried to be them, But time and time again they take. May vengeance be yours.

___
## Conclusion
If you'd like to learn more about how to make a Tower Defence game, check out this video by TechwithTim. https://www.youtube.com/watch?v=iLHAKXQBOoA&list=PL0JD8YOK85RoSodvtsgYIgwoBkZF6MHr3&index=17&app=desktop
Also! If you have an idea or want to recommend a feature, please do so in feature_requests.md 
Thanks for checking this out. Feel free to leave feedback, and share!
