# Написать программу, которая принимает на вход список чисел и возвращает список,
# содержащий только нечетные числа, умноженные на два.
# При этом, использовать функции filter, map и лямбда-функцию.

def get_odd_doubled_numbers(numbers: list) -> list:
    return list(map(lambda x: x*2, filter(lambda x: x % 2 != 0, numbers)))
#Эта функция принимает список чисел numbers и возвращает список,
# содержащий только нечетные числа, умноженные на два.
#Сначала с помощью filter() отбираются нечетные числа,
# а затем с помощью map() они умножаются на два. Результат возвращается в виде списка.
def test_get_odd_doubled_numbers():
    assert get_odd_doubled_numbers([1, 2, 3, 4, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([10, 20, 30]) == []
    assert get_odd_doubled_numbers([]) == []
    assert get_odd_doubled_numbers([1, 3, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([2, 4, 6]) == []
    print("All test_get_odd_doubled_numbers passed!")

test_get_odd_doubled_numbers()