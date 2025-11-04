import sys
import random
from ui import Ui_Form
from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
form = Ui_Form()
form.setupUi(Form)

def clear():
    table.clear()


def mathOper(row, col):
    if form.radioButtonU.isChecked(): return str(row * col)
    if form.radioButtonD.isChecked(): return str(round(row / col, 2))
    if form.radioButtonP.isChecked(): return str(row + col)
    if form.radioButtonM.isChecked(): return str(row - col)

def znak():
    if form.radioButtonU.isChecked(): return '*'
    if form.radioButtonD.isChecked(): return ':'
    if form.radioButtonP.isChecked(): return '+'
    if form.radioButtonM.isChecked(): return '-'


item1 = None
item2 = None

def primer():
    table.clear()
    if znak():
        if form.a.value() < form.b.value():
            a = form.a.value()
            b = form.b.value()
        else:
            b = form.a.value()
            a = form.b.value()

        if form.c.value() < form.d.value():
            c = form.c.value()
            d = form.d.value()
        else:
            d = form.c.value()
            c = form.d.value()

        global item1 
        item1 = random.randint(a, b)
        global item2
        item2 = random.randint(c, d)
        prim = f'{item1} {znak()} {item2} ='
        form.primer.setText(prim)
    else:
        form.primer.setText('Выберите знак')

def check():
    otvet = form.otvet.value()
    if mathOper(item1, item2) == str(otvet):
        form.otvet_label.setText('Верно')
        primer()
    else:
        form.otvet_label.setText('Не верно')

def res():
    table.clear()
    if form.a.value() < form.b.value():
        a = form.a.value()
        b = form.b.value()
    else:
        b = form.a.value()
        a = form.b.value()

    if form.c.value() < form.d.value():
        c = form.c.value()
        d = form.d.value()
    else:
        d = form.c.value()
        c = form.d.value()

    rowList = []
    colList = []

    for i in range(a, b+1):
        rowList.append(f'{i}')
    for i in range(c, d+1):
        colList.append(f'{i}')

    table.setHorizontalHeaderLabels(colList)
    table.setVerticalHeaderLabels(rowList)

    for row in range(a, b+1):
        arr = []
        for col in range(c, d+1):
            table.setItem(row - a, col - c, QStandardItem(mathOper(row, col)))

table = QStandardItemModel()
form.tableView.setModel(table)

form.res.clicked.connect(res)
form.clear.clicked.connect(clear)
form.get_primer.clicked.connect(primer)
form.check.clicked.connect(check)

Form.show()
sys.exit(app.exec())
