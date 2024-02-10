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

play()
