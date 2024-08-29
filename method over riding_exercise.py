a=int(input("enter area:"))
l=int(input("enter length:"))
b=int(input("enter breadth:"))

class polygon:
    def getarea(self):
        pass
class square(polygon):
    def getarea(self):
        return a*a
class rectangle(polygon):
    def getarea(self):
        return l*b

s=polygon()
s1=square()
s2=rectangle()
print("area of polygon:",s.getarea())
print("area of square:",s1.getarea())
print("area of rectangle:",s2.getarea())

