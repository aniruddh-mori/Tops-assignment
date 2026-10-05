


age = int(input("Enter a Age : "))

if (age>=18):
    time = int(input("Enter a Time according to 24 hours : "))
    if (time>=22 or time<=2):
        print("Order Allowed")
    else:
        print("Order Not Allowed")
else:
    print("Order Not Allowed")
