from PySide6.QtWidgets import QApplication
import sys
from BetaV.MainPage import MyMainPage

app = QApplication(sys.argv)

window = MyMainPage()
window.show()
app.exec()