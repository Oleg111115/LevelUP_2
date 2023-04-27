def filter_strings(list_of_strings):
    result = []
    for string in list_of_strings:
        if string[0].isupper():
            result.append(string)
    return result

list_of_strings="Red", "green", "Blue"
res = filter_strings(list_of_strings)
print(res)

#Программа определяет функцию `filter_strings(list_of_strings)`,
# которая принимает на вход список строк `list_of_strings`.
# Внутри функции происходит пробег по списку строк, на каждой итерации проверяется,
# начинается ли строка с большой буквы (записанной латиницей).
# Если да, то строка добавляется в результирующий список `result`.
# В конце функция возвращает результирующий список.

#assert filter_capitalized_words(["Apple", "Banana", "cherry"]) == ["Apple", "Banana"]
#assert filter_capitalized_words(["Python", "java", "C++"]) == ["Python"]
#assert filter_capitalized_words(["Red", "green", "Blue"]) == ["Red", "Blue"]