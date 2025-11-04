import sys
from ui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import math
from math import cos, sin, tan, exp


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
form = Ui_MainWindow()
form.setupUi(MainWindow)
# form.a.setValidator(QtGui.QDoubleValidator())


def clear():
    form.a.setValue(0)
    form.b.setValue(0)
    form.tochnost.setValue(1)
    form.q.setText('q')
    form.p.setText('p')
    form.t.setText('t')
    form.c.setText('c')



def res():
    a = form.a.value()
    b = form.b.value()
    toch = form.tochnost.value()
    t = sin(b**2)**a
    print(t)
    c = (math.e)**(math.sqrt(a+b+5))
    print(c)
    p = (a*c*b)**(1/5)
    print(p)
    q = math.tan(p**t)
    form.q.setText(f'{round(q, toch)}')
    form.p.setText(f'{round(p, toch)}')
    form.t.setText(f'{round(t, toch)}')
    form.c.setText(f'{round(c, toch)}')
    

clear()
form.pushButton_2.clicked.connect(clear)
form.pushButton.clicked.connect(res)




MainWindow.show()
sys.exit(app.exec())