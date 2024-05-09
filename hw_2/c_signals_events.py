"""
Реализация программы проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets
from hw_2.ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonLT.clicked.connect(self.moveLeftTop)
        self.ui.pushButtonRT.clicked.connect(self.moveRightTop)
        self.ui.pushButtonCenter.clicked.connect(self.moveCenter)
        self.ui.pushButtonLB.clicked.connect(self.moveLeftBottom)
        self.ui.pushButtonRB.clicked.connect(self.moveRightBottom)
        self.ui.pushButtonMoveCoords.clicked.connect(self.moveByCoords)

        self.windowTitleChanged.connect(self.onWindowTitleChanged)
        self.windowStateChanged.connect(self.onWindowStateChanged)
        self.resized.connect(self.onWindowResized)
        self.moved.connect(self.onWindowMoved)

    def moveLeftTop(self):
        self.move(0, 0)

    def moveRightTop(self):
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.move(screen.width() - self.width(), 0)

    def moveCenter(self):
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        center_x = (screen.width() - self.width()) // 2
        center_y = (screen.height() - self.height()) // 2
        self.move(center_x, center_y)

    def moveLeftBottom(self):
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.move(0, screen.height() - self.height())

    def moveRightBottom(self):
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.move(screen.width() - self.width(), screen.height() - self.height())

    def moveByCoords(self):
        x = self.ui.spinBoxX.value()
        y = self.ui.spinBoxY.value()
        self.move(x, y)

    def onWindowTitleChanged(self, title):
        print(f"Заголовок окна изменен на: {title}")

    def onWindowStateChanged(self, state):
        print(f"Состояние окна изменено на: {state}")

    def onWindowResized(self):
        print(f"Размер окна изменен на: {self.size()}")

    def onWindowMoved(self):
        print(f"Окно перемещено в позицию: {self.pos()}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
