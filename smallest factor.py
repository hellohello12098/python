number = int(input("Enter a number:"))
smallest_num = 0
for i in range(2, number//2+1):
    remainder = number % i
    if remainder == 0:
        print("the smallest factor is", i)
        break

