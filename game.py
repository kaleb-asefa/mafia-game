from statistics import mode
import random
from typing import Dict

class Game():
    action_at_night: Dict[str, bool] = {}
    def __init__(self, state:int=1):
        self.players = []
        self.state = state

    def add_player(self, player_object):
        self.players.append(player_object)

    def show_alive_players(self):
        for player in self.players:
                print(f'{player.name} is {'alive' if player.life else 'Dead'}')

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

    def night_phase(self):

        victims = []
        saves = []
        for player in [x for x in self.players if x.life]:
            if player.role == 'Mafia':
                print(f'{player.name} please choose who to kill')
                target = random.choice([x for x in self.players if x != player])
                victims.append(target)
                player.vote(target)

            elif player.role == 'Doctor':
                print(f'{player.name} please choose who to save')
                target = random.choice([x for x in self.players if x != player])
                saves.append(target)
                player.vote(target)
        
        for victim in victims:
            if victim not in saves:
                victim.die()
                Game.action_at_night[victim] = True

            elif victim in saves:
                Game.action_at_night[victim] = False

    def day_phase(self):
        for person, action in Game.action_at_night.items():
            if action:
                print(f'{person.name} was killed during the night')
            else:
                print('an attempt was made but got save by the doctor')

        print('now lets continue for voting')


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

my_game = Game()

my_game.add_player(pl1)
my_game.add_player(pl2)
my_game.add_player(pl3)
my_game.add_player(pl4)
my_game.add_player(pl5)
my_game.add_player(pl6)


my_game.start_game()

my_game.assign_roles()

my_game.night_phase()

my_game.show_alive_players()

my_game.day_phase()


