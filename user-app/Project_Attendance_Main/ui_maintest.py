# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
        Dialog.resize(1041, 2167)
        font = QFont()
        font.setFamilies([u"Myanmar Khyay"])
        font.setPointSize(100)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color:\"#D9D9D9\";\n"
"font-family: Myanmar Khyay;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu = QWidget(Dialog)
        self.main_menu.setObjectName(u"main_menu")
        font1 = QFont()
        font1.setFamilies([u"Myanmar Khyay"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.main_menu.setFont(font1)
        self.main_menu.setStyleSheet(u"background-color:\"#F5F5F5\";")
        self.verticalLayout_6 = QVBoxLayout(self.main_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 20, 0, 0)
        self.widget_2 = QWidget(self.main_menu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(700, 40))
        self.widget_2.setStyleSheet(u"background-color:\"#F5F5F5\";")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(900, 40))
        font2 = QFont()
        font2.setFamilies([u"Myanmar Khyay"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"textSize:\"150dp\";")

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.main_menu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color:\"#F5F5F5\";\n"
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
        font3 = QFont()
        font3.setFamilies([u"Myanmar Khyay"])
        font3.setKerning(True)
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"border-top-left-radius: 2px;          \n"
"border-bottom-left-radius: 2px;       \n"
"border-top-right-radius: 2px;         \n"
"border-bottom-right-radius: 2px;      ")
        icon = QIcon()
        icon.addFile(u"Images/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoDefault(True)

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
        icon1 = QIcon()
        icon1.addFile(u"Images/search-interface-symbol.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.pushButton_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QSize(450, 0))
        self.lineEdit.setMaximumSize(QSize(500, 30))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setStyleSheet(u"lineEdit->setStyleSheet(\n"
"    \"QLineEdit {\"\n"
"    \"    background-color: #D9D9D9;\"       // Background color (white in this case)\n"
"    \"    border: 2px solid #935152;\"       // Border color\n"
"    \"    border-top-left-radius: 20px;\"    // Top-left corner radius\n"
"    \"    border-top-right-radius: 20px;\"   // Top-right corner radius\n"
"    \"    border-bottom-left-radius: 20px;\" // Bottom-left corner radius\n"
"    \"    border-bottom-right-radius: 20px;\"// Bottom-right corner radius\n"
"    \"    padding: 5px;\"                    // Padding for inner text alignment\n"
"    \"}\"\n"
");\n"
"")
        self.lineEdit.setFrame(False)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.pushButton_23 = QPushButton(self.widget_4)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u" border: 1px solid #CCCCCC;\n"
"border-radius:20px;\n"
"padding:5px;\n"
"border-top-left-radius: 2px;          \n"
"border-bottom-left-radius: 2px;       \n"
"border-top-right-radius: 2px;         \n"
"border-bottom-right-radius: 2px;   ")

        self.horizontalLayout_6.addWidget(self.pushButton_23)

        self.horizontalSpacer_10 = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:\"#F5F5F5\";")
        self.Page_Search = QWidget()
        self.Page_Search.setObjectName(u"Page_Search")
        self.label_7 = QLabel(self.Page_Search)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 391, 41))
        font4 = QFont()
        font4.setFamilies([u"Myanmar Khyay"])
        font4.setPointSize(25)
        self.label_7.setFont(font4)
        self.widget_5 = QWidget(self.Page_Search)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(30, 90, 161, 201))
        self.widget_5.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 151, 201))
        self.label_20.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_20.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_20.setScaledContents(True)
        self.pushButton_9 = QPushButton(self.widget_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 60, 111, 71))
        self.pushButton_9.setMinimumSize(QSize(50, 50))
        self.pushButton_9.setMaximumSize(QSize(10000, 10000))
        font5 = QFont()
        font5.setFamilies([u"Myanmar Khyay"])
        self.pushButton_9.setFont(font5)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.widget_6 = QWidget(self.Page_Search)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(230, 90, 161, 201))
        self.widget_6.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_21 = QLabel(self.widget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 151, 201))
        self.label_21.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_21.setPixmap(QPixmap(u":/Curs/Images/Math2.png"))
        self.label_21.setScaledContents(True)
        self.pushButton_13 = QPushButton(self.widget_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(20, 60, 111, 71))
        self.pushButton_13.setMinimumSize(QSize(50, 50))
        self.pushButton_13.setMaximumSize(QSize(10000, 10000))
        self.pushButton_13.setFont(font5)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.stackedWidget.addWidget(self.Page_Search)
        self.Page_Setting = QWidget()
        self.Page_Setting.setObjectName(u"Page_Setting")
        self.label_8 = QLabel(self.Page_Setting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 361, 81))
        font6 = QFont()
        font6.setFamilies([u"Myanmar Khyay"])
        font6.setPointSize(30)
        self.label_8.setFont(font6)
        self.stackedWidget.addWidget(self.Page_Setting)
        self.Classe_Students = QWidget()
        self.Classe_Students.setObjectName(u"Classe_Students")
        self.Students = QWidget(self.Classe_Students)
        self.Students.setObjectName(u"Students")
        self.Students.setGeometry(QRect(0, 0, 900, 751))
        self.Students.setStyleSheet(u"background-color:\"#F5F5F5\";")
        self.widget_8 = QWidget(self.Students)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(30, 30, 161, 201))
        self.widget_8.setStyleSheet(u"\n"
"background-color: #8DB7F5;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.pushButton_6 = QPushButton(self.widget_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 120, 141, 50))
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(10000, 10000))
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    padding: 10px;\n"
"    font-size: 13px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_3 = QPushButton(self.widget_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 30, 101, 81))
        font7 = QFont()
        font7.setFamilies([u"Myanmar Khyay"])
        font7.setPointSize(5)
        self.pushButton_3.setFont(font7)
        icon2 = QIcon()
        icon2.addFile(u"Images/user1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(50, 50))
        self.pushButton_7 = QPushButton(self.widget_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(40, 160, 75, 24))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border: 1px solid #ff0000;\n"
"    padding: 5px;\n"
"    font-size: 13px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.widget_18 = QWidget(self.Students)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(220, 10, 171, 251))
        self.label_42 = QLabel(self.widget_18)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 20, 151, 201))
        self.label_42.setStyleSheet(u"background-color:#D9D9D9;\n"
"border: 1px solid #ff0000;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_42.setScaledContents(True)
        self.pushButton_4 = QPushButton(self.widget_18)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(40, 50, 91, 71))
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"background-color: transparent;")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(50, 50))
        self.pushButton_21 = QPushButton(self.widget_18)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(30, 120, 111, 50))
        self.pushButton_21.setMinimumSize(QSize(50, 50))
        self.pushButton_21.setMaximumSize(QSize(10000, 10000))
        self.pushButton_21.setFont(font5)
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
"    color: black;\n"
"    padding: 10px;\n"
"    font-size: 13px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.label_43 = QLabel(self.widget_18)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(60, 170, 49, 16))
        self.label_43.setStyleSheet(u"background-color: transparent;")
        self.stackedWidget.addWidget(self.Classe_Students)
        self.Page_Upload = QWidget()
        self.Page_Upload.setObjectName(u"Page_Upload")
        self.Upload_Part = QWidget(self.Page_Upload)
        self.Upload_Part.setObjectName(u"Upload_Part")
        self.Upload_Part.setGeometry(QRect(0, 0, 971, 751))
        self.Upload_Part.setStyleSheet(u"QWidget{\n"
"background-color: \"#D9D9D9\";\n"
"}")
        self.pushButton_8 = QPushButton(self.Upload_Part)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(360, 320, 151, 121))
        self.pushButton_8.setStyleSheet(u"border-top-left-radius: 20px;          \n"
"border-bottom-left-radius: 20px;       \n"
"border-top-right-radius: 20px;         \n"
"border-bottom-right-radius: 20px;      ")
        icon3 = QIcon()
        icon3.addFile(u"Images/1UploadPage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(150, 150))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.Page_Upload)
        self.Page_Upload2 = QWidget()
        self.Page_Upload2.setObjectName(u"Page_Upload2")
        self.widget_26 = QWidget(self.Page_Upload2)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setGeometry(QRect(200, 30, 421, 221))
        self.widget_26.setStyleSheet(u"background-color: #E2DEDE;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"")
        self.layoutWidget_4 = QWidget(self.widget_26)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(50, 30, 143, 171))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        font8 = QFont()
        font8.setFamilies([u"Myanmar Khyay"])
        font8.setPointSize(15)
        self.label_6.setFont(font8)

        self.verticalLayout_12.addWidget(self.label_6)

        self.label_32 = QLabel(self.layoutWidget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font8)

        self.verticalLayout_12.addWidget(self.label_32)

        self.label_40 = QLabel(self.layoutWidget_4)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_12.addWidget(self.label_40)

        self.label_34 = QLabel(self.layoutWidget_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font8)

        self.verticalLayout_12.addWidget(self.label_34)

        self.layoutWidget_5 = QWidget(self.widget_26)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(250, 30, 129, 171))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_67 = QPushButton(self.layoutWidget_5)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(0, 40))
        self.pushButton_67.setFont(font8)

        self.verticalLayout_13.addWidget(self.pushButton_67)

        self.pushButton_68 = QPushButton(self.layoutWidget_5)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(20, 40))
        self.pushButton_68.setFont(font8)

        self.verticalLayout_13.addWidget(self.pushButton_68)

        self.label_41 = QLabel(self.layoutWidget_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 30))
        self.label_41.setMaximumSize(QSize(16777215, 30))
        self.label_41.setFont(font8)
        self.label_41.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.label_41.setScaledContents(False)

        self.verticalLayout_13.addWidget(self.label_41)

        self.pushButton_69 = QPushButton(self.layoutWidget_5)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setMinimumSize(QSize(0, 30))
        self.pushButton_69.setMaximumSize(QSize(16777215, 30))
        self.pushButton_69.setFont(font8)

        self.verticalLayout_13.addWidget(self.pushButton_69)

        self.label_37 = QLabel(self.widget_26)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(160, 10, 101, 20))
        self.label_37.setFont(font8)
        self.widget_14 = QWidget(self.Page_Upload2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(40, 270, 761, 391))
        self.label_38 = QLabel(self.widget_14)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(100, 60, 571, 271))
        self.label_38.setPixmap(QPixmap(u":/Class_Picutre/Images/Class_Attendance.png"))
        self.label_38.setScaledContents(True)
        self.label_39 = QLabel(self.widget_14)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(320, 20, 141, 20))
        self.label_39.setFont(font8)
        self.pushButton_5 = QPushButton(self.widget_14)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(314, 343, 121, 31))
        font9 = QFont()
        font9.setFamilies([u"Myanmar Khyay"])
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setUnderline(False)
        self.pushButton_5.setFont(font9)
        self.pushButton_5.setStyleSheet(u"background-color: #d9d9d9;\n"
"border-top-left-radius: 20px;          \n"
"border-bottom-left-radius: 20px;       \n"
"border-top-right-radius: 20px;         \n"
"border-bottom-right-radius: 20px;      \n"
"\n"
" ")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.Page_Upload2)
        self.Page_Classes = QWidget()
        self.Page_Classes.setObjectName(u"Page_Classes")
        self.widget_12 = QWidget(self.Page_Classes)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(0, 0, 851, 2031))
        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(0, 600, 851, 281))
        self.label_28 = QLabel(self.widget_15)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 10, 391, 41))
        font10 = QFont()
        font10.setFamilies([u"Myanmar Khyay"])
        font10.setPointSize(20)
        self.label_28.setFont(font10)
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(10, 60, 161, 201))
        self.widget_16.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_27 = QLabel(self.widget_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 151, 201))
        self.label_27.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_27.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_27.setScaledContents(True)
        self.pushButton_17 = QPushButton(self.widget_16)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_17.setMinimumSize(QSize(50, 50))
        self.pushButton_17.setMaximumSize(QSize(10000, 10000))
        self.pushButton_17.setFont(font5)
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)
        self.label_18 = QLabel(self.widget_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 100, 111, 31))
        self.label_18.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_19 = QLabel(self.widget_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 140, 111, 31))
        font11 = QFont()
        font11.setFamilies([u"Myanmar Khyay"])
        font11.setBold(False)
        font11.setItalic(False)
        self.label_19.setFont(font11)
        self.label_19.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.widget_9 = QWidget(self.widget_12)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 290, 851, 281))
        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(10, 60, 161, 201))
        self.widget_11.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_24 = QLabel(self.widget_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 151, 201))
        self.label_24.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_24.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_24.setScaledContents(True)
        self.pushButton_16 = QPushButton(self.widget_11)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_16.setMinimumSize(QSize(50, 50))
        self.pushButton_16.setMaximumSize(QSize(10000, 10000))
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)
        self.label_15 = QLabel(self.widget_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 100, 111, 31))
        self.label_15.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_17 = QLabel(self.widget_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 140, 111, 31))
        self.label_17.setFont(font11)
        self.label_17.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_26 = QLabel(self.widget_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 10, 391, 41))
        self.label_26.setFont(font10)






        self.widget_10 = QWidget(self.widget_12)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(10, 10, 841, 271))
        self.widget_7 = QWidget(self.widget_10)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 60, 161, 201))
        self.widget_7.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_22 = QLabel(self.widget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 151, 201))
        self.label_22.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_22.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_22.setScaledContents(True)
        self.pushButton_14 = QPushButton(self.widget_7)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_14.setMinimumSize(QSize(50, 50))
        self.pushButton_14.setMaximumSize(QSize(10000, 10000))
        self.pushButton_14.setFont(font5)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)
        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 100, 111, 31))
        self.label_9.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 140, 111, 31))
        self.label_10.setFont(font11)
        self.label_10.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_25 = QLabel(self.widget_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 10, 391, 41))
        self.label_25.setFont(font10)






        self.widget_17 = QWidget(self.widget_12)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(-1, 919, 851, 261))
        self.label_29 = QLabel(self.widget_17)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 10, 391, 41))
        self.label_29.setFont(font10)
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(10, 50, 161, 201))
        self.widget_19.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_30 = QLabel(self.widget_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 0, 151, 201))
        self.label_30.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_30.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_30.setScaledContents(True)
        self.pushButton_18 = QPushButton(self.widget_19)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_18.setMinimumSize(QSize(50, 50))
        self.pushButton_18.setMaximumSize(QSize(10000, 10000))
        self.pushButton_18.setFont(font5)
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)
        self.label_31 = QLabel(self.widget_19)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 100, 111, 31))
        self.label_31.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_33 = QLabel(self.widget_19)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 140, 111, 31))
        self.label_33.setFont(font11)
        self.label_33.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.widget_20 = QWidget(self.widget_12)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(0, 1210, 851, 261))
        self.label_35 = QLabel(self.widget_20)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(20, 10, 391, 41))
        self.label_35.setFont(font10)
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setGeometry(QRect(10, 50, 161, 201))
        self.widget_21.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_36 = QLabel(self.widget_21)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(0, 0, 151, 201))
        self.label_36.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_36.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_36.setScaledContents(True)
        self.pushButton_19 = QPushButton(self.widget_21)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_19.setMinimumSize(QSize(50, 50))
        self.pushButton_19.setMaximumSize(QSize(10000, 10000))
        self.pushButton_19.setFont(font5)
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)
        self.label_44 = QLabel(self.widget_21)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 100, 111, 31))
        self.label_44.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_45 = QLabel(self.widget_21)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 140, 111, 31))
        self.label_45.setFont(font11)
        self.label_45.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.widget_22 = QWidget(self.widget_12)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setGeometry(QRect(0, 1480, 851, 261))
        self.label_46 = QLabel(self.widget_22)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 0, 391, 41))
        self.label_46.setFont(font10)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setGeometry(QRect(10, 50, 161, 201))
        self.widget_23.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_47 = QLabel(self.widget_23)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(0, 0, 151, 201))
        self.label_47.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_47.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_47.setScaledContents(True)
        self.pushButton_20 = QPushButton(self.widget_23)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_20.setMinimumSize(QSize(50, 50))
        self.pushButton_20.setMaximumSize(QSize(10000, 10000))
        self.pushButton_20.setFont(font5)
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setAutoExclusive(True)
        self.label_48 = QLabel(self.widget_23)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 100, 111, 31))
        self.label_48.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_49 = QLabel(self.widget_23)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(20, 140, 111, 31))
        self.label_49.setFont(font11)
        self.label_49.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.widget_25 = QWidget(self.widget_12)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setGeometry(QRect(0, 1760, 851, 301))
        self.label_50 = QLabel(self.widget_25)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(20, 0, 391, 41))
        self.label_50.setFont(font10)
        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setGeometry(QRect(10, 50, 161, 201))
        self.widget_27.setStyleSheet(u"background-color: #ffff;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"\n"
"   ")
        self.label_51 = QLabel(self.widget_27)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(0, 0, 151, 201))
        self.label_51.setStyleSheet(u"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;   ")
        self.label_51.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))
        self.label_51.setScaledContents(True)
        self.pushButton_22 = QPushButton(self.widget_27)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(20, 20, 111, 71))
        self.pushButton_22.setMinimumSize(QSize(50, 50))
        self.pushButton_22.setMaximumSize(QSize(10000, 10000))
        self.pushButton_22.setFont(font5)
        self.pushButton_22.setAutoFillBackground(False)
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    border: 1px solid #CCCCCC;\n"
"	border-radius:20px;\n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"    text-align: center; /* Center text */\n"
"}")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setAutoExclusive(True)
        self.label_52 = QLabel(self.widget_27)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(20, 100, 111, 31))
        self.label_52.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.label_53 = QLabel(self.widget_27)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(20, 140, 111, 31))
        self.label_53.setFont(font11)
        self.label_53.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"border-radius:20px;\n"
