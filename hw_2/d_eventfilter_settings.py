"""
Реализация программы взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from hw_2.ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Соединяем сигналы и слоты
        self.ui.dial.valueChanged.connect(self.update_values)
        self.ui.horizontalSlider.valueChanged.connect(self.update_values)

        # Настройка фильтра событий для QDial
        self.ui.dial.installEventFilter(self)

        # Загрузка сохраненных значений из QSettings
        self.load_settings()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress and source is self.ui.dial:
            if event.key() == QtCore.Qt.Key_Plus:
                self.ui.dial.setValue(self.ui.dial.value() + 1)
                print(f"Новое значение: {self.ui.dial.value()}")
                return True
            elif event.key() == QtCore.Qt.Key_Minus:
                self.ui.dial.setValue(self.ui.dial.value() - 1)
                print(f"Новое значение: {self.ui.value()}")
                return True
        return super().eventFilter(source, event)

    def update_values(self):
        sender = self.sender()
        if sender is self.ui.dial:
            self.ui.horizontalSlider.setValue(self.ui.dial.value())
        elif sender is self.ui.horizontalSlider:
            self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.dial.value())

    def load_settings(self):
        settings = QtCore.QSettings("A", "B")
        self.ui.comboBox.setCurrentIndex(settings.value("displayMode", 0))
        self.ui.lcdNumber.display(settings.value("value", 0))

    def closeEvent(self, event):
        settings = QtCore.QSettings("A", "B")
        settings.setValue("displayMode", self.ui.comboBox.currentIndex())
        settings.setValue("value", self.ui.lcdNumber.value())
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
