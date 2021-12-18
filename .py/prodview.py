import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtCore
from prodview_gui import Ui_MainWindow
import manualentry

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.manualentry_disp = []
        self.conn = []
        self.cur = []
        self.ui.tableWidget.setColumnWidth(0, 230)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.loaddata()
        self.ui.pushButton.clicked.connect(self.redirect)
        self.ui.pushButton_2.clicked.connect(self.loaddata)

    def redirect(self):
        self.loaddata()
        self.close()
        self.manualentry_disp = manualentry.MainWindow()
        self.manualentry_disp.showFullScreen()

    def loaddata(self):
        self.conn = sqlite3.connect("../db/inventory.db")
        self.cur = self.conn.cursor()
        query = 'SELECT * FROM inventory;'
        trow = 0
        rows = self.cur.execute(query)
        self.ui.tableWidget.setRowCount(10)
        for row in rows:
            self.ui.tableWidget.setItem(trow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(trow, 1, QtWidgets.QTableWidgetItem(row[2]))
            if row[3] is not None:
                self.ui.tableWidget.setItem(trow, 2, QtWidgets.QTableWidgetItem(row[3]))
            else:
                self.ui.tableWidget.setItem(trow, 2, QtWidgets.QTableWidgetItem("N/A"))
            self.ui.tableWidget.setItem(trow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            trow += 1
        self.cur.close()
        self.conn.close()


def main():
    app = QApplication(sys.argv)
    disp = MainWindow()
    disp.setWindowTitle("Inventory Management System")
    disp.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()