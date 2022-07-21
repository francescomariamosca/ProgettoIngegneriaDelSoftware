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

    def idWarn(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", "L'id del fornitore corrisponde ad un fornitore già esistente oppure non è un numero!")

    def messageCorrettaEliminazione(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " Il fornitore è stato eliminato correttamente! ")

    def messageWarningEliminazione(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", " Nessun fornitore corrisponde al codice fiscale inserito! ")

    def messageCorrettaModifica(self):
        self.message = QMessageBox.information(self, " PERFETTO! ", " Il fornitore è stato modificato con successo! ")

    def messageWarningModifica(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", " Impossibile effettuare la modifica! ")

    def messageWarningRicerca(self):
        self.message = QMessageBox.warning(self, " ATTENZIONE! ", " Nessun fornitore corrisponde all'id inserito! ")

    def getInserisciFornitoreLineEdit(self):
        id_fornitore = self.inserisciFornitore.idfornitore.text()
        if id_fornitore.isdigit() is False and id_fornitore != "":
            return 0
        nome = self.inserisciFornitore.nomeazienda.text()
        email = self.inserisciFornitore.emailazienda.text()
        telefono = self.inserisciFornitore.telefonoazienda.text()
        settore = self.inserisciFornitore.settore.text()
        citta = self.inserisciFornitore.cittazienda.text()
        via = self.inserisciFornitore.viazienda.text()

        return id_fornitore, nome, email, telefono, settore, citta, via

    def getEliminaFornitoreLineEdit(self):
        id_forn = self.eliminaFornitore.ricercaidfornitore.text()
        return id_forn

    def getRicercaFornitoreLineEdit(self):
        id_forn = self.ricercaFornitore.ricercaidfornitore.text()
        return id_forn

    def setTextModifica(self, id, nome, email, telefono, settore, citta, via):
        self.modificaFornitore.idfornitore.setText(id)
        self.modificaFornitore.nomeazienda.setText(nome)
        self.modificaFornitore.emailazienda.setText(email)
        self.modificaFornitore.telefonoazienda.setText(telefono)
        self.modificaFornitore.settore.setText(settore)
        self.modificaFornitore.cittazienda.setText(citta)
        self.modificaFornitore.viazienda.setText(via)

    def getModificaLineEdit(self):
        id_forn = self.modificaFornitore.idfornitore.text()
        nome = self.modificaFornitore.nomeazienda.text()
        email = self.modificaFornitore.emailazienda.text()
        tel = self.modificaFornitore.telefonoazienda.text()
        settore = self.modificaFornitore.settore.text()
        citta = self.modificaFornitore.cittazienda.text()
        via = self.modificaFornitore.viazienda.text()

        return id_forn, nome, email, tel, settore, citta, via
