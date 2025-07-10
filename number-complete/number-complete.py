#Is the input number complete?

while True:
    number = int(input('input the number: '))
    sum_number = 0
    for i in range(1,number):
        if (number % i) == 0:
            sum_number += i
    if number == sum_number: # عدد ورودی کامل است یا خیر
        print('this number is perfected')
    else:
        print('this number is not perfected')
    text = input('Are you want Continue:(y or n) ')
    if text == 'n' or text == 'N':
        break