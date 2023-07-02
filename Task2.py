# 2.Создайте список из случайных чисел. 
# Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random 
list_1 = []
count = int(input('Введите кол-во элементов: '))
for i in range(count):
    number = random.randint(1, 1000)
    list_1.append(number)
print(list_1)
i = 1    
for i in range (len(list_1) - 1):
    if list_1[i-1] < list_1[i] > list_1[i+1]:
        max_local = list_1[i]
        i += 1
    else: 
        i += 1
print(max_local)