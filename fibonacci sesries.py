n=int(input())
fib1=0
print(fib1)
fib2=1
print(fib2)

for i in range(3,n+1):
    fib3 = fib1 + fib2
    print(fib3)
    fib1=fib2
    fib2=fib3
