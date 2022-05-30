import random
from art import rules, rock, paper, scissors, lizard, spock
import time
import os


def clear(): os.system('cls')


class Game:
    def __init__(self, players, ai_player):
        self.players = players
        self.ai_player = ai_player
        self.winner = ''
        self.round_winner = ''
        self.game_over = False
        self.rounds_played = 1
        self.play()

    def play(self):
        while not self.game_over:
            clear()
            self.get_choice()
            self.check_results()
            clear()
            self.display_results()
            self.add_win()
            self.player_reset()

            for player in self.players:
                if player.wins > 1:
                    self.winner = player.name
                    self.game_over = True

    def get_choice(self):
        for each in range(len(self.players)):
            if self.players[each].name == 'Computer':
                self.players[each].choice = random.randint(1, 5)
            else:
                print(f'\n--------Round {self.rounds_played}--------')
                rules()
                while self.players[each].choice == '':
                    self.players[each].choice = input('What action do you wish to take against your opponent?: ')
                    if not self.players[each].choice.isdigit():
                        self.players[each].choice = ''
                    else:
                        if int(self.players[each].choice) < 1 or int(self.players[each].choice) > 5:
                            self.players[each].choice = ''

                self.players[each].choice = int(self.players[each].choice)

            if self.players[each].choice == 1: self.players[each].choice = 'Rock'
            if self.players[each].choice == 2: self.players[each].choice = 'Paper'
            if self.players[each].choice == 3: self.players[each].choice = 'Scissors'
            if self.players[each].choice == 4: self.players[each].choice = 'Lizard'
            if self.players[each].choice == 5: self.players[each].choice = 'Spock'


    def check_results(self):
        rock_wins = ['Scissors', 'Lizard']
        rock_loses = ['Paper', 'Spock']
        paper_wins = ['Rock', 'Spock']
        paper_loses = ['Scissors', 'Lizard']
        scissors_wins = ['Paper', 'Lizard']
        scissors_loses = ['Rock', 'Spock']
        lizard_wins = ['Spock', 'Paper']
        lizard_loses = ['Rock', 'Scissors']
        spock_wins = ['Scissors', 'Rock']
        spock_loses = ['Paper', 'Lizard']

        while self.round_winner == '':
            if self.ai_player and len(self.players) < 3:
                if self.players[0].choice == 'Rock':
                    if self.players[1].choice in rock_wins: self.round_winner = self.players[0].name
                    if self.players[1].choice in rock_loses: self.round_winner = self.players[1].name
                if self.players[0].choice == 'Paper':
                    if self.players[1].choice in paper_wins: self.round_winner = self.players[0].name
                    if self.players[1].choice in paper_loses: self.round_winner = self.players[1].name
                if self.players[0].choice == 'Scissors':
                    if self.players[1].choice in scissors_wins: self.round_winner = self.players[0].name
                    if self.players[1].choice in scissors_loses: self.round_winner = self.players[1].name
                if self.players[0].choice == 'Lizard':
                    if self.players[1].choice in lizard_wins: self.round_winner = self.players[0].name
                    if self.players[1].choice in lizard_loses: self.round_winner = self.players[1].name
                if self.players[0].choice == 'Spock':
                    if self.players[1].choice in spock_wins: self.round_winner = self.players[0].name
                    if self.players[1].choice in spock_loses: self.round_winner = self.players[1].name

            if not self.ai_player and len(self.players) < 4:
                if self.players[1].choice == 'Rock':
                    if self.players[2].choice in rock_wins: self.round_winner = self.players[1].name
                    if self.players[2].choice in rock_loses: self.round_winner = self.players[2].name
                if self.players[1].choice == 'Paper':
                    if self.players[2].choice in paper_wins: self.round_winner = self.players[1].name
                    if self.players[2].choice in paper_loses: self.round_winner = self.players[2].name
                if self.players[1].choice == 'Scissors':
                    if self.players[2].choice in scissors_wins: self.round_winner = self.players[1].name
                    if self.players[2].choice in scissors_loses: self.round_winner = self.players[2].name
                if self.players[1].choice == 'Lizard':
                    if self.players[2].choice in lizard_wins: self.round_winner = self.players[1].name
                    if self.players[2].choice in lizard_loses: self.round_winner = self.players[2].name
                if self.players[1].choice == 'Spock':
                    if self.players[2].choice in spock_wins: self.round_winner = self.players[1].name
                    if self.players[2].choice in spock_loses: self.round_winner = self.players[2].name

            if self.round_winner == '': self.round_winner = 'Tie'

    def display_results(self):
        print('')

        for player in self.players:
            print(f'{player.name} chose {player.choice}')
            if player.choice == 'Rock': rock()
            if player.choice == 'Scissors': scissors()
            if player.choice == 'Paper': paper()
            if player.choice == 'Lizard': lizard()
            if player.choice == 'Spock': spock()

            time.sleep(2)
        if self.round_winner == 'Tie':
            print('This was a tie! Let\'s go again')
            time.sleep(3.5)
        else:
            print(f'\n{self.round_winner} won this round.')
            time.sleep(3.5)

        return

    def add_win(self):
        for player in self.players:
            if player.name == self.round_winner:
                player.wins += 1

        self.round_winner = ''
        return

    def player_reset(self):
        for player in self.players:
            player.choice = ''
        self.rounds_played += 1