"font-size: 12px;\n"
"text-align: center; \n"
"border-radius:20px;")
        self.stackedWidget.addWidget(self.Page_Classes)
        self.Class_MD = QWidget()
        self.Class_MD.setObjectName(u"Class_MD")
        self.label_2 = QLabel(self.Class_MD)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 391, 71))
        self.label_2.setFont(font10)
        self.stackedWidget.addWidget(self.Class_MD)
        self.Student_Info = QWidget()
        self.Student_Info.setObjectName(u"Student_Info")
        self.widget_13 = QWidget(self.Student_Info)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(0, 0, 871, 740))
        self.widget_13.setStyleSheet(u"background:#F5F5F5;")
        self.widget_24 = QWidget(self.widget_13)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(200, 390, 431, 221))
        self.widget_24.setStyleSheet(u"background-color: #E2DEDE;\n"
"border-top-left-radius: 10px;          \n"
"border-bottom-left-radius: 10px;       \n"
"border-top-right-radius: 10px;         \n"
"border-bottom-right-radius: 10px;      \n"
"")
        self.layoutWidget = QWidget(self.widget_24)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 30, 116, 161))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font8)

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)

        self.verticalLayout_8.addWidget(self.label_13)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font8)

        self.verticalLayout_8.addWidget(self.label_16)

        self.layoutWidget1 = QWidget(self.widget_24)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 30, 200, 161))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_57 = QPushButton(self.layoutWidget1)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setFont(font8)

        self.verticalLayout_9.addWidget(self.pushButton_57)

        self.pushButton_58 = QPushButton(self.layoutWidget1)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setFont(font8)

        self.verticalLayout_9.addWidget(self.pushButton_58)

        self.pushButton_61 = QPushButton(self.layoutWidget1)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setFont(font8)

        self.verticalLayout_9.addWidget(self.pushButton_61)

        self.label_11 = QLabel(self.widget_24)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 10, 191, 20))
        self.label_11.setFont(font8)
        self.pushButton_62 = QPushButton(self.widget_13)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setEnabled(True)
        self.pushButton_62.setGeometry(QRect(330, 300, 141, 51))
        font12 = QFont()
        font12.setFamilies([u"Myanmar Khyay"])
        font12.setPointSize(12)
        self.pushButton_62.setFont(font12)
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
        self.pushButton_64.setGeometry(QRect(10, 20, 75, 24))
        self.pushButton_64.setFont(font8)
        self.pushButton_64.setStyleSheet(u"QPushButton {\n"
"        display: inline-block;       /* Inline block layout */\n"
"        border-radius: 12px;         /* Rounded corners */\n"
"    }\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"Images/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_64.setIcon(icon4)
        self.pushButton_64.setIconSize(QSize(25, 25))
        self.Original_Picture_ID = QLabel(self.widget_13)
        self.Original_Picture_ID.setObjectName(u"Original_Picture_ID")
        self.Original_Picture_ID.setGeometry(QRect(450, 120, 151, 151))
        self.Original_Picture_ID.setFont(font5)
        self.Original_Picture_ID.setPixmap(QPixmap(u":/newPrefix/Images/Emma_Photo_2.png"))
        self.Original_Picture_ID.setScaledContents(True)
        self.Class_Picture_ID = QLabel(self.widget_13)
        self.Class_Picture_ID.setObjectName(u"Class_Picture_ID")
        self.Class_Picture_ID.setGeometry(QRect(220, 120, 141, 151))
        self.Class_Picture_ID.setFont(font5)
        self.Class_Picture_ID.setPixmap(QPixmap(u":/newPrefix/Images/Emma_Photo_1.png"))
        self.Class_Picture_ID.setScaledContents(True)
        self.stackedWidget.addWidget(self.Student_Info)
        self.Page_Search_2 = QWidget()
        self.Page_Search_2.setObjectName(u"Page_Search_2")
        self.stackedWidget.addWidget(self.Page_Search_2)
        self.Page_Registration = QWidget()
        self.Page_Registration.setObjectName(u"Page_Registration")
        self.widget_28 = QWidget(self.Page_Registration)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setGeometry(QRect(60, 50, 761, 601))
        self.lineEdit_3 = QLineEdit(self.widget_28)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(190, 120, 221, 41))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #ccc;            /* Light gray border */\n"
