from PyQt6.QtWidgets import QApplication
from PyQt6 import uic


Form, Windows = uic.loadUiType('form.ui')
win = QApplication([])
windows = Windows()
form = Form()
form.setupUi(windows)
# Это место для кода

def clear():
    form.a.setText('0')
    form.c.setValue(5)
    form.tochnost.setValue(5)

clear()
form.pushButton_2.clicked.connect(clear)


windows.show()
win.exec()