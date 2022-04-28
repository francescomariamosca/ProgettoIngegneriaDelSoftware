from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from Liquidita.View.LiquiditaView import LiquiditaView


class ControllerLiquidita(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.liquditaView = LiquiditaView()

    def passaLiquidita(self):
        #inizializzazione interfaccia liquidita
        self.window = QtWidgets.QMainWindow()
        self.liquditaView.homeLidquidita.setupUi(self.window)
        self.window.show()

        #funzioni per tornare alla home
        self.liquditaView.homeLidquidita.tornahome.clicked.connect(self.window.close)
        self.liquditaView.homeLidquidita.tornahome.clicked.connect(self.home.mostra)