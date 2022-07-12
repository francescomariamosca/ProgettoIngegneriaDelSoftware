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

    def getTable(self):
        campo = self.vistaCampi.setcampo.currentText()
        ora = self.vistaCampi.setora.currentText()

        return campo, ora

    def getInserisciLineEdit(self):
        g1 = self.inserisciGiocatori.G1.text()
        g2 = self.inserisciGiocatori.G2.text()
        g3 = self.inserisciGiocatori.G3.text()
        g4 = self.inserisciGiocatori.G4.text()

        return g1, g2, g3, g4
