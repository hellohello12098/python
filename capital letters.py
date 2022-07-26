#program to print all capital letters in a string
#input
string = str(input("Enter string"))
#loop, process
for char in string :
    if (ord(char) >= 65 and ord(char) < 97):
        #output
        print(char)