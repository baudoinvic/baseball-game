import random

teams = []

class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def display_info(self):
        print(f"{self.name}: offensive power: {self.attack} / defensive power: {self.defense}")

def create_teams():
    global teams
    team1 = Team('Attackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]
    return teams

def play():
    print('Debug: play()')
    teams = create_teams()
    print("Information of all teams")
    for i, team in enumerate(teams, 1):
        print(f"{i}")
        team.display_info()
    user_team_index = int(input("Select your team (1-3): ")) - 1
    user_team = teams[user_team_index]
    print(f"Your team is '{user_team.name}'")
    opponent_team_index = int(input("Select opponent’s team (1-3): ")) - 1
    opponent_team = teams[opponent_team_index]
    print(f"Opponent’s team is '{opponent_team.name}'")
    print('Debug: top of 1', user_team_index)
    print('Debug: bottom of 1', opponent_team_index)
    print('Debug: top of 2', user_team.attack)
    print('Debug: bottom of 2', opponent_team.defense)
    print('Debug: top of 3', user_team.defense)
    print('Debug: bottom of 3', opponent_team.attack)
    print('Debug: top of 4', user_team.attack + opponent_team.defense)
    print('Debug: bottom of 4', opponent_team.attack + user_team.defense)
    print('Debug: top of 5', user_team.attack + opponent_team.defense - opponent_team.attack)
    print('Debug: bottom of 5', opponent_team.attack + user_team.defense - user_team.attack)
    print('Debug: top of 6', (user_team.attack + opponent_team.defense - opponent_team.attack) )
    print('Debug: bottom of 6', (opponent_team.attack + user_team.defense - user_team.attack) )
    print('Debug: top of 7',)
    print('Debug: bottom of 7', )
    print('Debug: top of 8', (user_team.attack + opponent_team.defense - opponent_team.attack) )
    print('Debug: bottom of 8', (opponent_team.attack + user_team.defense - user_team.attack) )
    print('Debug: top of 9', (user_team.attack + opponent_team.defense - opponent_team.attack)  > (opponent_team.attack + user_team.defense - user_team.attack) / 10 + random.uniform(-0.5, 0.5))

play()
