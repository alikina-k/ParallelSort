# Параллельная сортировка методом чет-нечетной перестановки

import random
import threading
import multiprocessing.dummy

# описание массива в виде класса для использования в потоках по ссылке
class MyArray:
    arr = [ ]
    changed = False

# функция сравнения двух соседних элементов массива
def Work(arg):
    if arg[0].arr[arg[1]] > arg[0].arr[arg[1] + 1]: # сравнение текущего элемента с правым
        arg[0].arr[arg[1]], arg[0].arr[arg[1] + 1] = arg[0].arr[arg[1] + 1], arg[0].arr[arg[1]] # перестановка элементов
        arg[0].changed = True # установка флага, что массив изменен
    
N = 100 # размер массива
M = 4 # количество потоков

array = MyArray() # создание объекта
array.arr = [ random.randint(-N, N) for i in range(N) ] # генерация случайного массива

print('Исходный массив:')
print(array.arr)

niter = 0 # счетчик итераций
array.changed = True

# пока массив изменяется
while array.changed:
    pool = multiprocessing.dummy.Pool(M) # создание пула потоков
    array.changed = False
    # каждому потоку передается ссылка на объект массива и четный/нечетный индекс элемента в зависимости от итерации
    pool.map(Work, [ [ array, i * 2 + niter % 2 ] for i in range((N - niter % 2) // 2) ])
    pool.close()
    pool.join()
    niter += 1 # увеличение счетчика итераций
    
print('Всего итераций: ' + str(niter))
print('Сортированный массив:')
print(array.arr)

input()
