"""
no=30
if no==1:
    print(no,"is not prime")
elif no>1:
    for i in range(2,no):
        if (no%i)==0:
            print(no,"not a prime")
        else:
            print(no,"is prime")
else:
    print(no,"is not prime")"""

"""
no=17
if no==1:
    print(no,"not prime")
elif no>1:
    for i in range(2,int(no/2)+1):
        if no%i==0:
            print(no,"not prime")
            break
    else:
            print(no,"is prime")
else:
    print(no,"not prime")"""


n=int(input("enter the number"))
flag=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("number",n,"is prime")
else:
    print("number",n,"is not prime")

