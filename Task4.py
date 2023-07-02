# 4.Создайте список из случайных чисел. Найдите второй максимум.

# a = [1, 2, 3] # Первый максимум == 3, второй == 2

import random 
list_1 = []
count = int(input('Введите кол-во элементов: '))
for i in range(count):
    number = random.randint(1, 10)
    list_1.append(number)
print(list_1)

max1 = 0
max2 = 0


for i in range(len(list_1)):
    if list_1[i] > max1:
        max1 = list_1[i]
    else:
        if list_1[i] > max2:
            max2 = list_1[i]
        
print(max2)