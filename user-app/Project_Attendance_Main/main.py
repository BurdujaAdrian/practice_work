from PySide6.QtWidgets import QApplication
import sys
from MainPage import MyMainPage
import requests
app = QApplication(sys.argv)

window = MyMainPage()
window.show()
app.exec()