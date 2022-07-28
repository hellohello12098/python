string = str(input("Enter a string: "))
prevposition = 0
counter1 = 0
for chr in string:
    counter1 += 1
    if chr == " ":
        print(string[prevposition:counter1])
        prevposition = counter1
print(string[prevposition:counter1])