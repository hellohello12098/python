#code to balance both lists by printing asterisks
list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11]
#process, loops
difference = len(list1) - len(list2)
for i in range(1,difference+1):
    list2.append("*")
for g,v in zip(list1,list2):
#output
    print(g,v)