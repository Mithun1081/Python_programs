#1
i=1
while True:
    if i%3==0:
        break
    print(i)
    i+=1

#2
x=1
x<<2

#3
print(2**(3**2))
print((2**3)**2)
print(2**3**2)

#4
print(min(max(False,-3,-4), 2,7))

#5
x=56.2236
print("%.2f"%x)

#6
print(len(["hello",2,4,6]))

#7
x='abcd'
for i in x:
    print(i.upper())

#8
class tester:
    def __init__(self, id):
        self.id = str(id)

        id="224"
temp = tester(12)
print(temp.id)

#9
z=set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)

#10
list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

#11
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)

#12
x = 'abcd'
for i in range(len(x)):
    print(i)

#13
z=set('abc$de')
print('a' in z)
#print(z)