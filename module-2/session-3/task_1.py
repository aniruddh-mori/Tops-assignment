
import math
scores = [56.7, 102.3, 88.9, 45.2, 120.8]

new_scores = []
for i in range(0,len(scores)):
    new_scores.append(round(scores[i]))

print("Original List of Score = ",scores)
print("rounded List of Score = ",new_scores)


