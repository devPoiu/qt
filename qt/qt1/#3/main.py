# Цифры в пятизначном числе. Дано пятизначное число (10000–99999).
# Определить, входит ли в него цифра n (0–9) или первая цифра чётная. если n
# входит, вывести все позиции (с 1), где она встречается. Если первая чётная,
# посчитать количество чётных цифр в числе. Если ни то ни другое, вывести
# сумму всех цифр.

import sys
from ui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import random


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
form = Ui_MainWindow()
form.setupUi(MainWindow)

def clear():
    form.poz.setText('')
    form.kol.setText('')
    form.summ.setText('')
    form.n.setValue(0)
    form.chislo.setValue(1000)

def res():
    form.poz.setText('')
    form.kol.setText('')
    form.summ.setText('')
    n = form.n.value()
    strN = str(n)
    chislo = form.chislo.value()
    strChislo = str(chislo)
    q = ''
    flag = 0
    if strN in str(chislo):
        for i in range(len(strChislo)):
            if strChislo[i] == strN:
                q += f'{i + 1} '
        form.poz.setText(q)
        flag += 1
    q = 0
    if int(strChislo[0]) % 2 == 0:
        for i in strChislo:
            if int(i) % 2 == 0:
                q += 1
        form.kol.setText(str(q))
        flag += 1
    if flag == 0:
        form.poz.setText('')
        form.kol.setText('')
        q = 0
        for i in strChislo:
            q += int(i)
        if q == 0: q = ''
        form.summ.setText(str(q))

def rand():
    form.chislo.setValue(random.randint(1000, 9999))


clear()
form.random.clicked.connect(rand)
form.pushButton.clicked.connect(res)

MainWindow.show()
sys.exit(app.exec())