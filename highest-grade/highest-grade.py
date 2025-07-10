#A student with the second highest GPA in terms of size

moadel_student = []
number_student = []
x = int(input('input tedad student: '))
for n in range(x + 1):
    if 0 < n:
        moadel_student.append(abs(float(input('input moadel: '))))
        number_student.append(input('input number student: '))
moadel_student.sort()
print('The second largest moadel: ',moadel_student[-2]) #دانشجویی که دومين معدل را ازنظر بزرگی دارد