
def reverse_message(msg):
    newstr = ""
    for i in range(len(msg)-1,-1,-1):
        newstr+=msg[i]
    return newstr
print(reverse_message("Hello World"))
