n = 0
sum = 0
while n < 5:
    try:
        number = int(input("Enter a number: "))
        n += 1
        sum += number
    except ValueError:
        print("invalid")

print(sum)