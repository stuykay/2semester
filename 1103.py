from functools import reduce
NUMBERS = [5, 12, 7, 20, 3, 18, 2, 15, 9, 30, 11, 6]

def greater_than_ten(numbers):
    for i in numbers:
        if i > 10:
            yield i

def square_numbers(numbers):
    for i in numbers:
        yield i**2

# print(list())
print(list(filter(lambda x: x%2==0, NUMBERS)))
print(list(map(lambda x: f'value={x}', NUMBERS)))
print(reduce(lambda x, y: x + y, NUMBERS))
print(reduce(lambda x, y: max(x, y), NUMBERS))

# Написать генератор, который возвращает первые n чисел кратных трем
def multiples_of_three(n):
    for i in range(0, 3*n, 3):
        yield i

# Написать генератор, который возвращает слова строки по одному
def word_generator(text):
    text = text.split(' ')
    for w in text:
        yield w

# Обработать текст: оставить слова длиной > 4, затем преобразовать все слова в верхний регистр
text =  'abcde guys what americans are about, pepe coco shneine'

def text_wrapper(text: str):
    text = text.split(' ')
    text = list(filter(lambda x: len(x) > 4, text))
    text = list(map(lambda x: x.upper(), text))
    return text

print(list(text_wrapper(text)))