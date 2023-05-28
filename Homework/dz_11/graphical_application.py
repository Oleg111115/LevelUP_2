import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример приложения')
        self.init_ui()

    def init_ui(self):
        self.label_name = QLabel('Имя:')
        self.edit_name = QLineEdit()
        self.label_age = QLabel('Возраст:')
        self.edit_age = QLineEdit()
        self.button_save = QPushButton('Сохранить')
        self.button_load = QPushButton('Загрузить')

        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.edit_name)
        layout.addWidget(self.label_age)
        layout.addWidget(self.edit_age)
        layout.addWidget(self.button_save)
        layout.addWidget(self.button_load)

        self.setLayout(layout)

        self.button_save.clicked.connect(self.save_data)
        self.button_load.clicked.connect(self.load_data)

    def save_data(self):
        name = self.edit_name.text()
        age = self.edit_age.text()

        conn = QSqlDatabase.database()
        if not conn.open():
            print("Database Error: %s" % conn.lastError().databaseText())
            sys.exit(1)

        query = QSqlQuery()
        query.exec_("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")

        query.prepare("INSERT INTO users (name, age) VALUES (?, ?)")
        query.addBindValue(name)
        query.addBindValue(age)
        query.exec_()

        conn.close()

        self.edit_name.clear()
        self.edit_age.clear()

        QMessageBox.information(self, 'Успех', 'Данные успешно сохранены.')

    def load_data(self):
        conn = QSqlDatabase.database()
        if not conn.open():
            print("Database Error: %s" % conn.lastError().databaseText())
            sys.exit(1)

        query = QSqlQuery()
        query.exec_("SELECT * FROM users")

        data = []
        while query.next():
            name = query.value(0)
            age = query.value(1)
            data.append((name, age))

        conn.close()

        for row in data:
            print(row)

        QMessageBox.information(self, 'Загруженные данные', str(data))

if __name__ == '__main__':
    # Создание пустой базы данных SQLite в том же каталоге, где находится скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'data.db')
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName(db_path)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
