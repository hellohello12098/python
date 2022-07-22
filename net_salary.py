#program for calculating net salary
#input basic salary
basic_salary = int(input("Enter net salary:"))
#calculate net salary
hra = basic_salary * 30/100
da = basic_salary * 20/100
net_salary = hra + da + basic_salary
#output
print("Net Salary:" , net_salary)