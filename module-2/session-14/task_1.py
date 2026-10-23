
shopping_cart = {}

users = int(input("Enter you want to add users : "))
for i in range(users):
    user = input("Enter a Username : ")
    shopping_cart[user] = {}
    items = int(input("Enter you want to Add Item : "))
    for j in range(items):
        name = (input("Enter the Product Name : "))
        price = int(input("Enter a Product price : "))
        qty = int(input("Enter a quantity of your product : "))
        shopping_cart[user][name] = {"price":price,"quntity":qty}
print(shopping_cart)

