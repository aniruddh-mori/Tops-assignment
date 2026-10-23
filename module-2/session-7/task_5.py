
def char_count_dict(text):
    text = text.lower().replace(",","").replace(".","").replace("!","").replace(" ","")
    text = sorted(text)
    chars = {}
    # print(text)
    for i in text:
        if i in chars:
            chars[i] +=1
        else:
            chars[i] = 1
    return chars
print(char_count_dict("Hello World!!"))

