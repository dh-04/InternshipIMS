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
        self.ui.pushButton_3.clicked.connect(self.close_win)

    def close_win(self):
        self.close()

    def redirect(self):
        self.close()
        self.prodview_disp.showFullScreen()


    def loaddata(self):
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = 'SELECT mat_code FROM inventory;'
        self.ids = list(self.cur.execute(query))
        self.conn.close()


    def incrementstock(self, prod_id, stock):
        #print(stock)
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = f"SELECT * FROM inventory WHERE mat_code= '{prod_id}'"
        prod = self.cur.execute(query)
        index = []
        currstock = []
        for el in list(prod):
            index = el[0]
            currstock = el[4]
        updatequery =  f"UPDATE inventory SET stock = {currstock+stock} WHERE id = {index}"
        self.cur.execute(updatequery)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def newentry(self, row):
        print("Entering this function")
        self.conn = sqlite3.connect("..\\db\\inventory.db")
        self.cur = self.conn.cursor()
        query = f"INSERT INTO inventory (mat_desc, mat_code, variant, stock) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{int(row[3])}');"
        print(f"Executing command {query}")
        self.cur.execute(query)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def processing(self):
        lbl = self.ui.label_5
        increase_stock = []
        flag1 = False #Checks for validity of prod id
        flag2 = True #Checks for validity of stock count
        flag3 = True #Checks for validity of prod_name.
        prod_name = self.ui.lineEdit_2.text()
        prod_id = self.ui.lineEdit_3.text()
        variant = self.ui.lineEdit_4.text()
        try:
            increase_stock = int(self.ui.lineEdit_5.text())
        except ValueError:
            flag2 = False
        if not prod_id:
            flag1 = False
        for id in self.ids:
            if prod_id == id[0]:
                while flag2:
                    self.incrementstock(prod_id, increase_stock)
                    flag1 = True
            else:
                if not prod_name:
                    flag3 = False
        if prod_name and prod_id and increase_stock:
            if not flag1:
                self.newentry([prod_name, prod_id, variant, increase_stock])
                flag1 = True
        #When all 3 flags are True the input is valid
        if flag1 and flag2 and flag3:
            lbl.setText("Stock updated successfully.")
            self.loaddata()
        # When flag1 is False, Product ID is invalid
        if not flag1 and flag2 and flag3:
            lbl.setText("Please enter a valid Product ID.")
            self.loaddata()
        # When flag2 is False, there is a problem in the stock input
        elif not flag2:
            lbl.setText("Please enter a valid stock count.")
            self.loaddata()
        #The other two possibilities are both flags being False and flag1 being False, flag2 being True.
        elif not flag3:
            lbl.setText("Please enter a valid Product Name.")
            self.loaddata()


def main():
    app = QApplication(sys.argv)
    disp = MainWindow()
    disp.setWindowTitle("Inventory Management System")
    disp.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
