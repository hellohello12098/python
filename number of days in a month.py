#code to decide how many days are in a month
month = int(input("Enter month number"))
#month has 31 days
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Your month has 31 days")
#month has 30 days
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Your month has 30 days")
#month has 28 days
elif month == 2:
    print("Your month has 28 days")
#invalid month
else:
    print("Invalid")