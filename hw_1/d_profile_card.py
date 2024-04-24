from PySide6 import QtWidgets
from ui.profile_card import Ui_Form


DEBUG = True


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEditLastName.setPlaceholderText('Введите вашу фамилию')
        self.ui.lineEditFirstName.setPlaceholderText('Введите ваше имя')
        self.ui.lineEditMiddleName.setPlaceholderText('Введите ваше отчество')
        self.ui.lineEditPhoneNumber.setPlaceholderText('Введите ваш телефон')

        if DEBUG:
            self.ui.lineEditLastName.setText('Иванов')
            self.ui.lineEditFirstName.setText('Иван')
            self.ui.lineEditMiddleName.setText('Иванович')
            self.ui.lineEditPhoneNumber.setText('1234567890')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
