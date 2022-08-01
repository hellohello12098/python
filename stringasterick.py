#code to balance lists by using .
list1 = "abcdefghijklmnop"
list2 = "qrstuv"
#process, loop
difference = len(list1) - len(list2)
for i in range(1,difference+1):
    list2 = list2 + "."
for s1,s2 in zip(list1,list2):
#output
    print(s1,s2)
