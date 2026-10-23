

values = [(3, 4), (5, 2),(7, 8)]
y = lambda a,b:(a+b,a*b)
res = list(map(lambda pair:(pair[0]+pair[1],pair[0]*pair[1]),values))
r = list(map(lambda pair:y(pair[0],pair[1]),values))
print(r)
