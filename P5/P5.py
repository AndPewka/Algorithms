import os
from random import randint
from time import time
import random
count = 100000
os.system("cls")

a = []
for i in range(count):
    a.append(randint(-100,100))

def bubble(b):
	a = b.copy()
	for i in range(len(a)):
		for j in range(i):
			if a[i] < a[j]:
				a[i],a[j] = a[j],a[i]
	return a


def quicksort(b):
    a = b.copy()
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in a:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)

def heapify(nums, heap_size, root_index):  
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(b): 
    a = b.copy() 
    n = len(a)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении, 
    # уменьшая счётчик i на 1 
    for i in range(n, -1, -1):
        heapify(a, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    
    return a


start_time = time()
sort = heap_sort(a)
end_time = time()
print("list sort by heap_sort for {} sec".format(end_time-start_time))

# start_time = time()
# sort = bubble(a)
# end_time = time()
# print("list sort by bubble for {} sec".format(end_time-start_time))

start_time = time()
sort = quicksort(a)
end_time = time()
print("list sort by quicksort for {} sec".format(end_time-start_time))



# start_time = time()
# sort = bubble(a)
# end_time = time()

# start_time = time()
# sort = bubble(a)
# end_time = time()





