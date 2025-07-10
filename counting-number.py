#Counting the number of fives in the range from one to a thousand

def formul(num):
    num1 = str(num)
    count = 0
    for i in range(len(num1)):
        if int(num1[i]) == 5:
            count += 1
    return count


count2 = 0
for i in range(1,56):
    count2 += formul(i)

print(count2)