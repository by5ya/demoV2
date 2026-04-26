from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from openpyxl.styles.builtins import title


def info_ok(text):
    message = QMessageBox(QMessageBox.Icon.Information, "Информация", text)
    message.addButton("Ок", QMessageBox.ButtonRole.AcceptRole)
    message.exec()
    return

def warn_ok(text):
    message = QMessageBox(QMessageBox.Icon.Warning, "Предупреждение", text)
    message.addButton("Ок", QMessageBox.ButtonRole.AcceptRole)
    message.exec()
    return

def warn_yes_no(text):
    message = QMessageBox(QMessageBox.Icon.Warning, "Предупреждение", text)
    btn1 = message.addButton("Да", QMessageBox.ButtonRole.AcceptRole)
    message.addButton("Нет", QMessageBox.ButtonRole.RejectRole)
    message.exec()
    return message.clickedButton() == btn1
