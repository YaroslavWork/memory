import uuid
import random


class Player():

    def __init__(self, name=""):
        self.uuid = uuid.uuid4()
        self.name = name

class Bot(Player):

    def __init__(self, name="", level_of_memory=0.5):
        super().__init__(name)
        self.level_of_memory = level_of_memory  # 0 - 1 when 0 is no memory and 1 is perfect memory
        self.memory = [] # Index, value
        self.make_a_decision = False

    def delete_not_available_cards(self, not_available):
        i = 0
        while i < len(self.memory):
            if self.memory[i][0] in not_available:
                del self.memory[i]
            else:
                i += 1

    def add_seen_card(self, cards: list[int, int]):
        for card in cards:
            if random.random() <= self.level_of_memory:
                if card not in self.memory:
                    self.memory.append(card)

    def make_choice(self, card_connection, available_cards):
        self.make_a_decision = True
        values_count = {} # Value, count
        for i in range(len(self.memory)):
            if self.memory[i][1] not in values_count:
                values_count[self.memory[i][1]] = 1
            else:
                values_count[self.memory[i][1]] += 1

        del_keys = []
        for key, value in values_count.items():
            if value < card_connection:
                del_keys.append(key)
        for key in del_keys:
            del values_count[key]

        if len(values_count) == 0:
            random.shuffle(available_cards)
            return available_cards[:card_connection]

        keys = list(values_count.keys())
        rand_value = random.choice(keys)
        card_idx = []
        for i in range(len(self.memory)):
            if self.memory[i][1] == rand_value:
                card_idx.append(self.memory[i][0])

        random.shuffle(card_idx)
        return card_idx