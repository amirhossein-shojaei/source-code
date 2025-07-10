#Fibonacci series

n = int(input('input the number: '))
while True:
    if n <= 1:
        print('This number is not true')
    if n == 1:
        print(1)
        break
    if n > 1:
        print(1)
    list1 = [1, 1]
    for i in range(n - 1):
        sum1 = list1[0] + list1[1]
        del list1[0]
        list1.append(sum1)
        print(list1[0]) # سری فيبوناچی
    break