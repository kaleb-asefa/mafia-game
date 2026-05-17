from statistics import mode
import random

class Game():
    def __init__(self, state=1):
        self.players = []
        self.state = state

    def add_player(self, player_object):
        self.players.append(player_object)

    def show_alive_players(self):
        for player in self.players:
            if player.life:
                print(f'{player.name} is alive')

    def start_game(self):
        print('The game has started')
        return self.show_alive_players()
    
    def assign_roles(self):
        roles = { 'Villagers' : 4, 
                 'Mafia' : 1, 
                 'Doctor' : 1}
        
        final_roles = []
        
        for role, times in roles.items():
            final_roles.extend([role] * times)

        random.shuffle(final_roles)

        for i in range(len(final_roles)):
            self.players[i].role = final_roles[i] 
        return self.overview()
    
    def overview(self):
        for player in self.players:
            print(f'{player.name} is {player.role}')


class Player():
    def __init__(self, name, role=None, life=True):
        self.name = name
        self.role = role
        self.life = life

    def show_role(self):
        print(f'you are {self.role}')
    
    def vote(self, target_player):
        print(f"{self.name} voted for {target_player.name}")

    def die(self):
        self.life = False


pl1 = Player('pl1')
pl2 = Player('pl2')
pl3 = Player('pl3')
pl4 = Player('pl4')
pl5 = Player('pl5')
pl6 = Player('pl6')

