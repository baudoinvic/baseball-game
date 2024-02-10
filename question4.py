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

def play():
  print('Debug: play()')
  create_teams()
  print("Information of all teams")
  for i, team in enumerate(teams, 1):
    print(f"{i}\n", end="")
    team.display_info()

play()
