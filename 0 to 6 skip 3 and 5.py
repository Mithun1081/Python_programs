#Prints values from 0 to 6 except 3
num = 0
for num in range(6):
 num = num + 1
 if num == 3:
  continue
 if   num==6:
     continue
 print('Num has value ' + str(num))
print('End of loop')