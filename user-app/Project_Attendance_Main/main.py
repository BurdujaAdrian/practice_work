from PySide6.QtWidgets import QApplication
import sys
"Here will be the first vesrsion"
from MainPage2 import MyMainPage
import requests
app = QApplication(sys.argv)

window = MyMainPage()
window.show()
app.exec()