"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets, QtCore
from a_threads import SystemInfo


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.system_info_thread = SystemInfo()
        self.system_info_thread.systemInfoReceived.connect(self.update_system_info)

        self.delay_input = QtWidgets.QLineEdit()
        self.cpu_label = QtWidgets.QLabel()
        self.ram_label = QtWidgets.QLabel()

        self.delay_input.textChanged.connect(self.update_delay)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Время задержки:"))
        layout.addWidget(self.delay_input)
        layout.addWidget(QtWidgets.QLabel("Загрузка CPU:"))
        layout.addWidget(self.cpu_label)
        layout.addWidget(QtWidgets.QLabel("Загрузка RAM:"))
        layout.addWidget(self.ram_label)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.system_info_thread.start()

    def update_system_info(self, data):
        cpu_value, ram_value = data
        self.cpu_label.setText(f"CPU: {cpu_value}%")
        self.ram_label.setText(f"RAM: {ram_value}%")

    def update_delay(self, delay):
        try:
            delay = int(delay)
            self.system_info_thread.delay = delay
        except ValueError:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Window()
    window.show()

    app.exec()
