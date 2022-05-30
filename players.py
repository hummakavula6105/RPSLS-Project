class Player:
    def __init__(self):
        self.name = ''
        self.wins = 0
        self.won_round = False
        self.choice = ''

    def get_name(self):
        return input('What is your player name?: ')


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'
