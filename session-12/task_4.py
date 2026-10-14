
products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

filter_arr = list(filter(lambda n: n.lower()[0] == "m",products))
print(filter_arr)
