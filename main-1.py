from setup import Setup
from game import Game
from art import logo

print(logo)
print('\nWelcome to a sassy game of Rock, Paper, Scissors, Lizard, Spark! A virtual way to beat your opponents and have a chuckle!')

setup = Setup()

game = Game(setup.players, setup.ai_player)
print(f'\nCongratulations {game.winner}. You outsmarted your foes!')
