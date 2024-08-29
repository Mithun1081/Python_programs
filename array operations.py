import array as arr
a=arr.array('i',[1,2,3,4,5])
#append method
a.append(6)
for i in range(0,6):
    print(a[i],end=" ")
print()
#insert method
a.insert(3,7)
for i in range(0,7):
    print(a[i])

print()
#to print string
a=arr.array("u",["a","b"])
for i in range(0,2):
    print(a[i])


#string method
"""import array as arr
a= arr.array("u",["some","one"])
for i in range(0,2):
    print(a[i],end="")
print()"""
a=arr.array("u","hello")
print(a.tounicode())