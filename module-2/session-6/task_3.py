
teams = ["GT","RCB","RR","CSK","MI"]
points = [15,9,30,8,11]

dict_teams = dict(zip(teams,points))
for key,point in list(dict_teams.items()):
    if point < 10:
        del dict_teams[key]

print(dict_teams)



