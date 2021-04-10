import random

# описание массива в виде класса
class MyArray:
    arr = [ ]
    changed = False

# функция сравнения двух соседних элементов массива
def Work(arg):
    if arg[0].arr[arg[1]] > arg[0].arr[arg[1] + 1]: # сравнение текущего элемента с правым
        arg[0].arr[arg[1]], arg[0].arr[arg[1] + 1] = arg[0].arr[arg[1] + 1], arg[0].arr[arg[1]] # перестановка элементов
        arg[0].changed = True # установка флага, что массив изменен
    
N = 100 # размер массива

array = MyArray() # создание объекта
array.arr = [ random.randint(-N, N) for i in range(N) ] # генерация случайного массива

print('Исходный массив:')
print(array.arr)

niter = 0 # счетчик итераций
array.changed = True

# пока массив изменяется
while array.changed:
    array.changed = False
    
    for i in range(len(array.arr) - 1):
        Work([ array, i ])
        
    niter += 1 # увеличение счетчика итераций
    
print('Всего итераций: ' + str(niter))
print('Сортированный массив:')
print(array.arr)

input()
