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

    def warnMaxOneUser(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Può essere assegnato massimo un dipendente ad ogni utente")

    def getEliminaLineEdit(self):
        nome_utente = self.eliminaUtente.ricercauser.text()
        return nome_utente

    def getRircercaLineEdit(self):
        cf = self.ricercaCf.ricercacfdip.text()
        return cf

    def getInsertLineEdit(self):
        username = self.inserisciUtente.username.text()
        password = self.inserisciUtente.password.text()

        return username, password

    def checkPasswords(self):
        password = self.inserisciUtente.password.text()
        confPass = self.inserisciUtente.confermapassword.text()

        if password == confPass:
            return True
        else:
            return False

