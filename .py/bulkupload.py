import sys
import sqlite3
import ntpath
import csv
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui, QtCore
import pandas as pd
from bulkupload_gui import Ui_MainWindow
import manualentry
import prodview

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.getfiles)
        self.ui.pushButton_2.clicked.connect(self.close_win)
        self.ui.pushButton_3.hide()
        self.ui.pushButton_4.clicked.connect(self.redirect)
        self.prodview_disp = prodview.MainWindow()
        self.ui.label_4.hide()
        self.conn = []
        self.cur = []
        self.ids = []

    def redirect(self):
        self.close()
        self.prodview_disp.showFullScreen()

    def process(self):
        self.ui.label_5.setText("Upload successful.")
        self.ui.pushButton_3.hide()

    def loaddata(self):
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = 'SELECT mat_code FROM inventory;'
        self.ids = list(self.cur.execute(query))
        self.conn.close()

    def incrementstock(self, prod_id, increasestock):
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = f"SELECT * FROM inventory WHERE mat_code= '{prod_id}'"
        prod = self.cur.execute(query)
        index = []
        currstock = []
        for el in list(prod):
            index = el[0]
            currstock = el[4]
        updatequery =  f"UPDATE inventory SET stock = {currstock+increasestock} WHERE id = {index}"
        self.cur.execute(updatequery)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def newentry(self, row):
        print("Entering this function")
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = f"INSERT INTO inventory (mat_desc, mat_code, variant, stock) VALUES ('{row[1]}', '{row[2]}', '{row[3]}', '{int(row[4])}');"
        print(f"Executing command {query}")
        self.cur.execute(query)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def getfiles(self):
        self.ui.label_5.clear()
        self.ui.pushButton_3.hide()
        title = "Open file"
        filter = "Excel Files(*.csv *.xlsx *.xls)"
        f = QFileDialog.getOpenFileName(self, title, "..\\" ,filter)
        try:
            with open(f[0], 'r') as file:
                dr = csv.DictReader(file)
                to_db = [(row['index'], row['prod_name'], row['prod_id'], row['variant'], row['stock']) for row in dr]
                self.loaddata()
                flag1 = True
                flag2 = False
                idCheck = False
                for id in self.ids:
                    for i in to_db:
                        if id[0] == i[2]:
                            flag2 = True
                            idCheck = True
                            self.incrementstock(i[2],int(i[4]))
                for i in to_db:
                    if i[4]:
                        if i[1] and i[2]:
                            if not idCheck:
                                self.newentry(i)
                                flag2 = True
                    else:
                        flag1 = False
            self.ui.label_4.setText(ntpath.basename(f[0]))
            self.ui.label_4.show()
            self.ui.pushButton.setText("Re-upload")
            if flag1 and flag2:
                self.ui.pushButton_3.show()
                self.ui.pushButton_3.clicked.connect(self.process)
            elif not flag1:
                self.ui.label_5.setText("One or more of the entries were invalid. Please check again.")
            else:
                self.ui.label_5.setText("File upload unsuccessful. Please try again.")
        except FileNotFoundError:
            self.ui.label_5.setText("File upload unsuccessful. Please try again.")


    def close_win(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    disp = MainWindow()
    disp.setWindowTitle("Inventory Management System")
    disp.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()