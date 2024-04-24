# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_card.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 200)
        Form.setMinimumSize(QSize(350, 150))
        Form.setMaximumSize(QSize(550, 200))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(80, 0))
        self.label_1.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label_1)

        self.lineEditLastName = QLineEdit(Form)
        self.lineEditLastName.setObjectName(u"lineEditLastName")
        self.lineEditLastName.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.lineEditLastName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditFirstName = QLineEdit(Form)
        self.lineEditFirstName.setObjectName(u"lineEditFirstName")
        self.lineEditFirstName.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.lineEditFirstName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditMiddleName = QLineEdit(Form)
        self.lineEditMiddleName.setObjectName(u"lineEditMiddleName")
        self.lineEditMiddleName.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.lineEditMiddleName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEditPhoneNumber = QLineEdit(Form)
        self.lineEditPhoneNumber.setObjectName(u"lineEditPhoneNumber")
        self.lineEditPhoneNumber.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.lineEditPhoneNumber)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"profile_card", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEditLastName.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.lineEditFirstName.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEditMiddleName.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEditPhoneNumber.setText("")
    # retranslateUi

