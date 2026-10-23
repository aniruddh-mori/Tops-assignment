

prices = [120, 250, 99, 180, 310]
charges = lambda charge: charge/10 + charge
result = list(map(charges,prices))
print(result)
