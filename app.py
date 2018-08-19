'''
Make two random teams from a list of players
'''

from random import choice

players = [ 'Pollob', 'Imran', 'Tanji', 'Rima', 'Palash', 'Hira', 'Rafi', 'Shovon', 'Rafiq' ]

print("Players:", ', '.join(players))

teamA = []
teamB = []

def addToTeam(team):
    person = choice(players)
    team.append(person)
    players.remove(person)

while len(players) > 0:
    addToTeam(teamA)

    if len(players) == 0:
        break

    addToTeam(teamB)


print("Team A: ", ', '.join(teamA))
print("Team B: ", ', '.join(teamB))