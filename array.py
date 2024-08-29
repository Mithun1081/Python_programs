import array as arr
a=arr.array('i',[1, 2, 3])
print("the new created array is=", end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print()


b=arr.array('d',[1.2, 2.0, 3.5])
print("the new created array is=", end=" ")
for i in range(0,3):
    print(b[i],end=" ")
print()