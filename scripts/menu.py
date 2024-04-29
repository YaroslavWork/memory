import pygame
import pygame_gui
import scripts.settings as s
from scripts.UI.button import Button
from scripts.UI.text import Text
import random


class Menu:

    def __init__(self, manager):
        self.manager = manager

        self.menu_layout = {
            "main_menu": [
                #pygame_gui.elements.UIButton(relative_rect=pygame.Rect((377, 231), (364, 80)), text="Singleplayer", manager=self.manager),
                Button(pygame.Rect((377, 231), (364, 80)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, Text(pygame.Rect((377, 231), (364, 80)).center, "SINGLEPLAYER", s.COLORS["text_primary"], 40, s.FONTS)),
                #pygame_gui.elements.UIButton(relative_rect=pygame.Rect((377, 339), (364, 80)), text="Multiplayer", manager=self.manager),
                Button(pygame.Rect((377, 339), (364, 80)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, Text(pygame.Rect((377, 339), (364, 80)).center, "MULTIPLAYER", s.COLORS["text_primary"], 40, s.FONTS)),
                #pygame_gui.elements.UIButton(relative_rect=pygame.Rect((377, 447), (364, 80)), text="Settings", manager=self.manager),
                Button(pygame.Rect((377, 447), (364, 80)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, Text(pygame.Rect((377, 447), (364, 80)).center, "SETTINGS", s.COLORS["text_primary"], 40, s.FONTS)),
                #pygame_gui.elements.UIButton(relative_rect=pygame.Rect((377, 555), (364, 80)), text="Exit", manager=self.manager)
                Button(pygame.Rect((377, 555), (364, 80)), s.COLORS["button_exit_background"], s.COLORS["button_exit_hover"], s.COLORS["button_exit_press"], s.COLORS["button_border"], 2, Text(pygame.Rect((377, 555), (364, 80)).center, "EXIT", s.COLORS["text_primary"], 40, s.FONTS)),
                [s.SPRITES["background"], [0, 0]],
                [s.SPRITES["logo"], [278, 16]],
                [s.SPRITES["singleplayer"], [288, 237]],
                [s.SPRITES["multiplayer"], [288, 345]],
                [s.SPRITES["settings"], [288, 453]],
                [s.SPRITES["exit"], [295, 564]]
            ],
            "singleplayer_rules": [
                Button(pygame.Rect((260, 365), (32, 50)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, s.SPRITES["left_click"]),
                Button(pygame.Rect((419, 365), (32, 50)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, s.SPRITES["right_click"]),
                Button(pygame.Rect((601, 365), (32, 50)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, s.SPRITES["left_click"]),
                Button(pygame.Rect((760, 365), (32, 50)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, s.SPRITES["right_click"]),
                Button(pygame.Rect((909, 377), (40, 28)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, s.SPRITES["slider"]),
                Button(pygame.Rect((196, 522), (75, 75)), s.COLORS["button_primary_background"], s.COLORS["button_primary_hover"], s.COLORS["button_primary_press"], s.COLORS["button_border"], 2, s.SPRITES["random"]),
                Button(pygame.Rect((837, 522), (189, 75)), s.COLORS["button_play_background"], s.COLORS["button_play_hover"], s.COLORS["button_play_press"], s.COLORS["button_border"], 2, s.SPRITES["start_game"]),
                Text(pygame.Rect((165, 231), (893, 80)).center, "RULES OF THE GAME", s.COLORS["text_primary"], 40, s.FONTS),
                Text(pygame.Rect((298, 374), (116, 24)).center, "SMALL", s.COLORS["text_primary"], 19, s.FONTS),
                Text(pygame.Rect((639, 374), (116, 24)).center, "EASY", s.COLORS["text_primary"], 19, s.FONTS),
                Text(pygame.Rect((340, 394), (31, 14)).center, "4x4", s.COLORS["text_primary"], 12, s.FONTS),
                Text(pygame.Rect((681, 394), (31, 14)).center, "2", s.COLORS["text_primary"], 12, s.FONTS),
                Text(pygame.Rect((195, 422), (262, 17)).center, "Size", s.COLORS["text_primary"], 14, s.FONTS),
                Text(pygame.Rect((536, 422), (262, 17)).center, "Card Connection", s.COLORS["text_primary"], 14, s.FONTS),
                Text(pygame.Rect((877, 422), (149, 17)).center, "Move or time", s.COLORS["text_primary"], 14, s.FONTS),
                Text(pygame.Rect((197, 600), (73, 15)).center, "Random", s.COLORS["text_primary"], 14, s.FONTS),
                Text(pygame.Rect((837, 600), (189, 15)).center, "Start game", s.COLORS["text_primary"], 14, s.FONTS),
                [s.SPRITES["background"], [0, 0]],
                [pygame.Rect((165, 231), (893, 404)), s.COLORS["second_background"], 0],
                [pygame.Rect((297, 373), (117, 34)), s.COLORS["text_primary"], 1],
                [pygame.Rect((638, 373), (117, 34)), s.COLORS["text_primary"], 1],
                [pygame.Rect((909, 377), (80, 28)), s.COLORS["text_primary"], 1],
                [pygame.Rect((196, 421), (261, 1)), s.COLORS["text_primary"], 0],
                [pygame.Rect((537, 421), (261, 1)), s.COLORS["text_primary"], 0],
                [pygame.Rect((878, 421), (148, 1)), s.COLORS["text_primary"], 0],
                [s.SPRITES["logo"], [278, 16]],
                [s.SPRITES["size"], [196, 358]],
                [s.SPRITES["card_connection"], [546, 369]],
                [s.SPRITES["move"], [880, 377]],
                [s.SPRITES["time"], [992, 377]],
            ]
        }

        self.size_statuses = ["SMALL", "MEDIUM", "LARGE"]
        self.size_number_statuses = ["4x4", "6x6", "8x8"]
        self.card_connection_statuses = ["EASY", "MEDIUM", "HARD"]
        self.card_connection_number_statuses = ["2", "3", "4"]

        self.idx_size = 0
        self.idx_card_connection = 0
        self.is_move = True

        self.buttons_action = {
            "main_menu": [
                lambda: self.update("singleplayer_rules"),
                lambda: ...,
                lambda: ...,
                lambda: ...,
            ],
            "singleplayer_rules": [
                lambda: self.change_size(to_right=False),
                lambda: self.change_size(to_right=True),
                lambda: self.change_card_connection(to_right=False),
                lambda: self.change_card_connection(to_right=True),
                lambda: self.change_game_type(),
                lambda: self.set_random(),
                lambda: ...,
            ]
        }

        self.active_menu = "main_menu"

        # Move for all buttons and disable them
        for key, value in self.menu_layout.items():
            for element in value:
                if type(element) == Button:
                    element.give_action(self.buttons_action[key][value.index(element)])

            if key == self.active_menu:
                for element in value:
                    if type(element) == Button:
                        element.enable()
                        element.show()
                    elif type(element) == Text:
                        element.show()
            else:
                for element in value:
                    if type(element) == Button:
                        element.disable()
                        element.hide()
                    elif type(element) == Text:
                        element.hide()

    def change_size(self, to_right=True):
        self.idx_size += 1 if to_right else -1
        if self.idx_size < 0:
            self.idx_size = 0
        elif self.idx_size >= len(self.size_statuses):
            self.idx_size = len(self.size_statuses) - 1

        self.menu_layout["singleplayer_rules"][8].change_text(self.size_statuses[self.idx_size])
        self.menu_layout["singleplayer_rules"][10].change_text(self.size_number_statuses[self.idx_size])

    def change_card_connection(self, to_right=True):
        self.idx_card_connection += 1 if to_right else -1
        if self.idx_card_connection < 0:
            self.idx_card_connection = 0
        elif self.idx_card_connection >= len(self.card_connection_statuses):
            self.idx_card_connection = len(self.card_connection_statuses) - 1

        self.menu_layout["singleplayer_rules"][9].change_text(self.card_connection_statuses[self.idx_card_connection])
        self.menu_layout["singleplayer_rules"][11].change_text(self.card_connection_number_statuses[self.idx_card_connection])

    def change_game_type(self):
        self.is_move = not self.is_move
        self.menu_layout["singleplayer_rules"][4].change_position((909, 377) if self.is_move else (949, 377))

    def set_random(self):
        for i in range(2):
            self.change_size(to_right=random.choice([True, False]))
            self.change_card_connection(to_right=random.choice([True, False]))

        for i in range(random.randint(0, 1)):
            self.change_game_type()


    def draw(self):
        # Text drawing
        texts = [element for element in self.menu_layout[self.active_menu] if type(element) == Text]


    def update(self, menu_name):
        self.active_menu = menu_name

        for key, value in self.menu_layout.items():
            if key == self.active_menu:
                for element in value:
                    if type(element) == Button:
                        element.enable()
                        element.show()
                    elif type(element) == Text:
                        element.show()
            else:
                for element in value:
                    if type(element) == Button:
                        element.disable()
                        element.hide()
                    elif type(element) == Text:
                        element.hide()

    def draw(self, screen):
        for element in self.menu_layout[self.active_menu]:
            if type(element) == list and type(element[0]) == pygame.surface.Surface:
                screen.blit(element[0], element[1])
            elif type(element) == list and type(element[0]) == pygame.Rect:
                pygame.draw.rect(screen, element[1], element[0], element[2])
                if element[2] == 0:
                    pygame.draw.rect(screen, s.COLORS["button_border"], element[0], 1)