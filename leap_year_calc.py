year = int(input("Enter a year: "))

#
# Put your code here.
#
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
