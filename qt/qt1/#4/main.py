import sys
from ui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
form = Ui_MainWindow()
form.setupUi(MainWindow)

def clear():
    form.r.setValue(0)
    form.y.setValue(0)
    form.x.setValue(0)
    form.label.setText('результат')

def res():
    r = form.r.value()
    x = form.x.value()
    y = form.y.value()

    if x > 0:
        if y**2 + x**2 < r**2:
            form.label.setText('попадание')
        else:
            form.label.setText('молоко')
    else:
        if abs(y) < r and abs(x) < r and abs(x) < abs(y):
            form.label.setText('попадание')
        else:
            form.label.setText('молоко')

clear()
form.res.clicked.connect(res)
form.clear.clicked.connect(clear)

MainWindow.show()
sys.exit(app.exec())