from functools import reduce

prices = [120, 80, 150, 60]

sumarr = reduce(lambda pre,res: pre+res,prices)
print("Sum = ",sumarr)