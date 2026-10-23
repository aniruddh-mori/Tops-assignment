
text = "the cat and the dog is in a garden of the house. and cat is abnoramly better."
stopwords = ['the', 'and', 'in', 'of', 'a', 'to', 'is']

words = text.lower().replace(",","").replace(".","").split()

filtered_words = []
char = {}
for word in words:
    if word not in stopwords:
        filtered_words.append(word)
 
for word in filtered_words:
    if word in char:
        char[word] +=1
    else:
        char[word] =1
print(char)
