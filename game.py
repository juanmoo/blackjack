'''
Blackjack simulation
'''

from dotted_dict import DottedDict
from deck import Shoe

class BlackJackGame(object):
    def __init__(self, config):
        self.config = config
        self.shoe = Shoe(self.config.num_decks, config=self.config)
        self.hands_dealt = 0
        self.net_gain = 0

        # current hand
        self.is_playing_hand = False
        self.house_hand = []
        self.player_hand = []

    def deal_hand(self):

        self.is_playing_hand = True
        cards_pulled = []
        pulled_plastic = False

        while len(cards_pulled) < 4:
            c = self.shoe.pull_card()
            if c == '*':
                pulled_plastic = True
                break
            cards_pulled.append(c)

        # Give response

        # Check if player and/or house have BlackJack

if __name__ == '__main__':
    config = DottedDict()
    config.num_decks = 3
    config.blackjack_payout = 1.5

    game = BlackJackGame(config)

