from enum import global_str

import requests
from urllib3 import request
import json
from ui_mainpage import Ui_Dialog
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QWidget, QFileDialog, QLabel
from PySide6.QtCore import QCoreApplication
url = ''

last_index = 0


class MyMainPage(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Main Page")

        # Hide widget initially
        self.widget_3.setHidden(True)
        global url
        url = r'https://cuddly-falcon-solid.ngrok-free.app/'
        print(url)
        
        # Fetch the student data
        response =requests.get(url[:-1] + "/api/collections/students/records?fields=id,Name,Group")
        response_data = response.json()
        self.students =response_data.get("items", [])

        # Dictionary to store buttons
        self.student_buttons = {}

        # Add student widgets
        index = 0
        row = 0
        width = 161
        height = 201
        padding = 40
        spacing = 20

        for student in self.students:
            # Create a button for each student
            button = QPushButton(parent=self.Students, text=f"{student['Name']}")
            button.setStyleSheet(u"background-color: #8DB7F5;\n"
                                 "border-radius: 10px;\n"
                                 "font-size:15px;\n")

            # Position the button
            button.setGeometry(QRect(30 + (width + padding) * index, 30 + (height + spacing) * row, width, height))

            # Procent label inside the button
            procent_label = QLabel(parent=button, text="0%")
            procent_label.setStyleSheet("font-size: 12px; color: black;")
            procent_width = 30
            procent_height = 20
            procent_x = (button.width() - procent_width) // 2
            procent_y = button.height() - procent_height - 10
            procent_label.setGeometry(procent_x, procent_y, procent_width, procent_height)

            # Store the button in the dictionary using the student's ID or Name
            self.student_buttons[student['Name']] = {'button': button, 'label': procent_label}

            # Connect the button click to a function
            button.clicked.connect(lambda _, s=student: self.switch_to_page_with_present(s))

            index += 1
            if index > 3:
                index = 0
                row += 1

        # Initialize the current student key
        self.current_student_key = None

        # Connect buttons to functions
        self.search_1.clicked.connect(self.switch_to_search_Page)
        self.search_2.clicked.connect(self.switch_to_search_Page)
        self.classes_1.clicked.connect(self.switch_to_classes_Page)
        self.classes_2.clicked.connect(self.switch_to_classes_Page)
        self.setting_1.clicked.connect(self.switch_to_setting_Page)
        self.setting_2.clicked.connect(self.switch_to_setting_Page)
        self.pushButton_4.clicked.connect(self.switch_to_class_with_students)
        self._3.clicked.connect(self.switch_to_upload_Page)
        self.pushButton_3.clicked.connect(self.open_image_dialog)

        # Back button
        self.pushButton_64.clicked.connect(self.switch_to_class_with_students)

        # Connect the pushButton_62 click to toggle status
        self.pushButton_62.clicked.connect(self.toggle_status)

    def switch_to_search_Page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_classes_Page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_setting_Page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_upload_Page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_class_with_students(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_page_with_present(self, student):
        """Switch to the page with the selected student's details."""
        self.current_student_key = student['id']

        if student:
            self.stackedWidget.setCurrentIndex(5)
            # Update the buttons with student info
            self.pushButton_57.setText(QCoreApplication.translate("Dialog", student["Name"], None))
            self.pushButton_59.setText(QCoreApplication.translate("Dialog", student["Group"], None))
            #self.pushButton_60.setText(QCoreApplication.translate("Dialog", student["Gender"], None))
            self.pushButton_61.setText(QCoreApplication.translate("Dialog", student["id"], None))

            # Update the status button based on the student's current status
            self.update_status_button(student.get("status", "absent"))

            self.label_6.setText(QCoreApplication.translate("Dialog", u"Classes", None))
        else:
            print(f"Student info for {self.current_student_key} not found.")

    def update_status_button(self, status):
        """Update the pushButton_62 with the correct text and style."""
        if status == 'present':
            self.pushButton_62.setText(QCoreApplication.translate("Dialog", "Present", None))
            self.pushButton_62.setStyleSheet(u"background-color: #108476; color: #000000")
        else:
            self.pushButton_62.setText(QCoreApplication.translate("Dialog", "Absent", None))
            self.pushButton_62.setStyleSheet(u"background-color: #d8d8d8; color: #000000")

    def toggle_status(self):
        """Toggle the status of the currently selected student between 'present' and 'absent'."""
        if self.current_student_key:
            # Find the student in self.students by id
            student = next((s for s in self.students if s['id'] == self.current_student_key), None)
            if student:
                # Toggle status
                if student.get("status") == "present":
                    student["status"] = "absent"
                else:
                    student["status"] = "present"

                # Update the button display based on the new status
                self.update_status_button(student["status"])
        else:
            print("No student selected for status change.")

    def open_image_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Open the dialog in read-only mode

        file_Name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)",
            options=options
        )
        if file_Name:  # Check if a file was selected
            self.image_path = file_Name  # Save the path to the selected image
            print(f"Selected image path: {self.image_path}")  # Optional: Print the selected path
            self.send_image_to_server(self.image_path)  # Send the image to the server

    def send_image_to_server(self, image_path):
        global url
        url_1 = f"{url[:-1]}/find/FAF-232"  # Adjust your endpoint as needed
        print(url_1)
        files = {'file': open(image_path, 'rb')}  # Open the image file in binary mode

        response = requests.post(url_1, files=files)
        print(response)
        if response.status_code == 200:
            print(f"Image uploaded successfully! - {response.text}")

            # Assuming the response is a dictionary with student Names as keys and percentages as values
            json_text = response.text.replace("'", '"')
            procent_data = json.loads(json_text)["python_output"]

            # Update each button's label with the new percentage
            for student_Name, procent_value in procent_data.items():
                if student_Name in self.student_buttons:
                    button_info = self.student_buttons[student_Name]
                    button_info['label'].setText(procent_value+"%")  # Update the label with the percentage
                    self.stackedWidget.setCurrentIndex(2)
        else:
            print(f"Failed to upload image: {response.status_code} - {response.text}")


