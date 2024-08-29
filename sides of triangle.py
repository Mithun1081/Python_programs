import cmath
s=int(input("side:"))
a=int(input("s1:"))
b=int(input("s2:"))
c=int(input("s3:"))
area_of_triangle=(s*(s-a)*(s-b)*(s-c))
s4=cmath.sqrt(area_of_triangle)
print(s4)
