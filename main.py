#!python3
import pygame

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1250, 845))
    from .game import Game
    new_game = Game(win)
    new_game.run()