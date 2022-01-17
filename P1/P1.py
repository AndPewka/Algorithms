#Отсортировать элементы одномерного массива по возрастанию
from time import time
import os
from random import randint

os.system("cls")
def sort_1(b):
	a = b.copy()
	count = 0 
	for i in range(len(a)):
		for j in range(i):
			count += 1;
			if a[i] < a[j]:
				a[i],a[j] = a[j],a[i]
	print("sort_1 -- {}".format(count))
	return a


def sort_2(b):
	a = b.copy()
	swapped = True
	count = 0
	while swapped:
		swapped = False
		for i in range(len(a) - 1):
			count += 1
			if a[i] > a[i + 1]:
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True
	print("sort_2 -- {}".format(count))
	return a

a = []

for i in range(10):
	a.append(randint(0,10))
	

print(a)

start_time = time()
sort = sort_1(a)
print(sort)

end_time = time()
print("list sort by bubble_1 for {} sec".format(end_time-start_time))


print(a)
start_time = time()
sort = sort_2(a)
print(sort)
end_time = time()
print("list sort by bubble_2 for {} sec".format(end_time-start_time))















