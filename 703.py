# Часть 1
# Task 1
class EvenIterator:
    def __init__(self, n):
        self.fin = n
        self.current = 2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.fin:
            raise StopIteration('Итератор закончил программу')
        else:
            value = self.current
            self.current += 2
            return value

for i in EvenIterator(21):
    print(i)

# Task 2
class ReverseList:
    def __init__(self, listik):
        self.listik = listik
        self.current = len(listik) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration('Итератор кончил работу')
        else:
            value = self.listik[self.current]
            self.current -= 1
            return value

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in ReverseList(l):
    print(i)

# Часть 2
import numpy as np

# Task 3
arr = np.array([3, 7, 1, 9, 4])
print(f'Максимальный элемент: {arr.max()}')
print(f'Среднее значение массива: {arr.mean()}')

# Task 4
arr = np.array([2, 8, 4, 10, 3])
res = np.where(arr > 5)
print(res)

# Task 5
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)

# Task 6
arr = np.array([1, 2, 3, 4])
print(3*arr)