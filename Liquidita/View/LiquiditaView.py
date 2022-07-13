from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Liquidita.View.LiquiditaHomeUI import LiquiditaHomeUI


class LiquiditaView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.homeLidquidita = LiquiditaHomeUI()

    def getInserisciLineEdit(self):

        idSocio = self.homeLidquidita.idsocio.text()
        if idSocio != "":
            if idSocio.isdigit() is False :
                return 0

        idFornitore = self.homeLidquidita.idfornitore.text()
        if idFornitore != "":
            if idFornitore.isdigit() is False:
                return 0

        idLiquidita = self.homeLidquidita.note.text()
        if idLiquidita.isdigit() is False :
            return 0

        costo = self.homeLidquidita.importo.text()
        if costo.isdigit() is False :
            return 0

        categoria = self.homeLidquidita.categorie.currentText()
        tipologia = self.homeLidquidita.tipologia.currentText()


        return idSocio, idFornitore, idLiquidita, costo, categoria, tipologia


    def enableFields(self):
        print("dentro")
        tipologia = self.homeLidquidita.tipologia.currentText()
        idFornitore = self.homeLidquidita.idfornitore
        idSocio = self.homeLidquidita.idsocio

        if tipologia == "ENTRATA":
            idFornitore.setEnabled(False)
            idSocio.setEnabled(True)
        else:
            idSocio.setEnabled(False)
            idFornitore.setEnabled(True)



    def warningMessageType(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE! ", " Alcuni campi devono essere numerici!")


    def warningMessageExisting(self):
        self.message = QMessageBox.warning(self, "ATTENZIONE! ", " L'id del socio o del fornitore inserito non corrispondono ad alcun socio o fornitore!")
