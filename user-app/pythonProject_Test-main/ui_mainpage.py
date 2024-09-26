# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage2.ui'
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
        Dialog.resize(1120, 882)
        font = QFont()
        font.setFamilies([u"Myanmar Khyay"])
        font.setPointSize(100)
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
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 70))
        self.pushButton.setMaximumSize(QSize(120, 70))
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(80, 70))

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_11)

        self._3 = QPushButton(self.widget_3)
        self._3.setObjectName(u"_3")
        self._3.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"Images/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self._3.setIcon(icon6)
        self._3.setIconSize(QSize(25, 25))
        self._3.setCheckable(True)
        self._3.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self._3)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(28, 350, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

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


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(15, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 5, 0, 1, 1)


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
        icon7 = QIcon()
        icon7.addFile(u"Images/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon7)
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
        self.label_7.setGeometry(QRect(10, 10, 361, 61))
        font3 = QFont()
        font3.setFamilies([u"Myanmar Khyay"])
        font3.setPointSize(30)
        self.label_7.setFont(font3)
        self.widget_5 = QWidget(self.Search_Page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(30, 120, 161, 201))
        self.widget_5.setStyleSheet(u"background-color: #8DB7F5;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.pushButton_4 = QPushButton(self.widget_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 60, 141, 91))
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setMaximumSize(QSize(10000, 10000))
        font4 = QFont()
        font4.setFamilies([u"Myanmar Khyay"])
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"text:Hi;\n"
"    color: black;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.widget_6 = QWidget(self.Search_Page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(220, 120, 161, 201))
        self.widget_6.setStyleSheet(u"background-color: #8DB7F5;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.pushButton_5 = QPushButton(self.widget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 60, 141, 91))
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(10000, 10000))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"text:Hi;\n"
"    color: black;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.stackedWidget.addWidget(self.Search_Page)
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.label_8 = QLabel(self.Setting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 361, 81))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.Setting)
        self.Classe_PSA = QWidget()
        self.Classe_PSA.setObjectName(u"Classe_PSA")
        self.Students = QWidget(self.Classe_PSA)
        self.Students.setObjectName(u"Students")
        self.Students.setGeometry(QRect(0, 0, 911, 740))
        self.Students.setStyleSheet(u"background:#FFFFFF;")
        self.stackedWidget.addWidget(self.Classe_PSA)
        self.Upload_Page = QWidget()
        self.Upload_Page.setObjectName(u"Upload_Page")
        self.widget_7 = QWidget(self.Upload_Page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 0, 901, 751))
        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 10, 131, 41))
        self.pushButton_3.setMaximumSize(QSize(150, 75))
        font5 = QFont()
        font5.setFamilies([u"Myanmar Khyay"])
        font5.setPointSize(10)
        self.pushButton_3.setFont(font5)
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 10, 111, 51))
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 140, 450, 400))
        self.label_10.setMaximumSize(QSize(450, 400))
        self.stackedWidget.addWidget(self.Upload_Page)
        self.Class_MD = QWidget()
        self.Class_MD.setObjectName(u"Class_MD")
        self.label_2 = QLabel(self.Class_MD)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 391, 101))
        font6 = QFont()
        font6.setFamilies([u"Myanmar Khyay"])
        font6.setPointSize(20)
        self.label_2.setFont(font6)
        self.stackedWidget.addWidget(self.Class_MD)
        self.Student_Info = QWidget()
        self.Student_Info.setObjectName(u"Student_Info")
        self.widget_13 = QWidget(self.Student_Info)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(0, 0, 670, 740))
        self.widget_13.setStyleSheet(u"background:#FFFFFF;")
        self.widget_24 = QWidget(self.widget_13)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(110, 310, 421, 271))
        self.widget_24.setStyleSheet(u"background-color: #D8D8D8;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"")
        self.layoutWidget = QWidget(self.widget_24)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 116, 221))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_13)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_15)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_16)

        self.layoutWidget1 = QWidget(self.widget_24)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(288, 10, 121, 241))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_57 = QPushButton(self.layoutWidget1)
        self.pushButton_57.setObjectName(u"pushButton_57")

        self.verticalLayout_9.addWidget(self.pushButton_57)

        self.pushButton_58 = QPushButton(self.layoutWidget1)
        self.pushButton_58.setObjectName(u"pushButton_58")

        self.verticalLayout_9.addWidget(self.pushButton_58)

        self.pushButton_59 = QPushButton(self.layoutWidget1)
        self.pushButton_59.setObjectName(u"pushButton_59")

        self.verticalLayout_9.addWidget(self.pushButton_59)

        self.pushButton_60 = QPushButton(self.layoutWidget1)
        self.pushButton_60.setObjectName(u"pushButton_60")

        self.verticalLayout_9.addWidget(self.pushButton_60)

        self.pushButton_61 = QPushButton(self.layoutWidget1)
        self.pushButton_61.setObjectName(u"pushButton_61")

        self.verticalLayout_9.addWidget(self.pushButton_61)

        self.pushButton_62 = QPushButton(self.widget_13)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setEnabled(True)
        self.pushButton_62.setGeometry(QRect(260, 250, 141, 51))
        font7 = QFont()
        font7.setFamilies([u"Myanmar Khyay"])
        font7.setPointSize(12)
        self.pushButton_62.setFont(font7)
        self.pushButton_62.setStyleSheet(u"background-color: #108476;\n"
"border-top-left-radius: 20px;          \n"
"border-bottom-left-radius: 20px;       \n"
"border-top-right-radius: 20px;         \n"
"border-bottom-right-radius: 20px;      \n"
"color: #ffffff;\n"
"\n"
"")
        self.pushButton_64 = QPushButton(self.widget_13)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setGeometry(QRect(30, 30, 75, 24))
        self.stackedWidget.addWidget(self.Student_Info)
        self.Classes = QWidget()
        self.Classes.setObjectName(u"Classes")
        self.label_6 = QLabel(self.Classes)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 261, 61))
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

        self.stackedWidget.setCurrentIndex(0)


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
        self._3.setText(QCoreApplication.translate("Dialog", u"Upload", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome Elene Bujor, attendance system is ready to operate.", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Discrete  \n"
"Mathematics", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"PSA", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Your File Name", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Image", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Class Discrete Mathematics", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Age:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Year:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Gender:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Student ID:", None))
        self.pushButton_57.setText(QCoreApplication.translate("Dialog", u"Plesca Denis", None))
        self.pushButton_58.setText(QCoreApplication.translate("Dialog", u"20", None))
        self.pushButton_59.setText(QCoreApplication.translate("Dialog", u"2004", None))
        self.pushButton_60.setText(QCoreApplication.translate("Dialog", u"Male", None))
        self.pushButton_61.setText(QCoreApplication.translate("Dialog", u"33441", None))
        self.pushButton_62.setText(QCoreApplication.translate("Dialog", u"Present", None))
        self.pushButton_64.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Classes", None))
    # retranslateUi

