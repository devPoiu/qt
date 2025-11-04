import sys
from ui import Ui_Form
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtWidgets import QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import math
from PyQt6.QtCore import QStringListModel


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
form = Ui_Form()
form.setupUi(Form)

def clear():
    form.start.setValue(-10)
    form.finish.setValue(8)
    form.step.setValue(1)
    modelTable.clear()
    data = []
    modelList.setStringList(data)


def res():
    x = form.start.value()
    finish = form.finish.value()
    step = round(form.step.value(), 1)
    data = ['I-------I-------I',
            'I    X     I     Y     I',
            'I-------I-------I']
    modelTable.setHorizontalHeaderLabels(['X', 'Y'])

    while x <= finish:
        if x >= -10 and x < -6:
            y = math.sqrt((x + 10) * (-x - 6)) - 2
        if x >= -6 and x < 2:
            y = x / 2 + 1
        if x >= 2 and x < 6:
            y = 0
        if x >= 6:
            y = (x - 6)**2
            
        add_row(str(round(x, 1)), str(round(y, 1)))
        data.append(f'{round(x, 1)}  I  {round(y, 1)}')
        x += step

    modelList.setStringList(data)


def add_row(x, y):
        item1 = QStandardItem(x)
        item2 = QStandardItem(y)
        modelTable.appendRow([item1, item2])

modelList = QStringListModel()
form.listView.setModel(modelList)

modelTable = QStandardItemModel()
form.tableView.setModel(modelTable)


form.res.clicked.connect(res)
form.clear.clicked.connect(clear)

Form.show()
sys.exit(app.exec())