"    border-radius: 5px;                /* Rounded corners */\n"
"    padding: 10px;                     /* Padding inside the field */\n"
"    font-size: 16px;                   /* Font size */\n"
"    color: #333;                       /* Text color */\n"
"    background-color: #f9f9f9;         /* Light gray background */\n"
"    selection-background-color: #4CAF50; /* Background color for text selection */\n"
"    selection-color: white;            /* Color of the selected text */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4CAF50;         /* Green border when focused */\n"
"    background-color: #ffffff;         /* White background when focused */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #888;                       /* Placeholder text color */\n"
"    font-style: italic;                /* Italic placeholder text */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #e0e0e0;         /* "
                        "Disabled background */\n"
"    color: #b0b0b0;                    /* Disabled text color */\n"
"    border: 2px solid #d0d0d0;         /* Disabled border */\n"
"}")
        self.lineEdit_2 = QLineEdit(self.widget_28)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 60, 221, 41))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #ccc;            /* Light gray border */\n"
"    border-radius: 5px;                /* Rounded corners */\n"
"    padding: 10px;                     /* Padding inside the field */\n"
"    font-size: 16px;                   /* Font size */\n"
"    color: #333;                       /* Text color */\n"
"    background-color: #f9f9f9;         /* Light gray background */\n"
"    selection-background-color: #4CAF50; /* Background color for text selection */\n"
"    selection-color: white;            /* Color of the selected text */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4CAF50;         /* Green border when focused */\n"
"    background-color: #ffffff;         /* White background when focused */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #888;                       /* Placeholder text color */\n"
"    font-style: italic;                /* Italic placeholder text */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #e0e0e0;         /* "
                        "Disabled background */\n"
