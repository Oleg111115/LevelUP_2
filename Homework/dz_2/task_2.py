
    
def calculate(expression):
    # Используем функцию eval для вычисления выражения
    # Библиотека eval в Python является встроенной функцией,
    # которая принимает выражение в виде строки и выполняет его как код Python.
    # Она может использоваться для вычисления математических выражений,
    # а также для выполнения других операций, таких как создание объектов, вызов функций и т.д.
    try:
        result = eval(expression)
    except:
        result = None

    return result

expression = '2+3*4-5/2'
result = calculate(expression)
print(result)

# assert calculate("2+3*4-5/2") == 11.5
# assert calculate("1+2+3+4+5") == 15
# assert calculate("10*5-7*3+2") == 31

# Отличное решение, рад что использовали функцию eval. И спасибо, заметили ошибку в тестах :-)
