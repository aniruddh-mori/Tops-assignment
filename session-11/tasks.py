
# Task -1
my_playlist = {
    "Barsaat" : 3.05,
    "Vaaroon" : 4.12,
    "Yodha" : 4.34
}
print("Original Dictionary : ",my_playlist)

# Task -2
my_playlist["LAAVAN"] = 3.06
my_playlist["Barsaat"] = 3.30

# Task -3
def display_friends(user_dict):
    for key,val in user_dict.items():
        print(f"{key}: {val} followers")
display_friends({"mori_ani_777": "2.3K", "jadav_nimesh":"1.4K","sonagra_hardik_132":"5.1K"})

# Task -4
food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

# a) all food items
print("Food items",food_order.keys())

# b) all item quantities 
print("Food Quntity",food_order.values())

# c) each item
print("Food items",food_order.items())

# Task -5
info = {
    "watch":2
}
def update_cart(cart, item, qty):
    qty = cart.get(item,0) + qty
    cart.update({item : qty})
    return cart

item = input("Enter item which you want to add : ").lower()
qty = int(input("Enter the Number of Quntity : "))
print(update_cart(info,item,qty))

