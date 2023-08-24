'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''

n = int(input('Введите колличество монет: '))

count_orel = 0
count_reshka = 0

for i in range(n):
    m = int(input(f'Введите сторону {i + 1}-ой(ей) монетки: 1(Орел) или 0(Решка)'))
    if m == 1:
        count_orel += 1
    else:
        count_reshka += 1
if count_orel < count_reshka:
    print(f'Переверните {count_orel} монетки, с орла на решку')
elif count_reshka < count_orel:
    print(f'Переверните {count_reshka} монетки, с решки на орла')
else:
    print(f'Количество орлов и решек одинаково, по {count_orel} штуки')

