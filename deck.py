'''
Deck object for blackjack game.
'''
import random


class Shoe(object):
    def __init__(self, num_decks, config=None):
        self.config = config
        self.num_decks = num_decks
        self.symbol_map = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        self.num_dealt = 0
        self.count = 0

        # initialize decks
        self.stack = []
        for _ in range(self.num_decks):
            deck = list(range(1,14))
            deck *= 4
            random.shuffle(deck)
            self.stack.extend(deck)
        self.num_cards = len(self.stack)

        # place divide card in second to last 1/8 of cards
        start = int(self.num_cards * (6/8) + 0.5)
        stop = int(self.num_cards * (7/8) + 0.5)
        j = random.randint(start, stop - 1)
        self.stack.insert(j, '*')

    def pull_card(self):

        if self.num_dealt >= self.num_cards:
            # No cards left to deal
            return None

        card = self.stack[self.num_dealt]
        
        # update count
        if card == '*':
            return card
        elif card == 0 or card >= 10:
            self.count -= 1
        elif 2 <= card <= 6:
            self.count += 1
        # 7 <= card <= 9 does nothing
        # plastic (*) does nothing

        self.num_dealt += 1

        return card

    def get_count(self):
        return self.count

    def get_true_count(self):
        half_decks_left = int( (self.num_cards - self.num_dealt)/26.0 + 0.5 )
        return self.count/half_decks_left
    
    def __repr__(self) -> str:
        shoe_top = self.stack[self.num_dealt: self.num_dealt + 5]
        shoe_top = ', '.join([self.symbol_map.get(j, str(j)) for j in shoe_top])
        return f'<Dealt Count: {self.num_dealt}, Count: {self.count}, Total Cards: {self.num_cards} Shoe Top: [{shoe_top}, ...], >'


if __name__ == '__main__':
    shoe = Shoe(2)
    print(shoe)

