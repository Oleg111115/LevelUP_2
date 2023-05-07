
class Phonebook:
    # список для хранения контактов
    contacts = []

    def __init__(self, name, phone_number):
        # инициализация атрибутов объекта
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def add_contact(cls, contact):
        # добавление контакта в список контактов класса
        cls.contacts.append(contact)

    @classmethod
    def remove_contact(cls, contact):
        # удаление контакта из списка контактов класса
        cls.contacts.remove(contact)

    def change_phone(self, new_phone_number):
        # изменение номера телефона контакта
        self.phone_number = new_phone_number

    @classmethod
    def print_contacts(cls):
        # вывод информации о всех контактах в телефонной книге
        if not cls.contacts:
            print("Телефонная книга пуста.")
        else:
            print("Контакты в телефонной книге:")
            for contact in cls.contacts:
                print(f"Имя: {contact.name}, Телефон: {contact.phone_number}")

    @classmethod
    def search_contact(cls, name):
        # поиск контакта по имени
        for contact in cls.contacts:
            if contact.name == name:
                print(f"Контакт найден: Имя: {contact.name}, Телефон: {contact.phone_number}")
                return
        print("Контакт не найден.")

    def __repr__(self):
        # возвращает строку, представляющую объект класса "Phonebook".
        return f"Phonebook({self.name}, {self.phone_number})"


# создаем объекты контактов
contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
Phonebook.add_contact(contact1)
Phonebook.add_contact(contact2)

# создаем и добавляем еще один контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact3)

# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()

# ищем контакт по имени
Phonebook.search_contact("Петр Петров")

# удаляем контакт
Phonebook.remove_contact(contact2)

# выводим информацию о всех контактах после удаления контакта
Phonebook.print_contacts()

