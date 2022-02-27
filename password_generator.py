import random
import string
import pyperclip
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIntValidator


qt_file = "password_generator.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_file)


def except_hook(cls, exception, traceback):  # PyQt6 doesn't output traceback errors by default
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook


def password_generator(num_of_letters: int, num_of_special: int, num_of_digits: int) -> str:
    password = ""
    numbers = [str(i) for i in range(10)]
    for i in range(0, num_of_digits):
        password += random.choice(numbers)
    letters = list(string.ascii_lowercase)
    letters += [i.upper() for i in letters]  # Appends a list of capital letters
    for i in range(0, num_of_letters):
        password += random.choice(letters)
    special = ["#", "@", "$", "&", "%", "=", "*", "!", "+", "_", "^", "(", ")", "/", "?", "-"]
    for i in range(0, num_of_special):
        password += random.choice(special)
    p = list(password)
    for i in range(0, 10):
        random.shuffle(p)
    password = "".join(p)
    return password


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.button_generate.clicked.connect(self.generate_password)
        self.button_copy.clicked.connect(self.copy_password)
        self.setWindowTitle("Password generator")
        # Styling
        self.setStyleSheet("background-color: rgb(35, 35, 35)")
        style_sheet_1 = "color: rgb(255, 255, 255); background-color: rgb(168, 22, 43)"
        style_sheet_2 = "color: rgb(255, 255, 255); background-color: rgb(47, 54, 205)"
        style_sheet_3 = "color: rgb(255, 255, 255); background-color: rgb(223, 56, 3)"
        self.button_generate.setStyleSheet(style_sheet_1)
        self.button_copy.setStyleSheet(style_sheet_1)
        self.label_1.setStyleSheet(style_sheet_2)
        self.label_letters.setStyleSheet(style_sheet_2)
        self.label_specials.setStyleSheet(style_sheet_2)
        self.label_digits.setStyleSheet(style_sheet_2)
        self.num_of_letters.setStyleSheet(style_sheet_3)
        self.num_of_specials.setStyleSheet(style_sheet_3)
        self.num_of_digits.setStyleSheet(style_sheet_3)
        self.line_edit_password.setStyleSheet("color: rgb(0, 100, 80); background-color: white")
        # Default values
        self.num_of_letters.setText("10")
        self.num_of_specials.setText("10")
        self.num_of_digits.setText("10")
        # Limit input size
        self.num_of_letters.setValidator(QIntValidator(1, 40, self))
        self.num_of_specials.setValidator(QIntValidator(1, 40, self))
        self.num_of_digits.setValidator(QIntValidator(1, 40, self))

    def generate_password(self):
        try:
            num_of_letters = self.num_of_letters.text()
            num_of_specials = self.num_of_specials.text()
            num_of_digits = self.num_of_digits.text()
            password = password_generator(int(num_of_letters), int(num_of_specials), int(num_of_digits))
            self.line_edit_password.setText(password)
        except ValueError:
            self.line_edit_password.setText("")
        except TypeError:
            self.line_edit_password.setText("")

    def copy_password(self):
        password = self.line_edit_password.text()
        pyperclip.copy(password)  # Copies password to clipboard


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
