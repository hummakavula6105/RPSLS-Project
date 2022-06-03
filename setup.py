from players import Computer, Player


class Setup:
    def __init__(self):
        self.players = []
        self.num_of_players = 0
        self.ai_player = False
        self.who_is_playing()
        self.create_players()

    def who_is_playing(self):
        computer_on = input('Do you want to play with a computer player? Y/N: ')
        if computer_on[0].upper() == 'Y': self.ai_player = True

        if self.ai_player:
            while self.num_of_players < 1 or self.num_of_players > 2:
                self.num_of_players = input('How many human players will there be? 1 or 2: ')
                if not self.num_of_players.isdigit():
                    self.num_of_players = 0
                else:
                    self.num_of_players = int(self.num_of_players)
        else:
            while self.num_of_players < 2 or self.num_of_players > 3:
                self.num_of_players = input('How many human players will there be? 2 or 3: ')
                if not self.num_of_players.isdigit():
                    self.num_of_players = 0
                else:
                    self.num_of_players = int(self.num_of_players)
        return

    def create_players(self):
        computer = Computer(self.ai_player)
        self.players.append(computer)

        for each in range(self.num_of_players):
            print(f'\nPlayer {each+1}:')
            player = Player()
            player.name = player.get_name()
            self.players.append(player)
        return
