entered_number = (int(input("Enter a number:")))
for range_number in range(2,entered_number//2+1):
    if entered_number%range_number== 0:
        print(range_number)
