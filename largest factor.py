#program to show largest factor of a number
#input
number = int(input("Enter a number:"))
largest_factor = 0
#process
for i in range(1,number//2+1):
    remainder = number % i
    if remainder == 0:
      largest_factor = i
#output
print(largest_factor)





