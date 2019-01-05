from Deck import Deck
from HumanPlayer import HumanPlayer
from CpuPlayer import CpuPlayer


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = HumanPlayer('Kal')
        self.dealer = CpuPlayer('Dealer')
        self.game_on = True

    def run(self, replay=False):
        player_turn = True
        dealer_limit_reached = False

        if replay:
            if self.player.no_chips() and self.will_player_play():
                self.ask_for_buy_in()
                self.ask_for_bet()
            elif not self.player.no_chips():
                self.ask_for_bet()
            else:
                self.game_on = False
        else:
            if self.will_player_play():
                self.ask_for_buy_in()
                self.ask_for_bet()
            else:
                self.game_on = False

        if self.game_on:
            self.deck.shuffle()
            for _i in range(2):
                self.player.take_card(card=self.deck.deal())
                self.dealer.take_card(card=self.deck.deal())
            self.player.show_all()
            self.dealer.show_some()
            while player_turn:
                player_wants_hit = self.will_player_hit()
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
        if self.game_on:
            while not dealer_limit_reached:
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

        player_quit = not self.game_on and player_turn
        if not player_quit and self.ask_for_replay():
            self.reset_for_replay()
            self.run(replay=True)
        else:
            print('\nThanks for playing!\n')

    def will_player_play(self):
        valid_choice = False
        print("\nYou've got to pay to play\n")
        while not valid_choice:
            choice = input('Are you buying in? (y or n)  ')
            if choice != 'y' and choice != 'n':
                print('\nPlease enter either "y" or "n"\n')
            else:
                valid_choice = True
        return choice == 'y'

    def ask_for_buy_in(self):
        valid_choice = False
        while not valid_choice:
            try:
                buy_in = int(input("\nWhat's your buy in?  "))
                self.player.buy_in(buy_in)
                valid_choice = True
            except:
                print('\nYou must provide a number')

    def ask_for_bet(self):
        valid_choice = False
        while not valid_choice:
            try:
                bet = int(input("\nWhat's your bet?  "))
                self.player.place_bet(bet)
                if self.player.is_bet_valid():
                    valid_choice = True
                else:
                    print("\nThat's not a valid bet.")
                    print("Bets cannot be more than you can cover and cannot be 0.")
                    self.player.reset_bet()
            except:
                print('\nYou must provide a number')

    def ask_for_replay(self):
        valid_choice = False
        while not valid_choice:
            replay = input('\nPlay again? (y or n)  ')
            if replay != 'y' and replay != 'n':
                print('Please enter either a "y" or "n"')
            else:
                valid_choice = True
        return replay == 'y'

    def reset_for_replay(self):
        self.game_on = True
        self.deck = Deck()
        self.player.reset_hand()
        self.dealer.reset_hand()

    def will_player_hit(self):
        valid_choice = False
        while not valid_choice:
            choice = input('Would you like to hit? (y or n)  ')
            if choice != 'y' and choice != 'n':
                print('\nPlease enter either "y" or "n"\n')
            else:
                print('\n')
                valid_choice = True
        return choice == 'y'

    def declare_winner(self, winner):
        self.game_on = False
        print('\n****************\n')
        print('Final Hands:\n')
        self.dealer.show_all()
        self.player.show_all()
        print('Final Scores:\n')
        print(f'Dealer: {self.dealer.get_score()}')
        print(f'Player: {self.player.get_score()}\n')
        print(f'{winner} has won!')

    def player_win(self):
        self.declare_winner('Player')
        self.player.win_bet()

    def dealer_win(self):
        self.declare_winner('Dealer')
        self.player.lose_bet()
