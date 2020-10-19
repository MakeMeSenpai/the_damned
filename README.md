# The Damned V.0.1.3
This is a Tower Defence Game, based on an old childhood favorite. Pick a Hero(/Monster) and fend off the wretched humans! This game is still in early development.Check out "More Lore" for deeper description.

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
    - [x] Create Wireframe for demo level
    - [x] Setup PyGame Window
    - [x] Impliment Demo Level design into Pygame Background
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
    - [ ] Enemies must follow the path and attack Home base. Bringing down Hero's Health
    - [ ] Heros must be able to move on the path
    - [ ] Enemies should stop if they run into the Hero
    - [ ] Heroes and Enemies should be able to attack one another. Thus killing Enemies and bringing down a Hero's Stamina
- Towers and CRUD
    - [ ] Players should be able to create towers by drag and drop.
    - [ ] Players should be able to Read what level a tower is, after clicking it
    - [ ] Towers should damage Enemies within it's personal range
    - [ ] Players should be able to Upgrade towers by clicking it in a the mini-menu
    - [ ] Players should be able to sell their towers by clicking it in a mini-menu
    - [ ] **Stretch:** Towers can only be placed in places that aren't blocked by the enviroment or other towers.
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
{Last Update: 10/18/20}
- 0.1.3
    - Added git master branches for safer development. This lets me experiment with feature requests and more without breaking the current game. As well as other banches for more defined updates.

- 0.1.0
    - Background is now visual and ready!! Woot, woot! We are very much on our way to getting this thing off the ground and running.

- 0.0.8
    - place holders have been added, as well as a boat load of code that we still can't see. I don't suggest coding blidly, but when you are stuck, you still gotta keep working. As well, More Lore was added to this page to give you a better insight on the world I am trying to build here.

___
## Info

### Enviroment Setup
- You will need Python3 and git downloaded onto your computer
- Open your computers terminal and go into a folder you would like this game to stay in. 
- Once this is found use 
```$git clone https://github.com/MakeMeSenpai/the_damned```
to install the game locally
- Next, you will go inside that folder and use 
```$pip3 install -r requirements.txt```
grabbing the game's necessary packages
- Finally, you can run the game using 
```$python3 main.py```

### How To Play
- There's no game to play quite yet! I've been having touble with Pygames blit functions.

### More Lore
- In a world that is blind to the good of magic, mid evil kingdoms set to vanquish all "evils". You have been mistreated, and forced into hiding time and time again.  It seems that other magical beings are starting to detest the humans as well...
- The Angel:
    - Coming to this place to help those in need. You have been long appriciated by those who had fallen deathly ill. This was until they saw your wings... the kingdom has now claimed you guilty of witch craft! Infecting the poor souls, and the sick you have helped now want you dead. Even the rightous can be considered monsters. Your goal is to reclaim the land for the Holy Father.
- The Demon:
    - Escaping from hell is no easy task. You find joy in slaughtering the weak. Damn them all! But now everyone knows about the monster you really are, and now want you dead. Your will is your own. Too much pride isn't always a bad thing and niether is greed. They will feel your wrath as you take over the land.
- The Vampire:
    - You have been around for longer than you can rememeber. Must have been 4, or even 500 years since you first sunk your teeth into that widow's neck. You spent most of your time reading, and enjoying elegancy. But the towns folk started to realize that people were disappearing. The night watch became more and more difficult to hide from, and you were caught in the act. Now the inputant humans want you dead. The daywalkers are nothing but insolent cattle, and now you must put them in their place.
- The WereWolf:
    - You found out with when you were 10 just what you were... blacking out and killing your childhood best friend. Werewolves have a lack of control, especially when young. Every full moon the tranformation period lasting longer, fur growing longer, and teeth growing sharper. It's not your fault you were born this way. You just wanted to be like everybody else. The last full moon -as always- changed you into your form, and you have better learned how to control it. However, now you just won't turn back. Stuck in your howling state, some nosey kids had peeped into your window and had sworn to have seen a monster. Now the townsmen want you dead. You tried to be friends with them, and you tried to be them; But time and time again they take. May vengence be yours.

___
## Conclusion
If you'd like to learn more about how to make a Tower Defence game, check out this video by TechwithTim. https://www.youtube.com/watch?v=iLHAKXQBOoA&list=PL0JD8YOK85RoSodvtsgYIgwoBkZF6MHr3&index=17&app=desktop
Also! If you have an idea or want to recommend a feature, please do so in feature_requests.md 
Thanks for checking this out. Feel free to leave feedback, and share!
