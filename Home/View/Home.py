from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Home.View.VistaHome import VistaHome


class Home(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.homeUI = VistaHome(self)

    def mostra(self):
        self.window = QtWidgets.QMainWindow()
        self.homeUI.setupUi(self.window)
        self.window.show()
        self.homeUI.dipendenti.clicked.connect(self.window.close)
        self.homeUI.soci.clicked.connect(self.window.close)
        self.homeUI.sicurezza.clicked.connect(self.window.close)
        self.homeUI.campi.clicked.connect(self.window.close)




