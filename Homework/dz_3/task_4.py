#Напишем рекурсивную функцию, которая вычисляет сумму цифр числа.

def sum_of_digits(n: int) -> int:
    if n < 10:  #Если число n меньше 10, то возвращается оно же, так как сумма цифр такого числа равна самому числу.
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)  #Если число n больше или равно 10, то суммируется остаток от деления числа n на 10 и результат вызова функции sum_of_digits от целочисленного деления n на 10. Таким образом, мы суммируем последнюю цифру числа n с результатом вычисления суммы цифр оставшейся части числа.


def test_sum_of_digits():
    assert sum_of_digits(654) == 15
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")

test_sum_of_digits()