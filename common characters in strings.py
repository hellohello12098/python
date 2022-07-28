string_1 = str(input("Enter a string:"))
string_2 = str(input("Enter another string:"))

for chr_1 in string_1:
    for chr_2 in string_2:
        if chr_1 == chr_2:
            print(chr_1)

