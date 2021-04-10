import random

# описание массива в виде класса
class MyArray:
    arr = [ ]

N = 100 # размер массива

array = MyArray() # создание объекта
array.arr = [ random.randint(-N, N) for i in range(N) ] # генерация случайного массива

print('Исходный массив:')
print(array.arr)

array.arr.sort()

print('Сортированный массив:')
print(array.arr)

input()
