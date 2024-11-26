"Now Main"
from PySide6.QtWidgets import QApplication
import sys
from MainTest import MyMainPage2
import requests
app = QApplication(sys.argv)

window = MyMainPage2()
window.show()
app.exec()