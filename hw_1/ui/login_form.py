# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(300, 170)
        widget.setMinimumSize(QSize(300, 170))
        widget.setMaximumSize(QSize(350, 200))
        self.verticalLayout = QVBoxLayout(widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 10))
        self.label.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_login = QLineEdit(widget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.lineEdit_login)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 10))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_password = QLineEdit(widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(100, 35))
        self.pushButton.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("widget", u"Login", None))
        self.lineEdit_login.setText("")
        self.label_2.setText(QCoreApplication.translate("widget", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

