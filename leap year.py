#code to determine whether year is a leap year
#year input
year = (int(input("Enter a year:")))
#code for leap year
if year % 4 == 0  and year % 100 != 0:
    print("Your year is a leap year")
elif year % 400 == 0:
    print("Your year is a leap year")
else:
    print("Your year is not a leap year")

