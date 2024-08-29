def find_largest(a,b,c):
    largest=a
    if b>largest:
        largest=b
    if c>largest:
        largest=c
    return largest

a=10
b=20
c=30
largest_number=find_largest(a,b,c)
print("the largest number is",largest_number)