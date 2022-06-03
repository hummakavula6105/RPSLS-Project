
import random
from art import rules
from utils import validate_int_input

class Player:
    def __init__(self):
        self.name = ''
        self.wins = 0
        self.won_round = False
        self.choice = ''
        self.human = True

    def get_name(self):
        return input('What is your player name?: ')
    
    
class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = input('What name do you wish the computer to have?: ')
        self.human = False
        
class Human(Player):
    def __init__(self):
        super().__init__()


def get_choice(players, rounds_played):
    for each in range(len(players)):
        if not players[each].human:
            players[each].choice = random.randint(1, 5)
        else:
            print(f'\n----Round {rounds_played}   Player {each}----')
            rules()
            players[each].choice = validate_int_input('What action do you wish to take against your opponent?: ')

        if players[each].choice == 1: players[each].choice = 'Rock'
        if players[each].choice == 2: players[each].choice = 'Paper'
        if players[each].choice == 3: players[each].choice = 'Scissors'
        if players[each].choice == 4: players[each].choice = 'Lizard'
        if players[each].choice == 5: players[each].choice = 'Spock'

    return players