from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Dipendenti.View.EliminaDipUI import EliminaDipUI
from Dipendenti.View.HomeGestioneDipUI import HomeGestioneDipUI
from Dipendenti.View.InserisciDipUI import InserisciDipUI
from Dipendenti.View.ModificaDipUI import ModificaDipUI
from Dipendenti.View.RicercaDipendenteUI import RicercaDipendenteUI


class DipendentiView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.homeDipendenti = HomeGestioneDipUI()
        self.inserisciDip = InserisciDipUI()
        self.eliminaDip = EliminaDipUI()
        self.modificaDip = ModificaDipUI()
        self.ricercaDip = RicercaDipendenteUI()

    def messageInserimentoCorretto(self):
        self.corretto = QMessageBox.information(self, " PERFETTO!", "Dipendente inserito correttamente!")

    def messageWarningInserimento(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", "Stai inserendo un dipendente che ha lo stesso codice fiscale di un altro!")

    def messageEliminazioneAvvenuta(self):
        self.messElimina = QMessageBox.information(self, "PERFETTO!", "Dipendente eliminato!")

    def messageWarningEliminazione(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", "Il dipendente che stai cercando di Eliminare non esiste!")

    def messageWarningRicerca(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", "Il codice fiscale che stai inserendo non combacia con alcun dipendente!")

    def messageCorrettoModify(self):
        self.message = QMessageBox.information(self, " ATTENZIONE! ",  "Modifica avvenuta con successo!")

    def messageWarningModify(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", "Impossibile effettuare la modifica!")


    def getInserisciLineEdit(self):
        cf = self.inserisciDip.cf.text()
        nome = self.inserisciDip.nomedip.text()
        cognome = self.inserisciDip.congomedip.text()
        citta = self.inserisciDip.cittadip.text()
        tel = self.inserisciDip.cellularedip.text()
        mansione = self.inserisciDip.mansionedip.text()
        ore = self.inserisciDip.oredip.text()
        stip = self.inserisciDip.stipendiodip.text()
        username = self.inserisciDip.usernamedip.text()

        return cf, nome, cognome, citta, tel, mansione, ore, stip, username