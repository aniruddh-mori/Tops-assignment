
usernames = [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]

res = list(filter(lambda user:user[1]>1000,usernames))
kform = map(lambda user:(user[0],f"{user[1]/1000}K"),res)

for user in kform:
    print(user)
