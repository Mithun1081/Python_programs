a=int(input())
b=int(input())
c=int(input())
if a < b and a < c:
    print(a,"is the smallest")
elif b < a and b < c:
    print(b,"is the smallest")
else:
    print(c,"is the smallest")