#program to print average of integers entered
#variable decleration
entered_number = 1
total = 0
count = 0
#loop, process
while entered_number != 0:
    entered_number = int(input("Enter some numbers [0 to stop]:"))
    total = total + entered_number
    count = count + 1
average = total // (count - 1)
#output
print(average)




