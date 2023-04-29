def get_unique_words(string, stop_symbols=''):
    # создаем пустой список для уникальных слов
    unique_words = []

    # разбиваем строку на список слов
    words = string.split()

    # проходим циклом по каждому слову и добавляем его в список
    # уникальных слов, если оно еще не было добавлено
    for word in words:
        # удаляем знаки препинания из слова
        for char in stop_symbols:
            word = word.replace(char, '')
        # добавляем слово в список уникальных слов, если оно еще не было добавлено
        if word not in unique_words:
            unique_words.append(word)

    return unique_words


string = "apple apple banana cherry"
stop_symbols = r'.,!?;:()[]{}<>'
unique_words = get_unique_words(string, stop_symbols)
print(unique_words)

# assert unique_words("hello world") == ["hello", "world"]
# assert unique_words("apple apple banana cherry") == ["apple", "banana", "cherry"]
# assert unique_words("Python is great, isn't it?") == ["Python", "is", "great", "isn't", "it"]