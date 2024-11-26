"Now Main"
import datetime
import random

import requests
from ui_maintest import Ui_Dialog
from PySide6.QtCore import QRect, QCoreApplication, QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QFileDialog, QLabel, QScrollArea, \
    QHBoxLayout
from PySide6.QtWidgets import QWidget
import json
from PySide6.QtCore import QTimer

" To frame all the design UI from Qt line in this Python code "

"TO DO"
"1)Transfer UI to python code - done "
"2)Frontend Development - 80% done "
"3)Beta Test"


"The Last 10%"

'''

Student Page code part:
-Make the local picture from backend to apper 


Classes Page and Search code part:
-Create a Python-based system to generate blocks like students for Classes.
-Display the class name, group, and time on each block.
-Add a scroll system to view the entire week's schedule (create a widget for each day).


'''




class MyMainPage2(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Main Page")
        self.setFixedSize(1000, 800)






        # Set the initial page of the stackedWidget to index 0 (Now Main page)
        self.stackedWidget.setCurrentIndex(9)
        if self.stackedWidget.currentIndex() == 9:
            self.widget_3.setHidden(True)
            self.widget.setHidden(True)
            self.widget_2.setHidden(True)
            self.widget_4.setHidden(True)
            self.pushButton_24.clicked.connect(self.login)

        # Hide widget initially
        self.widget_3.setHidden(True)
        global url
        global token
        global uuid
        global headers
        global group_id
        url = r'https://cuddly-falcon-solid.ngrok-free.app/'
        print(url)
        #self.students = []
        # Simulate local student data (instead of fetching from a server)

        self.Original_Picture_ID.picture()


        # Dictionary to store buttons
        self.student_buttons = {}

        # Add student widgets

        # Initialize the current student key
        self.current_student_key = None
        # Connect buttons to functions
        self.search_1.clicked.connect(self.switch_to_classes_Page)
        self.search_2.clicked.connect(self.switch_to_classes_Page)
        self.classes_1.clicked.connect(self.switch_to_classes_Page)
        self.classes_2.clicked.connect(self.switch_to_classes_Page)
        self.setting_1.clicked.connect(self.switch_to_setting_Page)
        self.setting_2.clicked.connect(self.switch_to_setting_Page)
        # Button upload
        self.pushButton_12.clicked.connect(self.switch_to_upload_Page)
        self.pushButton_upload.clicked.connect(self.switch_to_upload_Page)
        self.pushButton_8.clicked.connect(self.open_image_dialog)
        self.pushButton_23.clicked.connect(self.create_search_button)

        #Button back to class
        self.pushButton_5.clicked.connect(self.switch_to_class_back)

        # self.pushButton_4.clicked.connect(self.switch_to_class_with_students)
        # self._3.clicked.connect(self.switch_to_upload_Page)
        # self.pushButton_3.clicked.connect(self.open_image_dialog)

        # Back button
        self.pushButton_64.clicked.connect(self.switch_to_class_with_students)

        # Connect the pushButton_62 click to toggle status
        self.pushButton_62.clicked.connect(self.toggle_status)

    def generate_random_color_hex(self):
        # Generate a random color using RGB values
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Convert the RGB values to hexadecimal format
        hex_color = f'#{r:02x}{g:02x}{b:02x}'

        return hex_color

    def login(self):
        global url
        global token
        global uuid
        global group_id
        email = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        print(email)
        print(password)
        admin_login_url = f"{url[:-1]}/api/collections/Teacher_account/auth-with-password"
        data = {"identity": email, "password": password}
        print(data);
        response = requests.post(admin_login_url, json = data)
        print(response)
        token = response.json()["token"]
        headers = {"Authorization": f"Bearer {token}"}
        print(email)
        response_id = requests.get(url[:-1] + f"/api/collections/Teachers/records?filter=Email='{email}'",
                                   headers=headers)
        uuid = response_id.json()["items"][0]["id"]
        print(uuid)
        response_group = requests.get(url[:-1] + f"/api/collections/Groups/records?fields=Group_name,id", headers=headers)
        group_id = response_group.json()
        print(group_id)
        self.widget.setHidden(False)
        self.widget_2.setHidden(False)
        self.widget_4.setHidden(False)
        name = email.split("@")[0].split(".")
        self.take_student_info()
        self.create_student_buttons()
        self.label.setText(f"Welcome {name[0].capitalize()}" + " " + f"{name[1].capitalize()}" + ", attendance system is ready to operate.")
        self.create_classes_buttons_for_teacher()
        self.stackedWidget.setCurrentIndex(5)


    def get_schedule_info(self):
        global uuid
        global url
        global token
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url[:-1] + f"/api/collections/Schedule/records?filter=Teacher_ID='{uuid}'",
                                   headers=headers)
        print(response.json()['items'])
        return response.json()['items']


    def take_student_info(self):
        global url
        global token
        headers = {"Authorization": f"Bearer {token}"}
        all_students = []
        page = 1
        limit = 30

        while True:
            params = {"page": page, "limit": limit}
            response = requests.get(url[:-1] + "/api/collections/students/records?fields=id,Surname,Name,Group,Photo",
                                    headers=headers, params=params)
            response_data = response.json()

            # Collect students from the current page
            students = response_data.get("items", [])
            all_students.extend(students)

            # If there are no more students, break the loop
            if len(students) < limit:
                break

            # Move to the next page
            page += 1

        self.students = all_students
        print(f"Total students fetched: {len(self.students)}")
        self.change_student_info()

    def change_student_info(self):
        self.pushButton_67.setText(QCoreApplication.translate("Dialog", str(len(self.students)), None))
        self.pushButton_68.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"         0", None))
        self.pushButton_69.setText(QCoreApplication.translate("Dialog", u"0", None))


    def clear_student_buttons(self):
        """Clear all existing student buttons."""
        for student_name, button_info in self.student_buttons.items():
            button_info['button'].deleteLater()  # Remove button from the UI

        self.student_buttons.clear()  # Clear the dictionary

    # def create_search_button(self):
    #     "Make to find the specific student by name "
    #     "The search bar is : lineEdit"
    #     "The name of button is Find : pushButton_23"
    #     "Page name: Search_Page_2 - index 8"
    def create_search_button(self):
        """Create a button to search for a specific student by name or surname."""
        search_query = self.lineEdit.text()  # Get the text from the search bar (lineEdit)

        # Filter students based on the search query in either Name or Surname
        filtered_students = [
            student for student in self.students if
            search_query.lower() in (student['Name'].lower() + " " + student['Surname'].lower())
        ]

        if filtered_students:
            # If students are found, display them on the Search_Page_2
            self.update_search_results(filtered_students)
            self.stackedWidget.setCurrentIndex(8)  # Switch to Search_Page_2 (index 10)
        else:
            # If no students are found, show a message or handle accordingly
            self.show_no_results_message()

    def update_search_results(self, students):
        """Update the search results page with the filtered students."""
        # Clear any existing student buttons or results
        self.clear_search_results()

        # Create buttons or other UI elements for each found student
        for student in students:
            # Create a button for each filtered student (adjust layout as needed)
            button = QPushButton(parent=self.Page_Search_2, text=f"{student['Name']}" + " " + f"{student['Surname']}")
            button.setStyleSheet("background-color: #8DB7F5; border-radius: 10px; font-size: 15px;")

            # Set button size and position (you can adjust this as per your layout)
            button.setGeometry(
                QRect(30, 30 + (200 * students.index(student)), 161, 201))  # Adjust geometry for your layout

            # Connect button to student details page
            button.clicked.connect(lambda _, s=student: self.switch_to_page_with_present(s))

    def clear_search_results(self):
        """Clear existing search result buttons from the UI."""
        # Remove any existing buttons from Search_Page_2
        for button in self.Page_Search_2.findChildren(QPushButton):
            button.deleteLater()  # Remove the button from the layout
        self.student_buttons.clear()  # Clear the dictionary of student buttons

    def show_no_results_message(self):
        """Show a message when no students are found."""
        self.label_no_results.setText("No students found.")  # Assuming you have a label to show this message
        self.label_no_results.setVisible(True)  # Make the label visible

    """ make this work"""

    def create_classes_buttons_for_teacher(self):
        global url

        # Fetch the teacher data from the server

        index = 0
        row = 0
        width = 151
        height = 201
        padding = 40
        spacing = 20
        today_index = datetime.datetime.today().weekday()

        # Loop through each teacher and create a button with class details
        class_info = self.get_schedule_info()
        print(class_info)
        for clas in class_info:
            if datetime.datetime.today() == self.transform_day_to_index(clas["Day"]):
                self.class_label = QPushButton(self.widget_10)
                self.class_label.setObjectName(u"label_22")
                self.class_label.setGeometry(QRect(10 + (width + padding) * index, 60 + (height + spacing) * row, width, height))
                color = self.generate_random_color_hex()
                self.class_label.setStyleSheet(u"border-top-left-radius: 10px;          \n"
                                            "border-bottom-left-radius: 10px;       \n"
                                            "border-top-right-radius: 10px;         \n"
                                            "border-bottom-right-radius: 10px;   "
                                            f"background-color: {color}")
                #self.class_label.setPixmap(QPixmap(u":/Curs/Images/Math1.png"))

                self.pushButton_14.setText(QCoreApplication.translate("Dialog", u"Name  \n""Class", None))
                self.label_9.setText(QCoreApplication.translate("Dialog", u"      Name Group", None))
                self.label_10.setText(QCoreApplication.translate("Dialog", u" Time: 00:00AM/PM", None))
                index += 1
                if index > 3:
                    index = 0
                    row += 1

    def transform_day_to_index(self, day):
        # Define the mapping of days to indices
        day_to_index = {
            "Mon": 0,
            "Tue": 1,
            "Wed": 2,
            "Thu": 3,
            "Fri": 4,
            "Sat": 5,
            "Sun": 6
        }

        # Return the corresponding index for the day
        return day_to_index.get(day, "Invalid day")



    def switch_to_teacher_page(self, teacher):
        """Switch to the teacher's detail page."""
        self.stackedWidget.setCurrentIndex(6)  # Assume teacher details are shown in index 6
        self.label_teacher_name.setText(f"{teacher['Name']} {teacher['Surname']}")
        self.label_teacher_class.setText(f"Class: {teacher['ClassName']}")
        self.label_teacher_group.setText(f"Group: {teacher['GroupName']}")
        self.label_teacher_time.setText(f"Time: {teacher['Time']}")



    def create_student_buttons(self):
        """Re-create student buttons with updated data."""
        index = 0
        row = 0
        width = 161
        height = 201
        padding = 40
        spacing = 20

        for student in self.students:
            # Combine Name and Surname for the button text
            student_name = f"{student['Name']} {student['Surname']}"

            # Create a button for each student with both Name and Surname
            button = QPushButton(parent=self.Students, text=student_name)
            button.setStyleSheet(u"background-color: #8DB7F5;\n"
                                 "border-radius: 10px;\n"
                                 "font-size:15px;\n")

            # Position the button
            button.setGeometry(QRect(30 + (width + padding) * index, 30 + (height + spacing) * row, width, height))

            # Percentage label inside the button
            procent_label = QLabel(parent=button, text="0%")
            procent_label.setStyleSheet("font-size: 12px; color: black;")
            procent_width = 30
            procent_height = 20
            procent_x = (button.width() - procent_width) // 2
            procent_y = button.height() - procent_height - 10
            procent_label.setGeometry(procent_x, procent_y, procent_width, procent_height)

            # Store the button in the dictionary using the student's full name (Name + Surname)
            self.student_buttons[student_name] = {'button': button, 'label': procent_label}

            # Connect the button click to a function to show student details
            button.clicked.connect(lambda _, s=student: self.switch_to_page_with_present(s))



            # Update index and row for button positioning
            index += 1
            if index > 3:
                index = 0
                row += 1

    def switch_to_search_Page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_classes_Page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_setting_Page(self):
        self.stackedWidget.setCurrentIndex(1)

    #Button with upload page
    def switch_to_upload_Page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_upload_Page2(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_class_with_students(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_class_back(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_page_with_present(self, student):
        """Switch to the page with the selected student's details."""
        global url
        self.current_student_key = student['id']
        print(student)

        #Page with students
        if student:
            self.stackedWidget.setCurrentIndex(7)
            # Update the buttons with student info
            self.pushButton_57.setText(QCoreApplication.translate("Dialog", student["Name"] + " " +student["Surname"] , None))
            self.pushButton_58.setText(QCoreApplication.translate("Dialog", student["Group"], None))
            self.pushButton_61.setText(QCoreApplication.translate("Dialog", student["id"], None))
            response = requests.get(url[:-1]+"/api/files/4i53pyqjukl7lxi/" + f"{student['id']}/"+f"{student['Photo']}")
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            if pixmap.isNull():
                print("Failed to load image.")
            else:
                self.Original_Picture_ID.setPixmap(pixmap)  # Assuming label_38 is a QLabel in your UI

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
        # Since we are no longer using a server, simulate the result
        print(f"Simulating image processing for {image_path}")

        # Display the image on label_38
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Failed to load image.")
        else:
            self.label_38.setPixmap(pixmap)  # Assuming label_38 is a QLabel in your UI

        # Simulate some dummy result data for students
        simulated_result = {
            "John Doe": "95",
            "Jane Smith": "80",
            "Alice Brown": "70",
            "Bob White": "60"
        }

        # Update each button's label with the new percentage
        for student_Name, procent_value in simulated_result.items():
            if student_Name in self.student_buttons:
                button_info = self.student_buttons[student_Name]
                button_info['label'].setText(procent_value + "%")  # Update the label with the percentage

        # Switch to the next screen or view (index 2)
        self.stackedWidget.setCurrentIndex(4)
