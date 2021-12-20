import sys
import sqlite3
import ntpath
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui, QtCore
import pandas as pd
from bulkupload_gui import Ui_MainWindow
import manualentry

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.getfiles)
        self.ui.pushButton_2.clicked.connect(self.close_win)
        self.ui.pushButton_3.hide()
        self.ui.label_4.hide()
        self.df = []
        self.ui.pushButton_3.clicked.connect(self.process)

    def process(self):
        self.ui.label_5.setText("Upload successful.")
        self.ui.pushButton_3.hide()
        #Take the dataframe and upload it to the SQL Database
            #Check for errors, check for pre-existing entries and just update stock in that case.

    def getfiles(self):
        title = "Open file"
        filter = "Excel Files(*.csv *.xlsx *.xls)"
        f = QFileDialog.getOpenFileName(self, title, "../" ,filter)
        try:
            self.df = pd.read_csv(f[0])
            self.ui.label_4.setText(ntpath.basename(f[0]))
            self.ui.label_4.show()
            self.ui.pushButton.setText("Re-upload")
            self.ui.pushButton_3.show()
        except Error:
            print("File upload unsuccessful. Please try again.")


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