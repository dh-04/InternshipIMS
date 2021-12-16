import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui, QtCore
from ui import Ui_Form


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.processing)

    def processing(self):
        lbl = self.ui.label_5
        lbl.setGeometry(QtCore.QRect(520, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        lbl.setFont(font)
        print("Here")
        self.ui.lineEdit.setText = ""
        self.ui.lineEdit_2.setText = ""
        self.ui.lineEdit_3.setText = ""
        lbl.setText("Stock updated successfully.")


def main():
    app = QApplication(sys.argv)
    disp = MainWindow()
    disp.setWindowTitle("Inventory Management System")
    disp.resize(1366,800)
    disp.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
