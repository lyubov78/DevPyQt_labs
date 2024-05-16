"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets
from b_systeminfo_widget import Window as WindowWidget
from c_weatherapi_widget import WindowWeather as WeatherWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.window = WindowWidget()
        self.weather_window = WeatherWidget()

        l_left = QtWidgets.QVBoxLayout()
        l_left.addWidget(self.window)
        l_left.addSpacerItem(QtWidgets.QSpacerItem(
            0, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        ))

        l_main = QtWidgets.QHBoxLayout()
        l_main.addLayout(l_left)
        l_main.addWidget(self.weather_window)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(l_main)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()
