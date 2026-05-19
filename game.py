import random
from collections import defaultdict


class Game:
    def __init__(self, state: int = 1):
        self.players = []
        self.state = state
        self.action_at_night: dict[str, bool] = {}

    def add_player(self, player_object):
        self.players.append(player_object)

    def show_alive_players(self):
        for player in self.players:
            print(f"{player.name} is {'alive' if player.life else 'Dead'}")

    def start_game(self):
        print("The game has started")
        return self.show_alive_players()

    def assign_roles(self):
        roles = {Villager: 4, Mafia: 1, Doctor: 1}

        final_roles = []

        for role, times in roles.items():
            final_roles.extend([role] * times)

        random.shuffle(final_roles)

        for i in range(len(final_roles)):
            self.players[i] = final_roles[i](self.players[i].name)
        return self.overview()

    def overview(self):
        for player in self.players:
            print(f"{player.name} is {player.role}")

    def night_phase(self):

        events = defaultdict(list)
        for player in [x for x in self.players if x.life]:
            result = player.perform_night_action(self)
            if result is not None:
                events[result[0]].append(result[1])

        for name, actions in events.items():
            if "Kill" in actions and "Save" not in actions:
                name.die()
                self.action_at_night[name] = True

            elif "Kill" in actions and "Save" in actions:
                self.action_at_night[name] = False

    def day_phase(self):
        for person, action in self.action_at_night.items():
            if action:
                print(f"{person.name} was killed during the night")
            else:
                print("an attempt was made but got save by the doctor")

        print("now lets continue for voting")

    def conducting_vote(self):
        voting_status: dict[str, int] = defaultdict(int)
        for player in [x for x in self.players if x.life]:
            vote = random.choice(
                [x for x in self.players if x != player and player.life],
            )
            player.vote(vote)
            voting_status[vote] += 1

        voted_on = max(voting_status, key=voting_status.get)
        voted_on.die()
        print(f" the town has voted to excute {voted_on.name}")

    def next_round(self):
        self.players = [player for player in self.players if player.life]
        self.state += 1
        self.action_at_night.clear()
        self.show_alive_players()


class Player:
    def __init__(self, name, role=None):
        self.name = name
        self.role = role
        self.life = True

    def show_role(self):
        print(f"you are {self.role}")

    def vote(self, target_player):
        print(f"{self.name} voted for {target_player.name}")

    def die(self):
        self.life = False

    def perform_night_action(self, game_session):
        pass


class Villager(Player):
    def __init__(self, name, role="Villager"):
        super().__init__(name, role)


class Mafia(Player):
    def __init__(self, name, role="Mafia"):
        super().__init__(name, role)

    def perform_night_action(self, game_session):
        print(f"{self.name} please choose who to kill")
        target = random.choice(
            [x for x in game_session.players if x != self and x.life],
        )
        return (target, "Kill")


class Doctor(Player):
    def __init__(self, name, role="Doctor"):
        super().__init__(name, role)

    def perform_night_action(self, game_session):
        print(f"{self.name} please choose who to Save")
        target = random.choice(
            [x for x in game_session.players if x != self and x.life],
        )
        return (target, "Save")


player_1 = Player("john")
player_2 = Player("Mary")
player_3 = Player("James")
player_4 = Player("David")
player_5 = Player("Sarah")
player_6 = Player("Michael")

my_game = Game()

my_game.add_player(player_1)
my_game.add_player(player_2)
my_game.add_player(player_3)
my_game.add_player(player_4)
my_game.add_player(player_5)
my_game.add_player(player_6)


my_game.start_game()
print("--" * 20)
my_game.assign_roles()
print("--" * 20)
my_game.night_phase()
print("--" * 20)
my_game.show_alive_players()
print("--" * 20)

my_game.day_phase()
print("--" * 20)

my_game.conducting_vote()
print("--" * 20)

my_game.next_round()
print("--" * 20)

my_game.night_phase()
print("--" * 20)

my_game.show_alive_players()
print("--" * 20)

my_game.day_phase()
print("--" * 20)

my_game.conducting_vote()
print("--" * 20)
