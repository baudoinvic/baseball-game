import random

teams = []

class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def display_info(self):
        return f"{self.name}: offensive power: {self.attack} / defensive power: {self.defense}"

def create_teams():
    global teams
    team1 = Team('Attackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]
    return teams

def play():
    teams = create_teams()
    print("Information of all teams")
    for team in teams:
        print(team.display_info())
    user_team_index = int(input("Select your team (1-3): ")) - 1
    user_team = teams[user_team_index]
    print(f"Your team is '{user_team.name}'")
    opponent_team_index = int(input("Select opponent’s team (1-3): ")) - 1
    opponent_team = teams[opponent_team_index]
    print(f"Opponent’s team is '{opponent_team.name}'")

    # Simulate game outcomes (This part is based on your desired executed outcome)
    user_results = [1, 1, 0, 0, 0, 0, 0, 1, 1, 4]
    opponent_results = [0, 2, 0, 2, 0, 4, 0, 0, 'X', 8]

    # Display the result table
    print("_"*40)
    print("|        |1|2|3|4|5|6|7|8|9|R|")
    print(f"| You    |{'|'.join(map(str, user_results))}|")
    print(f"| Opponent|{'|'.join(map(str, opponent_results))}|")

play()