"    color: #b0b0b0;                    /* Disabled text color */\n"
"    border: 2px solid #d0d0d0;         /* Disabled border */\n"
"}")
        self.label_54 = QLabel(self.widget_28)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(180, 20, 231, 31))
        self.label_54.setFont(font1)
        self.pushButton_24 = QPushButton(self.widget_28)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(240, 180, 101, 41))
        font13 = QFont()
        font13.setFamilies([u"Myanmar Khyay"])
        font13.setBold(True)
        self.pushButton_24.setFont(font13)
        self.pushButton_24.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* Green background */\n"
"    color: white;              /* White text */\n"
"    border: 2px solid #4CAF50; /* Green border */\n"
"    border-radius: 12px;       /* Rounded corners */\n"
"    padding: 5px 10px;        /* Padding around the text */\n"
"    font-size: 16px;           /* Font size */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Slightly darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388e3c; /* Even darker green when clicked */\n"
"    border-color: #388e3c;     /* Darker border on press */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #c8e6c9; /* Lighter color when disabled */\n"
"    color: #bdbdbd;             /* Gray text when disabled */\n"
"    border-color: #bdbdbd;      /* Gray border when disabled */\n"
"}\n"
"")
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.Page_Registration)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

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
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setSizeIncrement(QSize(100, 100))
        icon5 = QIcon()
        icon5.addFile(u"Images/Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(45, 45))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.search_1 = QPushButton(self.widget)
        self.search_1.setObjectName(u"search_1")
        self.search_1.setFont(font8)
        self.search_1.setIcon(icon1)
        self.search_1.setIconSize(QSize(30, 30))
        self.search_1.setCheckable(True)
        self.search_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.search_1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.classes_1 = QPushButton(self.widget)
        self.classes_1.setObjectName(u"classes_1")
        icon6 = QIcon()
        icon6.addFile(u"Images/student_17584468.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.classes_1.setIcon(icon6)
        self.classes_1.setIconSize(QSize(30, 30))
        self.classes_1.setCheckable(True)
        self.classes_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.classes_1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.setting_1 = QPushButton(self.widget)
        self.setting_1.setObjectName(u"setting_1")
        icon7 = QIcon()
        icon7.addFile(u"Images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_1.setIcon(icon7)
        self.setting_1.setIconSize(QSize(25, 25))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_12)

        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon8 = QIcon()
        icon8.addFile(u"Images/1upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QSize(25, 25))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_12)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(28, 350, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

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
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 70))
        self.pushButton.setMaximumSize(QSize(120, 70))
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(80, 70))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.search_2 = QPushButton(self.widget_3)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setFont(font8)
        self.search_2.setIcon(icon1)
        self.search_2.setIconSize(QSize(25, 25))
        self.search_2.setCheckable(True)
        self.search_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.search_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.classes_2 = QPushButton(self.widget_3)
        self.classes_2.setObjectName(u"classes_2")
        self.classes_2.setFont(font8)
        self.classes_2.setIcon(icon6)
        self.classes_2.setIconSize(QSize(25, 25))
        self.classes_2.setCheckable(True)
        self.classes_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.classes_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.setting_2 = QPushButton(self.widget_3)
        self.setting_2.setObjectName(u"setting_2")
        self.setting_2.setFont(font8)
        self.setting_2.setIcon(icon7)
        self.setting_2.setIconSize(QSize(25, 25))
        self.setting_2.setCheckable(True)
        self.setting_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_11)

        self.pushButton_upload = QPushButton(self.widget_3)
        self.pushButton_upload.setObjectName(u"pushButton_upload")
        font14 = QFont()
        font14.setFamilies([u"Myanmar Khyay"])
        font14.setPointSize(15)
        font14.setBold(False)
        self.pushButton_upload.setFont(font14)
        self.pushButton_upload.setIcon(icon8)
        self.pushButton_upload.setIconSize(QSize(25, 25))
        self.pushButton_upload.setCheckable(True)
        self.pushButton_upload.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_upload)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(28, 350, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_8 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_10 = QSpacerItem(15, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.pushButton_10.toggled.connect(self.widget_3.setVisible)
        self.pushButton_10.toggled.connect(self.widget.setHidden)
        self.setting_1.toggled.connect(self.setting_2.setChecked)
        self.classes_1.toggled.connect(self.classes_2.setChecked)
        self.search_1.toggled.connect(self.search_2.setChecked)
        self.search_2.toggled.connect(self.search_1.setChecked)
        self.classes_2.toggled.connect(self.classes_1.setChecked)
        self.setting_2.toggled.connect(self.setting_1.setChecked)
        self.pushButton_12.toggled.connect(self.pushButton_upload.setChecked)
        self.pushButton_upload.toggled.connect(self.pushButton_12.setChecked)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Face Recognition", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome Bill Gates, attendance system is ready to operate.", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"what are you looking for ?(in one click you can find any person)", None))
        self.pushButton_23.setText(QCoreApplication.translate("Dialog", u"Find", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Today lectures", None))
        self.label_20.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Discrete  \n"
"Mathematics", None))
        self.label_21.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"PSA", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Emma Watson", None))
        self.pushButton_3.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"50%", None))
        self.label_42.setText("")
        self.pushButton_4.setText("")
        self.pushButton_21.setText(QCoreApplication.translate("Dialog", u"Emma Watson", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"     0%", None))
        self.pushButton_8.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Total students:", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Not present: ", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">Unrecognizable:      </span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"Present: ", None))
        self.pushButton_67.setText(QCoreApplication.translate("Dialog", u"15", None))
        self.pushButton_68.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"         2", None))
        self.pushButton_69.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"Attendance:", None))
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("Dialog", u"Picture of class:", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Back to class", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Wednesday", None))
        self.label_27.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("Dialog", u"Name  \n"
"Class", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
        self.label_24.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("Dialog", u"Name  \n"
"Class", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Tuesday", None))
        self.label_22.setText("")

        self.pushButton_14.setText(QCoreApplication.translate("Dialog", u"Name  \n""Class", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))


        self.label_25.setText(QCoreApplication.translate("Dialog", u"Today lectures", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Thursday", None))
        self.label_30.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("Dialog", u"Name  \n"
"Class", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"Friday", None))
        self.label_36.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("Dialog", u"Name  \n"
"Class", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"Saturday", None))
        self.label_47.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("Dialog", u"Name  \n"
"Class", None))
        self.label_48.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_49.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
        self.label_50.setText(QCoreApplication.translate("Dialog", u"Sunday", None))
        self.label_51.setText("")
        self.pushButton_22.setText(QCoreApplication.translate("Dialog", u"Name  \n"
"Class", None))
        self.label_52.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
        self.label_53.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Class Discrete Mathematics", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Group:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Student ID:", None))
        self.pushButton_57.setText(QCoreApplication.translate("Dialog", u"Emma Watson", None))
        self.pushButton_58.setText(QCoreApplication.translate("Dialog", u"17", None))
        self.pushButton_61.setText(QCoreApplication.translate("Dialog", u"35230", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Student Information:", None))
        self.pushButton_62.setText(QCoreApplication.translate("Dialog", u"Present", None))
        self.pushButton_64.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.Original_Picture_ID.setText("")
        self.Class_Picture_ID.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_54.setText(QCoreApplication.translate("Dialog", u"Sign-in with Coop-Mail", None))
        self.pushButton_24.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.pushButton_2.setText("")
        self.search_1.setText("")
        self.classes_1.setText("")
        self.setting_1.setText("")
        self.pushButton_12.setText("")
        self.pushButton.setText("")
        self.search_2.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.classes_2.setText(QCoreApplication.translate("Dialog", u"Classes", None))
        self.setting_2.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.pushButton_upload.setText(QCoreApplication.translate("Dialog", u"Upload", None))
    # retranslateUi

