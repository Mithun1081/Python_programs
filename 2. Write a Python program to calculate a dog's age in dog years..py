#2. Write a Python program to calculate a dog's age in dog years.
h_age=int(input("enter the dogs age in human years:"))
if h_age<0:
    print("enter only positive numbers")
    exit()
elif h_age<=2:
    d_age=h_age*10.5
else:
    d_age=21+(h_age-2)*4
print("the dog age in dog year's:",d_age)