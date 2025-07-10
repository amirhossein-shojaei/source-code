#Employee salary after deduction of taxes and insurance costs

salary = int(input('input your salary: '))
bime = (salary * 7) / 100
maliat = (salary * 10) / 100
daryafti = salary - (bime + maliat)
print('Bime is: ', bime, '\nmaliat is: ', maliat, '\ndaryafti is: ', daryafti)