#4. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
x=int(input("enter the side1:"))
y=int(input("enter the side2:"))
z=int(input("enter the side3:"))

if x==y==z:
    print("equilateral triangle")
elif x==y or x==z or y==z:
    print(" isosceles triangle")
else:
    print("scalene triangle")