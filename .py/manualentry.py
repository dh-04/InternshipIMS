import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui, QtCore
from manualentry_gui import Ui_Form
import prodview


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ids = []
        self.conn = []
        self.cur = []
        self.loaddata()
        self.prodview_disp = prodview.MainWindow()
        self.ui.pushButton.clicked.connect(self.processing)
        self.ui.pushButton_2.clicked.connect(self.redirect)

    def redirect(self):
        self.close()
        self.prodview_disp.showFullScreen()


    def loaddata(self):
        self.conn = sqlite3.connect("../db/inventory.db")
        self.cur = self.conn.cursor()
        query = 'SELECT mat_code FROM inventory;'
        self.ids = list(self.cur.execute(query))
        self.conn.close()


    def incrementstock(self, prod_id):
        self.conn = sqlite3.connect("../db/inventory.db")
        self.cur = self.conn.cursor()
        query = f"SELECT * FROM inventory WHERE mat_code= '{prod_id}'"
        prod = self.cur.execute(query)
        index = []
        currstock = []
        for el in list(prod):
            index = el[0]
            currstock = el[4]
        updatequery =  f"UPDATE inventory SET stock = {currstock+1} WHERE id = {index}"
        self.cur.execute(updatequery)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def processing(self):

        lbl = self.ui.label_5
        lbl.setGeometry(QtCore.QRect(520, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        lbl.setFont(font)
        input = self.ui.lineEdit_2.text()
        flag = False
        if not input:
            flag = False
        for id in self.ids:
            if input == id[0]:
                flag = True
        if not flag:
            lbl.setText("Please enter a valid Product ID")
            self.loaddata()
        else:
            #Increment stock of the given prod. ID.
            self.incrementstock(input)
            lbl.setText("Stock updated successfully.")
            self.loaddata()


def main():
    app = QApplication(sys.argv)
    disp = MainWindow()
    disp.setWindowTitle("Inventory Management System")
    disp.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
