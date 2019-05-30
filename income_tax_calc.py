#Instantiate the income variable to capture the user's annual income
income = float(input("Enter the annual income in thalers: "))

# Evaluate income tax to find the level it should be taxed
# Calculate the tax based on the income level
# Print the tax owed for the user
if income <= 85528:
    tax = income * .18 - 556.02
    if tax < 0: tax = 0
else:
    tax = (income - 85528) * .32 + 14839.02

tax = round(tax, 0)
print("The tax is:", tax, "thalers")