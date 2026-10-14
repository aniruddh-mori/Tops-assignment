

# Task - 1
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')
print("Original Tuple : ",fav_apps)


# Task - 2
print("2nd app name : ",fav_apps[1])
print("4th app name : ",fav_apps[3])

# Task - 3
# fav_apps[0] = "YouTube"

# TypeError: 'tuple' object does not support item assignment
# explain: This error happens because Python tuples are IMMUTABLE. 
# Once a tuple is created, its elements cannot be changed, added, or removed. 


# Task - 4
print("Middle apps ; ",fav_apps[1:4])

# Task - 5
new_apps = ("Facebook","Amazon")
all_apps = fav_apps + new_apps
print("Merge Tuples : ",all_apps)
