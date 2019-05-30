# Instantiate the variable year to capture a year from the user
year = int(input("Enter a year: "))

# Evaluate the year on conditions related to leap years
# Print whether it's a leap year or a common year
# If it's outside the Gregorian calendar time, print a message to say that
if year > 1582:
    if year % 4 != 0:
        print("common year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 != 0:
        print("common year")
    else:
        print("leap year")
else:
    print("Not within the Gregorian calendar period")