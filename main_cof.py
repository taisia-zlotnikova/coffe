import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee.ui', self)
        self.connection = sqlite3.connect("coffee_db.sqlite")
        self.select_data()

    def select_data(self):
        res = self.connection.cursor().execute('SELECT * FROM coffee_tabl').fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())