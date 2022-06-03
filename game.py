import random
from art import rules, rock, paper, scissors, lizard, spock
import time
import os
from utils import check_results
from players import get_choice


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
            self.players = get_choice(self.players, self.rounds_played)
            self.round_winner = check_results(self.players, self.ai_player)
            clear()
            
            self.display_results()
            self.add_win()
            self.player_reset()
 
            for player in self.players:
                if player.wins > 1:
                    self.winner = player.name
                    self.game_over = True        
               
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
            print('This round was a tie! Let\'s go again')
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
