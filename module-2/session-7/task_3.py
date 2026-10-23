

def word_freq_dict(text):
    text = text.lower().replace(",","").replace(".","").replace("!","").split()
    words = {}

    for i in text:
        if i in words:
            words[i] +=1
        else:
            words[i] = 1
    return words
print(word_freq_dict("Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"))
