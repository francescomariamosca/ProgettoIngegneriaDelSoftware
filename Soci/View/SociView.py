from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Soci.View.EliminaSocioUI import EliminaSocioUI
from Soci.View.GestioneSociUI import GestioneSociUI
from Soci.View.InserisciSocioUI import InserisciSocioUI
from Soci.View.ModificaSocioUI import ModificaSocioUI
from Soci.View.RicercaUI import RicercaUI


class SociView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.inserisciSocio = InserisciSocioUI()
        self.homeSoci = GestioneSociUI()
        self.eliminaSocio = EliminaSocioUI()
        self.ricercaSocio = RicercaUI()
        self.modificaSocio= ModificaSocioUI()

    def sociInserimentoCorretto(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "Il cliente è stato inserito con successo")

    def sociInserimentoWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il cliente che stai cercando di inserire è già presente nel Sistema oppure alcuni dati sono mancanti!")

    def dateErrore(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il formato della data che stai inserendo non è corretto!")

    def sociEliminazioneCorretto(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "Il cliente è stato eliminato con successo!")

    def sociEliminazioneWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il dipendente che stai cercando di eliminare non esiste!")

    def sociRicercaWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il socio che stai cercando non esiste!")

    def sociModificaWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "L'id di un cliente non può essere modificato!")

    def sociModificaCorretto(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "Il socio è stato modificato con successo!")

    def scadenzaAbbonamento(self, id_socio, email):
        converted = str(id_socio)
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "L'abbonamento del socio " + converted + " sta per scadere, invo una mail a " + email)


