

import math

bill_amount = float(input("Enter your Zomato bill amount: "))

discount = bill_amount * 0.10
final_bill = bill_amount - discount

final_bill = math.floor(final_bill)

print("Original Bill : ", bill_amount)
print("Discount (10%) : ", discount)
print("Final Bill Amount : ", final_bill)
