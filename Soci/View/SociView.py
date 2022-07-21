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

    def idWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "L'id del socio deve essere un numero non assegnato ad altri soci!")

    def dateErrore(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il formato della data che stai inserendo non è corretto!")

    def sociEliminazioneCorretto(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "Il cliente è stato eliminato con successo!")

    def sociEliminazioneWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il dipendente che stai cercando di eliminare non esiste!")

    def sociRicercaWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Il socio che stai cercando non esiste!")

    def sociModificaWarn(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "Qualcosa è andato storto con la modifica!")

    def sociModificaCorretto(self):
        self.message = QMessageBox.information(self, "PERFETTO!", "Il socio è stato modificato con successo!")

    def scadenzaAbbonamento(self, id_socio, email):
        converted = str(id_socio)
        self.message = QMessageBox.warning(self, "ATTENZIONE!", "L'abbonamento del socio " + converted + " sta per scadere, invo una mail a " + email)

    def getInserisciLineEdit(self):
        id_socio = self.inserisciSocio.idsocio.text()
        if id_socio.isdigit() is False and id_socio != "":
            return 0
        e_mail = self.inserisciSocio.email.text()
        CF = self.inserisciSocio.cfsocio.text()
        nome = self.inserisciSocio.nome.text()
        cognome = self.inserisciSocio.cognome.text()
        tel = self.inserisciSocio.telefono.text()
        data = self.inserisciSocio.datarinnovo.text()

        return id_socio, e_mail, CF, nome, cognome, tel, data

    def getEliminaLineEdit(self):
        id_socio = self.eliminaSocio.ricercaid.text()
        return id_socio

    def getRicercaLineEdit(self):
        id_socio = self.ricercaSocio.ricercaid.text()
        return id_socio

    def getModificaLineEdit(self):
        id_socio = self.modificaSocio.idsocio.text()
        e_mail = self.modificaSocio.email.text()
        CF = self.modificaSocio.cfsocio.text()
        nome = self.modificaSocio.nome.text()
        cognome = self.modificaSocio.cognome.text()
        tel = self.modificaSocio.telefono.text()
        data = self.modificaSocio.datarinnovo.text()

        return id_socio, e_mail, CF, nome, cognome, tel, data
