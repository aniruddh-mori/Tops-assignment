
n1 = int(input("Enter a First Number : "))
n2 = int (input("Enter a second Number : "))

op = input("Enter an Operator for you want operation : ").strip()

if (op == "+"):
    print(f"Sum of {n1} and {n2} is {n1+n2}")
elif (op == "-"):
    print(f"Substract of {n1} and {n2} is {n1-n2}")
elif (op == "*"):
    print(f"Multiplication of {n1} and {n2} is {n1*n2}")
elif(op == "/"):
    print(f"division of {n1} and {n2} is {n1/n2}")
else:
    print("enters an invalid operator")