from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main container widget for the page (Classe_Students)
        self.Classe_Students = QWidget()
        self.Classe_Students.setObjectName(u"Classe_Students")

        # Create the scroll area
        self.scroll_area = QScrollArea(self.Classe_Students)
        self.scroll_area.setWidgetResizable(True)  # Allow the content to resize with the scroll area

        # Create the content widget (Students widget)
        self.Students = QWidget(self.Classe_Students)
        self.Students.setObjectName(u"Students")
        self.Students.setStyleSheet(u"background-color: #F5F5F5;")  # Background color for Students widget

        # Create a layout for the content widget (Students)
        layout = QVBoxLayout(self.Students)

        # Add some content to the layout (e.g., buttons)
        for i in range(30):  # Simulating a large number of items
            button = QPushButton(f"Student {i + 1}")
            layout.addWidget(button)

        # Set the Students widget as the content of the scroll area
        self.scroll_area.setWidget(self.Students)

        # Main layout for the page
        main_layout = QVBoxLayout(self.Classe_Students)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)
        self.setWindowTitle("Classe Students Page with Scroll")
        self.resize(900, 800)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
