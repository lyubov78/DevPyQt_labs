from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # TODO Вызовите метод для инициализации интерфейса
        self.initUi()


    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        labelLogin = QtWidgets.QLabel("Логин")  # Создайте виджет QLabel с текстом "Логин"
        labelRegistration = QtWidgets.QLabel("Регистрация")  # Создайте виджет QLabel с текстом "Регистрация"

        self.lineEditLogin = QtWidgets.QLineEdit()  # создайте виджет QLineEdit
        self.lineEditLogin.setPlaceholderText("Введите логин")  # добавьте placeholderText "Введите логин"
        self.lineEditPassword = QtWidgets.QLineEdit()  # создайте виджет QLineEdit
        self.lineEditPassword.setPlaceholderText("Введите пароль")  # добавьте placeholderText "Введите пароль"
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)  # установите ограничение видимости вводимых знаков

        self.pushButtonLogin = QtWidgets.QPushButton()  # создайте виджет QPushButton
        self.pushButtonLogin.setText("Войти")  # установите текст "Войти"

        self.pushButtonRegistration = QtWidgets.QPushButton()  # создайте виджет QPushButton
        self.pushButtonRegistration.setText("Регистрация")  # установите текст "Регистрация"

        layoutLogin = QtWidgets.QHBoxLayout()  # Создайте QHBoxLayout
        layoutLogin.addWidget(labelLogin)  # добавьте labelLogin
        layoutLogin.addWidget(self.lineEditLogin)  # добавьте self.lineEditLogin

        layoutPassword = QtWidgets.QHBoxLayout()  # Создайте QHBoxLayout
        layoutPassword.addWidget(labelRegistration)  # добавьте labelRegistration
        layoutPassword.addWidget(self.lineEditPassword)  # добавьте self.lineEditPassword

        layoutButtons = QtWidgets.QHBoxLayout()  # Создайте QHBoxLayout
        layoutButtons.addWidget(self.pushButtonLogin)  # добавьте self.pushButtonLogin
        layoutButtons.addWidget(self.pushButtonRegistration)  # добавьте self.pushButtonRegistration

        layoutMain = QtWidgets.QVBoxLayout()  # Создайте QVBoxLayout
        layoutMain.addLayout(layoutLogin)  # добавьте layoutLogin
        layoutMain.addLayout(layoutPassword)  # добавьте layoutPassword
        layoutMain.addLayout(layoutButtons)  # добавьте layoutButtons

        self.setLayout(layoutMain)  # установите layoutMain на основной виджет


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
