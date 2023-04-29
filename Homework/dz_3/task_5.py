#Допустим, у нас есть два списка одинаковой длины,
# names и ages, содержащие соответственно имена и возрасты людей.
# Мы хотим создать новый список строк, в которых будут указаны имена и возрасты
# в формате "Имя - возраст". Напишите comprehension, который решает эту задачу

def create_name_age_strings(names: list, ages: list) -> list:
    return [f"{name} - {age}" for name, age in zip(names, ages)]
#функция create_name_age_strings() принимает два списка names и ages одинаковой длины,
# содержащих имена и возрасты людей соответственно. Функция создает новый список строк,
# в которых каждая строка содержит имя и возраст человека в формате "Имя - возраст".
# Для этого используется comprehension.
#Тест создает два тестовых случая. В первом случае, передаются непустые списки names и ages,
# а ожидаемый результат - список строк, каждая из которых содержит имя и возраст
# соответствующего человека.
# Во втором случае, передаются пустые списки, а ожидаемый результат - пустой список.
# Если функция работает правильно, то оба тестовых случая должны пройти.
# Функция zip() используется для объединения двух или более итерируемых объектов в кортежи
# путем параллельного итерирования.
def test_create_name_age_strings():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    expected = ["Alice - 25", "Bob - 30", "Charlie - 35"]
    result = create_name_age_strings(names, ages)
    assert result == expected

    names = []
    ages = []
    expected = []
    result = create_name_age_strings(names, ages)
    assert result == expected
    print("All test_create_name_age_strings pass")

test_create_name_age_strings()