
msgs = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']
for msg in msgs:
    if(msg == "How are you?"):
        print(msg)
        break
    elif not(msg == "Spam"):
            print(msg)
    continue
