from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Campi.View.HomePrenotazioniUI import HomePrenotazioniUI
from Campi.View.VistaHomeCampiUI import VistaHomeCampiUI


class CampiView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.vistaPrenotazioni = HomePrenotazioniUI()
        self.vistaCampi = VistaHomeCampiUI()