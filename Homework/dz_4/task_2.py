class Calculator:
    def __init__(self):
        self.memory = [] # Инициализация списка для хранения значений в памяти калькулятора
        self.results = [] # Инициализация списка для хранения результатов операций
    #методы add, subtract, multiply и divide,
    # которые выполняют соответствующие операции над двумя числами
    # и сохраняют результат в списке results
    def add(self, a, b):
        result = a + b
        self.results.append(result)

    def subtract(self, a, b):
        result = a - b
        self.results.append(result)

    def multiply(self, a, b):
        result = a * b
        self.results.append(result)

    def divide(self, a, b):
        result = a / b
        self.results.append(result)

    def memorize_result(self):
        if self.results:# Проверка, есть ли результаты операций
            last_result = self.results[0:4]# Получение результатов из списка результатов
            self.memory.append(last_result)# Добавление последнего результата в список памяти

    def show_results(self):
        print("Results:", self.results)

    def show_memory(self):
        print("Memory:", self.memory)


# Создаем объект калькулятора
calc = Calculator()

# Выполняем операции
calc.add(11, 26)
calc.subtract(11, 26)
calc.multiply(11, 26)
calc.divide(11, 26)

# Сохраняем результат в память калькулятора
calc.memorize_result()

# Отображаем результаты операций
calc.show_results()

# Отображаем результат, сохраненный в памяти калькулятора
calc.show_memory()

