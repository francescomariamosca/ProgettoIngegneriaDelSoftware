from PyQt5.QtWidgets import QMainWindow

from Liquidita.View.LiquiditaHomeUI import LiquiditaHomeUI


class LiquiditaView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.homeLidquidita = LiquiditaHomeUI()