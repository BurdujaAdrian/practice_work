# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(990, 882)
        font = QFont()
        font.setFamilies([u"Myanmar Khyay"])
        font.setPointSize(20)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color:\"#D9D9D9\";\n"
"font-family: Myanmar Khyay;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMaximumSize(QSize(50, 820))
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: \"#FFFFFF\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    height: 35px;\n"
"    border: none;\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color:\"#F5FAFE\";\n"
"color:\"#1F95EF\";\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMinimumSize(QSize(25, 25))
        self.pushButton_8.setMaximumSize(QSize(30, 28))
        icon = QIcon()
        icon.addFile(u"../../../../Users/foral/Desktop/QTUI/back 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(20, 20))
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 30))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setSizeIncrement(QSize(100, 100))
        icon1 = QIcon()
        icon1.addFile(u"Images/Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(45, 45))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.search_1 = QPushButton(self.widget)
        self.search_1.setObjectName(u"search_1")
        font1 = QFont()
        font1.setFamilies([u"Myanmar Khyay"])
        font1.setPointSize(15)
        self.search_1.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"Images/search-interface-symbol.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_1.setIcon(icon2)
        self.search_1.setIconSize(QSize(30, 30))
        self.search_1.setCheckable(True)
        self.search_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.search_1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.classes_1 = QPushButton(self.widget)
        self.classes_1.setObjectName(u"classes_1")
        icon3 = QIcon()
        icon3.addFile(u"Images/student_17584468.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.classes_1.setIcon(icon3)
        self.classes_1.setIconSize(QSize(30, 30))
        self.classes_1.setCheckable(True)
        self.classes_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.classes_1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.setting_1 = QPushButton(self.widget)
        self.setting_1.setObjectName(u"setting_1")
        icon4 = QIcon()
        icon4.addFile(u"Images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_1.setIcon(icon4)
        self.setting_1.setIconSize(QSize(25, 25))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(28, 400, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setMaximumSize(QSize(20, 20))
        self.label_3.setPixmap(QPixmap(u"../../../../Users/foral/Desktop/QTUI/Images/Group 91.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_9 = QSpacerItem(15, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.widget_3.setMaximumSize(QSize(130, 820))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"    background-color: \"#FFFFFF\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: black;\n"
"    height: 35px;\n"
"    border: none;\n"
"    padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color:\"#F5FAFE\";\n"
"color:\"#1F95EF\";\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pushButton_9 = QPushButton(self.widget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setMinimumSize(QSize(25, 25))
        self.pushButton_9.setMaximumSize(QSize(30, 28))
        icon5 = QIcon()
        icon5.addFile(u"../../../../Users/foral/Desktop/QTUI/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.pushButton_9.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.horizontalSpacer_6 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 70))
        self.pushButton.setMaximumSize(QSize(120, 70))
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(80, 70))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.search_2 = QPushButton(self.widget_3)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setFont(font1)
        self.search_2.setIcon(icon2)
        self.search_2.setIconSize(QSize(25, 25))
        self.search_2.setCheckable(True)
        self.search_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.search_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.classes_2 = QPushButton(self.widget_3)
        self.classes_2.setObjectName(u"classes_2")
        self.classes_2.setFont(font1)
        self.classes_2.setIcon(icon3)
        self.classes_2.setIconSize(QSize(25, 25))
        self.classes_2.setCheckable(True)
        self.classes_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.classes_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.setting_2 = QPushButton(self.widget_3)
        self.setting_2.setObjectName(u"setting_2")
        self.setting_2.setFont(font1)
        self.setting_2.setIcon(icon4)
        self.setting_2.setIconSize(QSize(25, 25))
        self.setting_2.setCheckable(True)
        self.setting_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(28, 425, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(20, 20))
        self.label_5.setMaximumSize(QSize(20, 20))
        self.label_5.setPixmap(QPixmap(u"../../../../Users/foral/Desktop/QTUI/Images/Group 91.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_8 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_10 = QSpacerItem(15, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)

        self.main_menu = QWidget(Dialog)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_6 = QVBoxLayout(self.main_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.widget_2 = QWidget(self.main_menu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(700, 40))
        self.widget_2.setStyleSheet(u"background-color:\"#ffffff\";")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(900, 40))
        font2 = QFont()
        font2.setFamilies([u"Myanmar Khyay"])
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"textSize:\"150dp\";")

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.main_menu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color:\"#FFFFFF\";\n"
"\n"
"QPushButton {\n"
"    color: black;\n"
"    height: 35px;\n"
"    border: none;\n"
" \n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_10 = QPushButton(self.widget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon6 = QIcon()
        icon6.addFile(u"Images/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.pushButton_11 = QPushButton(self.widget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    height: 35px;\n"
"    border: none;\n"
" \n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color:\"#F5FAFE\";\n"
"color:\"#1F95EF\";\n"
"font-weight:bold;\n"
"\n"
"}\n"
"")
        self.pushButton_11.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.pushButton_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(450, 0))
        self.lineEdit.setMaximumSize(QSize(500, 30))

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_10 = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:\"#FFFFFF\";")
        self.Search_Page = QWidget()
        self.Search_Page.setObjectName(u"Search_Page")
        self.label_7 = QLabel(self.Search_Page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 210, 381, 161))
        font3 = QFont()
        font3.setFamilies([u"Myanmar Khyay"])
        font3.setPointSize(30)
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.Search_Page)
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.label_8 = QLabel(self.Setting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 250, 381, 161))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.Setting)
        self.Classes = QWidget()
        self.Classes.setObjectName(u"Classes")
        self.label_6 = QLabel(self.Classes)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 165, 381, 161))
        self.label_6.setFont(font3)
        self.stackedWidget.addWidget(self.Classes)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)


        self.retranslateUi(Dialog)
        self.pushButton_10.toggled.connect(self.widget_3.setVisible)
        self.pushButton_10.toggled.connect(self.widget.setHidden)
        self.pushButton_9.toggled.connect(self.widget.setVisible)
        self.setting_1.toggled.connect(self.setting_2.setChecked)
        self.classes_1.toggled.connect(self.classes_2.setChecked)
        self.search_1.toggled.connect(self.search_2.setChecked)
        self.search_2.toggled.connect(self.search_1.setChecked)
        self.classes_2.toggled.connect(self.classes_1.setChecked)
        self.setting_2.toggled.connect(self.setting_1.setChecked)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Face Recognition", None))
        self.pushButton_8.setText("")
        self.pushButton_2.setText("")
        self.search_1.setText("")
        self.classes_1.setText("")
        self.setting_1.setText("")
        self.label_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton.setText("")
        self.search_2.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.classes_2.setText(QCoreApplication.translate("Dialog", u"Classes", None))
        self.setting_2.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome Elene Bujor, attendance system is ready to operate.", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Classes", None))
    # retranslateUi

