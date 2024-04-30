import pygame
import random
import enum
import time

from scripts.UI.text import Text
import scripts.settings as s
from scripts.player import Player, Bot


def generate_field(size, card_connection):
    pos = [i for i in range(size)]
    values = [i for i in range(size//card_connection)]*card_connection
    field = [-1 for _ in range(size)]
    for i in range(len(values)):
        idx = random.choice(pos)
        pos.remove(idx)
        field[idx] = values[i]

    return field

class GameStatus(enum.Enum):
    PREPARING = 0
    STARTED = 1
    FINISHED = 2

class Game:

    def __init__(self, field_rect, size=16, card_connection=2):
        self.field_rect = field_rect
        card_size = (field_rect.width-(int(size**(1/2))+1)*10)//int(size**(1/2))
        self.cards = [pygame.Rect(i*(card_size+10)+field_rect.left+10, j*(card_size+10)+field_rect.top+10, card_size, card_size) for i in range(int(size**(1/2))) for j in range(int(size**(1/2)))]
        self.content = [None for _ in range(size)]
        self.solved = [None for _ in range(size)]
        self.card_connection = card_connection
        self.opened: list[list[int, int]] = [] #Index, value

        self.move_idx = 0
        self.game_status = GameStatus.PREPARING

        self.start_time = 0
        self.moves = 0


    def close_card(self):
        self.opened = []
        for content in self.content:
            if type(content) == Text:
                content.hide()

    def check_if_the_same(self):
        is_the_same = True
        for idx, value in self.opened:
            if value != self.opened[0][1]:
                is_the_same = False
                break

        return is_the_same


    def card_draw(self, screen):
        pygame.draw.rect(screen, s.COLORS["second_background"], self.field_rect)

        for i, card in enumerate(self.cards):
            if self.solved[i] is not None:
                match self.solved[i]:
                    case 0:
                        pygame.draw.rect(screen, s.COLORS["red_player_secondary"], card)
                    case 1:
                        pygame.draw.rect(screen, s.COLORS["blue_player_secondary"], card)
                    case 2:
                        pygame.draw.rect(screen, s.COLORS["green_player_secondary"], card)
                    case 3:
                        pygame.draw.rect(screen, s.COLORS["yellow_player_secondary"], card)
                continue


            pygame.draw.rect(screen, (240, 175, 139), card)
            pygame.draw.rect(screen, (0, 0, 0), card, 2)

        for idx, value in self.opened:
            if self.content[idx] is None:
                pos = [self.cards[idx].center[0], self.cards[idx].center[1]+self.cards[idx].width/20]
                self.content[idx] = Text(pos, str(value), s.COLORS["text_primary"], int(self.cards[idx].width*0.9), s.FONTS)
            else:
                self.content[idx].show()

            pygame.draw.rect(screen, (255, 227, 211), self.cards[idx])
            pygame.draw.rect(screen, (0, 0, 0), self.cards[idx], 2)

    def update(self):
        pass

class SingleplayerGame(Game):
    def __init__(self, field_rect, size=16, card_connection=2, is_move=True):
        super().__init__(field_rect, size, card_connection)
        self.field = generate_field(size, card_connection)
        self.is_move = is_move

        self.info_content = None
        if self.is_move:
            self.info_content = Text((s.SIZE[0]*0.67, s.SIZE[1]*0.05), "Moves: 0", s.COLORS["text_primary"], 40, s.FONTS, False)
        else:
            self.info_content = Text((s.SIZE[0]*0.67, s.SIZE[1]*0.05), "Time: 00:00.000", s.COLORS["text_primary"], 40, s.FONTS, False)

    def find_card(self, mouse_pos):
        if len(self.opened) == self.card_connection:
            self.close_card()
            return

        for i in range(len(self.cards)):
            if self.cards[i].collidepoint(mouse_pos) and self.solved[i] is None:
                if self.game_status == GameStatus.PREPARING:
                    self.game_status = GameStatus.STARTED
                    self.start_time = time.time()

                if i not in [idx for idx, _ in self.opened]:
                    self.opened.append([i, self.field[i]])
                    if len(self.opened) == self.card_connection:
                        is_the_same = self.check_if_the_same()

                        if is_the_same:
                            for idx, _ in self.opened:
                                self.solved[idx] = 0

                            if None not in self.solved:
                                self.game_status = GameStatus.FINISHED
                                self.start_time = time.time()-self.start_time
                        else:
                            self.moves += 1

                break

    def draw(self, screen):
        self.card_draw(screen)
        if self.is_move:
            self.info_content.change_text(f"Moves: {self.moves}")
        else:
            # Time format: 00:00.000
            if self.game_status == GameStatus.PREPARING:
                self.info_content.change_text(f"Time: 00:00.000")
            if self.game_status == GameStatus.STARTED:
                minutes = int(time.time()-self.start_time)//60
                seconds = int(time.time()-self.start_time)%60
                milliseconds = int((time.time()-self.start_time)*1000)%1000
                self.info_content.change_text(f"Time: {str(minutes).zfill(2)}:{str(seconds).zfill(2)}.{str(milliseconds).zfill(3)}")
            else:
                minutes = int(self.start_time)//60
                seconds = int(self.start_time)%60
                milliseconds = int(self.start_time*1000)%1000
                self.info_content.change_text(f"Time: {str(minutes).zfill(2)}:{str(seconds).zfill(2)}.{str(milliseconds).zfill(3)}")

class OnePCGame(Game):

    def __init__(self, players, field_rect, size=16, card_connection=2):
        super().__init__(field_rect, size, card_connection)
        self.players = players
        self.field = generate_field(size, card_connection)
        self.current_player = 0

        self.last_open_card = 0
        self.interface_is_blocked = False

    def add_to_memory(self):
        for player in self.players:
            if type(player) == Bot:
                player.add_seen_card(self.opened)

    def delete_opened_from_memory(self):
        not_available = [i for i in range(len(self.field)) if self.solved[i] is not None]
        for player in self.players:
            if type(player) == Bot:
                player.delete_not_available_cards(not_available)


    def result_for_opened(self, is_the_same=False):
        if is_the_same:
            for idx, _ in self.opened:
                self.solved[idx] = self.current_player

            if None not in self.solved:
                self.game_status = GameStatus.FINISHED
        else:
            self.current_player = (self.current_player+1)%len(self.players)


    def find_card(self, mouse_pos):
        for i in range(len(self.cards)):
            if self.cards[i].collidepoint(mouse_pos) and self.solved[i] is None and not self.interface_is_blocked:
                return i
        return -1

    def open_card(self, index):
        if index not in [idx for idx, _ in self.opened]:
            self.last_open_card = time.time()
            self.opened.append([index, self.field[index]])
            if len(self.opened) == self.card_connection:
                self.interface_is_blocked = True
                is_the_same = self.check_if_the_same()
                self.add_to_memory()
                self.result_for_opened(is_the_same)
                self.delete_opened_from_memory()

    def draw(self, screen):
        self.card_draw(screen)

    def update(self):
        if len(self.opened) == self.card_connection and time.time()-self.last_open_card > 1:
            self.close_card()
            if type(self.players[self.current_player]) == Bot:
                print("BOT PLAYING")
                self.interface_is_blocked = True
                avaialble_cards = [i for i in range(len(self.field)) if self.solved[i] is None]
                cards_idx = self.players[self.current_player].make_choice(self.card_connection, avaialble_cards)
                for i in range(len(cards_idx)):
                    self.open_card(cards_idx[i])
            else:
                self.interface_is_blocked = False