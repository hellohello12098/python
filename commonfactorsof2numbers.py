#program to show common factors between 2 numbers
first_number = int(input("Enter a number:"))
second_number = int(input("Enter a second number:"))

if first_number < second_number:
    smallest_value = first_number
else:
    smallest_value = second_number
for i in range(1, (smallest_value ) + 1):
    first_remainder = first_number % i
    second_remainder = second_number % i
    if first_remainder == 0 and second_remainder == 0:
        print(i)

