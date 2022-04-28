from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Sicurezza.GestioneUtente.View.EliminaUtenteUI import EliminaUtenteUI
from Sicurezza.GestioneUtente.View.GestioneUtentiUI import GestioneUtentiUI
from Sicurezza.GestioneUtente.View.InserisciUtenteUI import InserisciUtenteUI
from Sicurezza.GestioneUtente.View.RicercaCFCreazioneUI import RicercaCFCreazioneUI


class UtentiView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.homeUtente = GestioneUtentiUI()
        self.ricercaCf = RicercaCFCreazioneUI()
        self.inserisciUtente = InserisciUtenteUI()
        self.eliminaUtente = EliminaUtenteUI()

    def warnElimina(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Non esiste alcun utente con quel nome utente da eliminare")

    def correttoEliminazione(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "L'utente è stato eliminato con successo!")

    def warnRicerca(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Non esiste alcun dipendente a cui è associato quel codice fiscale")

    def correttoInserimento(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "Hai inserito con successo un nuovo utente")

    def warnInserimento(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Le password non corrispondono!")

    def warnUtenteEsistente(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Questo nome utente è già stato assegnato ad un altro dipendente")