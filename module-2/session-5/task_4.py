
squad =  {
    'CSK':{'captain': 'Dhoni', 'players': 18},
    'MI': {'captain': 'Rohit', 'players': 17}
    }
squad["GT"] = {'captain': 'Hardik', 'players': 16}

for key,val in squad.items():
    print(key," = ",val["captain"])

