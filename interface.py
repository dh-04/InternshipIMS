"""
    Name: interface.py
    Author: Rajshankar M
    Description: Python script file that displays the GUI (Graphic User Interface) for the Module
"""

import sys
from PySide6 import QtCore, QtWidgets, QtGui


class HomeView(QtWidgets.QWidget):
    """
        HomeView class that returns the default view whenever the application is launched.
    """
    def __init__(self):
        """
            __init__ constructor
            text: Text label from QLabel that displays text in the GUI
            layout: Box layout of QtWidgets
        """
        super().__init__()
        self.text = QtWidgets.QLabel("Hello World!",
                                     alignment = QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)


class CheckOutView(QtWidgets.QWidget):
    """
       TODO: Checkout view that allows the user to check items out of the stock.
    """
    pass


class PrintableView(QtWidgets.QWidget):
    """
        TODO: Generates a printable view of various statistics. WIP.
    """
    pass


class ManualEntryView(QtWidgets.QWidget):
    """
        TODO: View that allows user to manually change the stock.
    """
    pass


class SearchView(QtWidgets.QWidget):
    """
        TODO: View that allows user to search for a particular item based on material code, material description.
    """
    pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = HomeView()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())