"""
5. Write a Python program to create the multiplication table (from 1 to 10) of a number.
Expected Output:

Input a number: 6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24     """
n=int(input("enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)