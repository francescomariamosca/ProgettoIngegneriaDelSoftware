from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Campi.View.HomePrenotazioniUI import HomePrenotazioniUI
from Campi.View.InserisciGiocatoriUI import InserisciGiocatoriUI
from Campi.View.VistaHomeCampiUI import VistaHomeCampiUI


class CampiView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.vistaPrenotazioni = HomePrenotazioniUI()
        self.vistaCampi = VistaHomeCampiUI()
        self.inserisciGiocatori = InserisciGiocatoriUI()

    def correttaCancellazione(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " Hai eliminato la prenotazione con successo!")

    def warnPrenotazione(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", " Il campo che stai cercando di prenotare è già occupato!")

    def warnInserimento(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE! ", " Per prenotare un campo devi inserire almeno un giocatore")

    def correttoInserimento(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " La prenotazione è stata inserita con successo")