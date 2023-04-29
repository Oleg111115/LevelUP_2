# Написать программу, которая принимает на вход список чисел
# и с помощью декоратора выводит время выполнения функции,
# которая сортирует его по возрастанию.

import time
from typing import List

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()    #функция "wrapper" сохраняет текущее время в переменную "start_time", используя модуль "time"
        result = func(*args, **kwargs)#вызывает исходную функцию "func" (то есть, "sort_numbers") с переданными ей аргументами "args" и "kwargs" и сохраняет ее результат в переменную "result"
        end_time = time.time()    #сохраняет текущее время в переменную "end_time"
        print(f"Execution time: {end_time - start_time} seconds") #выводит время выполнения функции на экран, вычитая "end_time" из "start_time"
        return result
    return wrapper

@timer
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers
#Эта функция принимает список целых чисел numbers в качестве аргумента
# и сортирует его в порядке возрастания, используя метод sort().
# Затем функция возвращает отсортированный список.
def test_sort_numbers():
    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert sort_numbers([]) == []
    assert sort_numbers([1]) == [1]
    assert sort_numbers([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert sort_numbers([1, 2, 3, 4]) == [1, 2, 3, 4]
    print("All test_sort_numbers pass")

test_sort_numbers()