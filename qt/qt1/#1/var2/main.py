import sys
from ui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from math import cos, sin


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
form = Ui_MainWindow()
form.setupUi(MainWindow)
# form.a.setValidator(QtGui.QDoubleValidator())


def clear():
    form.x.setValue(0)
    form.y.setValue(0)
    form.tochnost.setValue(1)


def res():
    x = form.x.value()
    y = form.y.value()
    t = form.tochnost.value()
    z1 = cos(x) ** 4 + sin(y) ** 2 + (1/4) * sin(2*x) ** 2 - 1
    z2 = sin(y+x) * sin(y - x)
    form.z1.setText(f'{round(z1, t)}')
    form.z2.setText(f'{round(z2, t)}')
    

clear()
form.pushButton_2.clicked.connect(clear)
form.pushButton.clicked.connect(res)




MainWindow.show()
sys.exit(app.exec())