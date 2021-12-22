import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtCore
from prodview_gui import Ui_MainWindow
import manualentry
import bulkupload

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.manualentry_disp = []
        self.bulkentry_disp = []
        self.conn = []
        self.cur = []
        self.ui.tableWidget.setColumnWidth(0, 230)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 133)
        self.ui.tableWidget.setRowCount(self.getrowcount())
        self.loaddata()
        self.ui.pushButton.clicked.connect(self.redirect_manual)
        self.ui.pushButton_2.clicked.connect(self.loaddata)
        self.ui.pushButton_3.clicked.connect(self.close_win)
        self.ui.pushButton_4.clicked.connect(self.redirect_bulk)

    def close_win(self):
        self.close()

    def redirect_manual(self):
        self.loaddata()
        self.close()
        self.manualentry_disp = manualentry.MainWindow()
        self.manualentry_disp.showFullScreen()

    def redirect_bulk(self):
        self.loaddata()
        self.close()
        self.bulkentry_disp = bulkupload.MainWindow()
        self.bulkentry_disp.showFullScreen()

    def getrowcount(self):
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = 'SELECT COUNT(*) FROM inventory;'
        rowcount = self.cur.execute(query)
        res = []
        for row in rowcount:
            res = int(row[0])
        self.cur.close()
        self.conn.close()
        return res

    def loaddata(self):
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = 'SELECT * FROM inventory;'
        trow = 0
        rows = self.cur.execute(query)
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