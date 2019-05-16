income = float(input("Enter the annual income in thalers: "))

#
# Put your code here.
#
if income <= 85528:
    tax = income * .18 - 556.02
    if tax < 0: tax = 0
else:
    tax = (income - 85528) * .32 + 14839.02

tax = round(tax, 0)
print("The tax is:", tax, "thalers")