from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from GestioneDatabase.QueryGestioneFornitori.TableFornitori import TableFornitori
from GestioneDatabase.QueryGestioneSoci.TableSoci import TableSoci
from GestioneDatabase.QueryLiquidita.TableLiquidita import TableLiquidita
from Liquidita.View.LiquiditaView import LiquiditaView


class LogicaLiquidita(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.liquditaView = LiquiditaView()
        self.tableSoci = TableSoci()
        self.tableFornitori = TableFornitori()
        self.tableLiquidita = TableLiquidita()

    def passaLiquidita(self):
        #inizializzazione interfaccia liquidita
        self.window = QtWidgets.QMainWindow()
        self.liquditaView.homeLidquidita.setupUi(self.window)
        self.loadDataLiquidita()
        self.loadDataSoci()
        self.loadDataFornitori()
        self.window.show()

        tipologia = self.liquditaView.homeLidquidita.tipologia.currentText()
        idFornitore = self.liquditaView.homeLidquidita.idfornitore
        idSocio = self.liquditaView.homeLidquidita.idsocio

        if (tipologia == "ENTRATA"):
            idFornitore.setEnabled(False)
            idSocio.setEnabled(True)

        self.liquditaView.homeLidquidita.tipologia.activated.connect(self.liquditaView.enableFields)

        #funzioni per attivare l'inserimento di una entrata o uscita
        self.liquditaView.homeLidquidita.insentrata.clicked.connect(self.inserisciEntrata)
        self.liquditaView.homeLidquidita.eliminaEntrata.clicked.connect(self.eliminaEntrata)

        #funzioni per tornare alla home
        self.liquditaView.homeLidquidita.tornahome.clicked.connect(self.window.close)
        self.liquditaView.homeLidquidita.tornahome.clicked.connect(self.home.mostra)

    def inserisciEntrata(self):
        print("ok")
        if(self.liquditaView.getInserisciLineEdit() == 0):
            print("entrato")
            self.liquditaView.warningMessageType()
        else:
            idSocio, idFornitore, idLiquidita, costo, categoria, tipologia = self.liquditaView.getInserisciLineEdit()
            params = {'id_transazione': idLiquidita, 'tipologia': tipologia, 'categoria': categoria, 'importo': costo, 'socio':idSocio, 'fornitore':idFornitore  }
            if tipologia == "ENTRATA":
                flag = True
            else:
                flag = False
            insertQuery = self.tableLiquidita.insertQuery(params, flag)
            if insertQuery == 0:
                self.liquditaView.warningMessageExisting()
            else:
                print("enrico omosessuale")
                self.window.close()
                self.passaLiquidita()

    def eliminaEntrata(self):
        print("dentro")
        if (self.liquditaView.getDeleteLineEdit() == 0):
            self.liquditaView.warningElimina()

        else:
            id = self.liquditaView.getDeleteLineEdit()
            print(id)
            result = self.tableLiquidita.deleteQuery(id)
            print(result)
            if result == 0:
                self.liquditaView.warningElimina()
            else:
                print("concetti&Piergallini&Balloni omosessuale")
                self.window.close()
                self.passaLiquidita()

    def loadDataSoci(self):
        result = self.tableSoci.loadData()
        rowindex = 0
        self.liquditaView.homeLidquidita.tabsoci.setRowCount(80)

        for row in result:
            id = row[0]
            converted_id = str(id)
            self.liquditaView.homeLidquidita.tabsoci.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(converted_id))
            self.liquditaView.homeLidquidita.tabsoci.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[3] + " " + row[4]))
            rowindex += 1

    def loadDataFornitori(self):
        result = self.tableFornitori.loadData()
        rowindex = 0
        self.liquditaView.homeLidquidita.tabfornitori.setRowCount(80)

        for row in result:
            id = row[0]
            converted_id = str(id)
            self.liquditaView.homeLidquidita.tabfornitori.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(converted_id))
            self.liquditaView.homeLidquidita.tabfornitori.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            rowindex += 1
    def loadDataLiquidita(self):
        result = self.tableLiquidita.loadData()
        print(result)
        rowindex = 0
        self.liquditaView.homeLidquidita.tabliquidita.setRowCount(60)
        for row in result:
            self.liquditaView.homeLidquidita.tabliquidita.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(row[2]))

            importo = row[3]
            converted_importo = str(importo)
            self.liquditaView.homeLidquidita.tabliquidita.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(converted_importo))

            self.liquditaView.homeLidquidita.tabliquidita.setItem(rowindex, 2, QtWidgets.QTableWidgetItem(row[1]))

            socio = row[4]
            converted_socio = str(socio)
            self.liquditaView.homeLidquidita.tabliquidita.setItem(rowindex, 3, QtWidgets.QTableWidgetItem(converted_socio))

            fornitore = row[5]
            converted_fornitore = str(fornitore)
            self.liquditaView.homeLidquidita.tabliquidita.setItem(rowindex, 4, QtWidgets.QTableWidgetItem(converted_fornitore))

            id = row[0]
            converted_id = str(id)
            self.liquditaView.homeLidquidita.tabliquidita.setItem(rowindex, 5, QtWidgets.QTableWidgetItem(converted_id))

            rowindex += 1