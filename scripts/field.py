import pygame.draw

from scripts.menu import Menu
import scripts.settings as s

class Field:

    def __init__(self, manager):
        self.manager = manager
        self.menu = Menu(self.manager)

    def draw(self, screen):
        self.menu.draw(screen)