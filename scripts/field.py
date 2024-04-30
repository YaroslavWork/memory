import pygame.draw

from scripts.game import Game, SingleplayerGame, OnePCGame
from scripts.menu import Menu
import scripts.settings as s
from scripts.player import Player, Bot


class Field:

    def __init__(self, manager):
        self.manager = manager
        self.menu = Menu(self.manager)
        self.you = Player()
        #self.game = SingleplayerGame(pygame.Rect(10, 10, 700, 700), 36, 2, True)
        self.game = OnePCGame([self.you, Bot(), Bot(), Bot()], pygame.Rect(10, 10, 700, 700), 36, 3)

        self.is_game = True
        self.menu.hide_menu()

    def draw(self, screen):
        if self.is_game:
            self.game.draw(screen)
        else:
            self.menu.draw(screen)

    def update(self):
        if self.is_game:
            self.game.update()