from PySide6 import QtWidgets
from ui.login_form import Ui_widget


DEBUG = True


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_widget()
        self.ui.setupUi(self)

        self.ui.lineEdit_login.setPlaceholderText('Введите логин')
        self.ui.lineEdit_password.setPlaceholderText('Введите пароль')

        if DEBUG:
            self.ui.lineEdit_login.setText('admin')
            self.ui.lineEdit_password.setText('123')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
