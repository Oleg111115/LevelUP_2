a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = 0

if a > 0:
    for i in range(a):
        result += b
else:
    for i in range(abs(a)):
        result -= b

print("Результат умножения: ", result)



# C помощью цикла for суммируем число b a раз,
# если а положительное,
# или вычитаем число b абсолютное значение a раз,
# если а отрицательное.

# assert multiply(2, 3) == 6
# assert multiply(10, 5) == 50
# assert multiply(7, -3) == -21