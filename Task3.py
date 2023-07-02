# 3.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random 
list_1 = []
count = int(input('Введите кол-во элементов: '))
for i in range(count):
    number = random.randint(1, 10)
    list_1.append(number)
print(list_1)

list_1.sort()
t = 1
maxx_t = 1

for i in range(1, len(list_1)):
    if list_1[i] == list_1[i-1]:
        t += 1
    else:
        if t > maxx_t:
            maxx_t = t
        t = 1
    if t > maxx_t:
        maxx_t = t
print(maxx_t)