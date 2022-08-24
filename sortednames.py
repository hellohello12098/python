#program to accept names and sort them in names1.txt file
#create list and accept names
names = []
enteredname = input("Enter name: ")
#loop input until end
while enteredname != "end":
    names.append(enteredname)
    enteredname = input("Enter name: ")
#sort and create file
names.sort()
f = open(r"c:\python\Kavya\names1.txt","w")
for name in names:
    f.write(name + "\n")
f.close()
