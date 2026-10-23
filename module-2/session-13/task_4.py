
matrix = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]
rating = [j for inner in matrix for j in inner if j>4]

print(rating)

