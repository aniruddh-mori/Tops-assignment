

ipl_scores = {}

teams = int(input("Enter number of teams: "))

for i in range(teams):
    team = input("Enter team name: ")
    ipl_scores[team] = {}

    players = int(input("Enter number of players: "))

    for j in range(players):
        name = input("Enter player name: ")
        runs = int(input("Enter runs scored: "))

        ipl_scores[team][name] = runs

print("\nIPL Scores:")
print(ipl_scores)

team_name = input("\nEnter team name to check: ")
player_name = input("Enter player name to check: ")

if team_name in ipl_scores and player_name in ipl_scores[team_name]:
    print(player_name, "scored", ipl_scores[team_name][player_name], "runs")
else:
    print("Team or player not found.")
