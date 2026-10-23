
msg = input("Enter a String : ").lower()
char = {}
for i in msg:
    if i in char:
        char[i] +=1
    else:
        char[i] = 1
print(char)
