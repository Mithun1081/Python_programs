name=input("enter the name:")
rollno=input("enter the rollno:")
tamil=int(input("enter tamil mark:"))
english=int(input("enter english mark:"))
maths=int(input("enter maths mark:"))
physics=int(input("enter physics mark:"))
chemistry=int(input("enter chemistry mark:"))
computer=int(input("enter computer mark:"))
avg=(tamil+english+maths+physics+chemistry+computer)/6
print("\t",name,"\t",rollno,"\t",avg)
#print("{:4.3f}".format(avg))