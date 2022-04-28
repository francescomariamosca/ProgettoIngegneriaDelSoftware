from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Fornitori.View.EliminaFornitoreUI import EliminaFornitoreUI
from Fornitori.View.HomeFornitoriUI import HomeFornitoriUI
from Fornitori.View.InserisciFornitoreUI import InserisciFornitoreUI
from Fornitori.View.ModificaFornitoreUI import ModificaFornitoreUI
from Fornitori.View.RicercaModificaFornitoreUI import RicercaModificaFornitoreUI


class FornitoriView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.homeFornitori = HomeFornitoriUI()
        self.inserisciFornitore = InserisciFornitoreUI()
        self.eliminaFornitore = EliminaFornitoreUI()
        self.ricercaFornitore = RicercaModificaFornitoreUI()
        self.modificaFornitore = ModificaFornitoreUI()

    def messageCorrettoInserimento(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " Fornitore inserito correttamente! ")

    def messageWarningInserimento(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", "Stai inserendo un fornitore che ha lo stesso id di un altro!")

    def messageCorrettaEliminazione(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " Il fornitore è stato eliminato correttamente! ")

    def messageWarningEliminazione(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", " Nessun fornitore corrisponde al codice fiscale inserito! ")

    def messageCorrettaModifica(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " Il fornitore è stato modificato con successo! ")

    def messageWarningModifica(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", " Impossibile effettuare la modifica! ")
