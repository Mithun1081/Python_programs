def sum_of_digits(number):
    sum_digits=0
    while number>0:
        digit=number%10
        sum_digits+=digit
        number//=10
    return sum_digits
number=125
print(sum_of_digits(number))