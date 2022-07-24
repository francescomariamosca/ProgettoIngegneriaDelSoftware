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

    def typeWarning(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE! ", "Alcuni campi devono essere numerici")


    def getInserisciLineEdit(self):
        cf = self.inserisciDip.cf.text()
        nome = self.inserisciDip.nomedip.text()
        cognome = self.inserisciDip.congomedip.text()
        citta = self.inserisciDip.cittadip.text()

        tel = self.inserisciDip.cellularedip.text()
        if tel.isdigit() is False and tel !="":
            return 0
        mansione = self.inserisciDip.mansionedip.text()
        ore = self.inserisciDip.oredip.text()
        if ore.isdigit() is False:
            return 0
        stip = self.inserisciDip.stipendiodip.text()
        if stip.isdigit() is False:
            return 0
        username = self.inserisciDip.usernamedip.text()

        return cf, nome, cognome, citta, tel, mansione, ore, stip, username

    def getEliminaLineEdit(self):
        cf = self.eliminaDip.ricercacf.text()
        return cf

    def getRicercaLineEdit(self):
        cf = self.ricercaDip.cf.text()
        return cf

    def setModificaLineEdit(self, cf, nome, cognome, citta, tel, mansione, ore, stip, username):
        self.modificaDip.cf.setText(cf)
        self.modificaDip.nomedip.setText(nome)
        self.modificaDip.congomedip.setText(cognome)
        self.modificaDip.cittadip.setText(citta)
        self.modificaDip.cellularedip.setText(tel)
        self.modificaDip.mansionedip.setText(mansione)
        self.modificaDip.oredip.setText(ore)
        self.modificaDip.stipendiodip.setText(stip)
        self.modificaDip.usernamedip.setText(username)

    def getModificaLineEdit(self):
        cf = self.modificaDip.cf.text()
        nome = self.modificaDip.nomedip.text()
        cognome = self.modificaDip.congomedip.text()
        citta = self.modificaDip.cittadip.text()

        telefono = self.modificaDip.cellularedip.text()
        if telefono.isdigit() is False and telefono != "":
            return 0
        mansione = self.modificaDip.mansionedip.text()

        ore = self.modificaDip.oredip.text()
        if ore.isdigit() is False:
            return 0
        stip = self.modificaDip.stipendiodip.text()
        if stip.isdigit() is False:
            return 0
        username = self.modificaDip.usernamedip.text()

        return cf, nome, cognome, citta, telefono, mansione, ore, stip, username