from ui_mainpage import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog, QPushButton

class MyMainPage(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Page")
            #here is widget the board nothing else
        self.widget_3.setHidden(True)

        self.search_1.clicked.connect(self.switch_to_search_Page)
        self.search_2.clicked.connect(self.switch_to_search_Page)

        self.classes_1.clicked.connect(self.switch_to_classes_Page)
        self.classes_2.clicked.connect(self.switch_to_classes_Page)

        self.setting_1.clicked.connect(self.switch_to_setting_Page)
        self.setting_2.clicked.connect(self.switch_to_setting_Page)


    def switch_to_search_Page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_classes_Page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_setting_Page(self):
        self.stackedWidget.setCurrentIndex(1)


