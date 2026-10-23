
review = "I ordered from Swiggy yesterday and the food was absolutely delicious! The delivery guy was super fast, and everything arrived hot."
review = review.lower()
new_review = ""
words = {}
for i in review:
    if i == "." or i =="," or i == "!" or i =="'":
        continue
    new_review +=i 

review_arr = new_review.split()

for i in review_arr:
    if i in words:
        words[i] +=1
    else:
        words[i] = 1
print(words)
