#code to show largest of 3 numbers entered by user
num_1 = (int(input("Enter a number:")))
num_2 = (int(input("Enter a second number:")))
num_3 = (int(input("Enter a third number:")))

#process
if num_1 > num_2 and num_1 > num_3:
    largest = num_1
elif num_2 > num_2 and num_2 > num_3:
    largest = num_2
else:
    largest = num_3

#Output
print("The largest number is:", largest)
