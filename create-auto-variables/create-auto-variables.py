#Create as many variables as you want

list1 = [10 , 20 , 30 , 40 , 50 , 60]
dict1 = {}

for i in range(1 , len(list1)+1):
    number_name = f"num{i}"
    dict1[number_name] = list1[i-1]
print(dict1)