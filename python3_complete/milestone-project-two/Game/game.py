from Deck import Deck
from HumanPlayer import HumanPlayer
from CpuPlayer import CpuPlayer


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = HumanPlayer('Kal')
        self.dealer = CpuPlayer('Dealer')
        self.game_on = True

    def run(self):
        player_turn = True
        dealer_limit_reached = False

        self.deck.shuffle()
        for _i in range(2):
            self.player.take_card(card=self.deck.deal())
            self.dealer.take_card(card=self.deck.deal())
        self.player.show_all()
        self.dealer.show_some()

        while self.game_on:
            while player_turn:
                player_wants_hit = self.hit_or_stay()
                if player_wants_hit:
                    self.player.take_card(card=self.deck.deal())
                    self.dealer.show_some()
                    self.player.show_all()
                else:
                    player_turn = False
                    break
                if self.player.has_busted():
                    while self.player.has_high_aces():
                        self.player.adjust_for_ace()
                        if self.player.get_score() <= 21:
                            break
                    else:
                        self.dealer_win()
                        player_turn = False

            while not dealer_limit_reached and self.game_on:
                if self.dealer.should_hit():
                    self.dealer.take_card(card=self.deck.deal())
                elif self.dealer.has_busted():
                    while self.dealer.has_high_aces():
                        self.dealer.adjust_for_ace()
                        if self.dealer.get_score() <= 21:
                            break
                    else:
                        self.player_win()
                        dealer_limit_reached = True
                else:
                    dealer_limit_reached = True
                    break

            if self.game_on:
                player_score = self.player.get_score()
                dealer_score = self.dealer.get_score()
                if player_score > dealer_score:
                    self.player_win()
                else:
                    self.dealer_win()

    def hit_or_stay(self):
        valid_choice = False
        while not valid_choice:
            choice = input('Would you like to hit? (y or n)  \n')
            if choice != 'y' and choice != 'n':
                print('Please enter either "y" or "n"\n')
            else:
                valid_choice = True
        return True if choice == 'y' else False

    def player_win(self):
        self.game_on = False
        print('\n****************\n')
        print('Final Hands:\n')
        self.dealer.show_all()
        self.player.show_all()
        print('Final Scores:\n')
        print(f'Dealer: {self.dealer.get_score()}')
        print(f'Player: {self.player.get_score()}\n')
        print('Player has won!\n')

    def dealer_win(self):
        self.game_on = False
        print('\n****************\n')
        print('Final Hands:\n')
        self.dealer.show_all()
        self.player.show_all()
        print('Final Scores:\n')
        print(f'Dealer: {self.dealer.get_score()}')
        print(f'Player: {self.player.get_score()}\n')
        print('Dealer has won!\n')
