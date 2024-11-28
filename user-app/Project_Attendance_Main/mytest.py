'''
this is a working example, need to add widgets here in this format
problem: adding QMainWindow attribute breaks the widgets
'''

import sys
from PySide6.QtGui import QPixmap, QImage, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QScrollArea, QWidget, QLineEdit, QPushButton, QDialog
from ui_maintest import Ui_Dialog

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a vertical layout for the custom widget
        layout = QVBoxLayout(self)
        
        # Create a label and set some text
        label = QLabel("This is a custom widget!", self)
        layout.addWidget(label)
        
        # Create a text input field (QLineEdit)
        lineEdit = QLineEdit(self)
        layout.addWidget(lineEdit)
        
        # Create a button
        button = QPushButton("Click Me", self)
        layout.addWidget(button)



class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()

        
        self.initUI()

    def initUI(self):
        # Create the main widget that will hold all other widgets
        self.mywidget = QWidget()
        
        # Create a vertical layout to hold all the content
        self.vbox = QVBoxLayout(self.mywidget)

        for _ in range(20):
            custom_widget = CustomWidget()  # Instantiate the custom widget
            self.vbox.addWidget(custom_widget)
            # self.vbox.addWidget(self.widget_10)
            # self.vbox.addWidget(self.widget_9)
            # self.vbox.addWidget(self.widget_15)
            # self.vbox.addWidget(self.widget_17)

        # Create a scroll area to make the images and custom widget scrollable
        scrollArea = QScrollArea()
        scrollArea.setBackgroundRole(QPalette.Dark)
        scrollArea.setWidget(self.mywidget)

        # Set the scroll area as the central widget of the main window
        self.setCentralWidget(scrollArea)

        # Set the window properties
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Images and Custom Widget in Scroll Area')
        self.show()

# Main entry point of the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



