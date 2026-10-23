
restaurant_names = ['Burger Hub', 'Pizza Point', 'Sushi House']
deli_time = [30, 25, 40]

for restaurant,delivery in zip(restaurant_names,deli_time):
    print(restaurant,"-",delivery)
