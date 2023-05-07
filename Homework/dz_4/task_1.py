class Student:
    # список для хранения всех студентов
    students = []

    #  инициализируем атрибуты объекта класса Student
    def __init__(self, first_name, last_name, course, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.gpa = gpa

        # добавляем текущего студента в список всех студентов
        self.students.append(self)

    # Метод класса для добавления студента в список всех студентов, с помощью метода append
    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

    # Метод экземпляра для изменения курса студента
    def change_course(self, new_course):
        self.course = new_course

    # Метод класса для вывода информации о всех студентах
    @classmethod
    def print_students(cls):
        seen_students = set()  # Множество для отслеживания уже выведенных студентов
        for student in cls.students:
            if student not in seen_students:
                print(
                    f"Имя: {student.first_name}, Фамилия: {student.last_name}, Курс: {student.course}, GPA: {student.gpa}")
                seen_students.add(student)

    # Метод класса для поиска студента по фамилии
    @classmethod
    def search_student(cls, last_name):
        for student in cls.students:
            if student.last_name == last_name:
                print(f"Студент найден: Имя: {student.first_name}, Фамилия: {student.last_name}, Курс: {student.course}, GPA: {student.gpa}")
                return

        print(f"Студент с фамилией {last_name} не найден.")

# создаем объекты студентов
student1 = Student("Иван", "Иванов", 3, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)

# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
Student.print_students()

# ищем студента по фамилии
Student.search_student("Петров")
