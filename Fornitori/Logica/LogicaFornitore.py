from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from Fornitori.View.FornitoriView import FornitoriView
from GestioneDatabase.QueryGestioneFornitori.TableFornitori import TableFornitori


class LogicaFornitore(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.fornitoreView = FornitoriView()
        self.tableFornitore = TableFornitori()
        self.resultSearch = None

    def passaFornitori(self):
        # inizializza interfaccia fornitori

        self.window = QtWidgets.QMainWindow()
        self.fornitoreView.homeFornitori.setupUi(self.window)
        self.loadTableFornitori()
        self.window.show()

        # funzione per tornare alla home
        self.fornitoreView.homeFornitori.tornahome.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.tornahome.clicked.connect(self.home.mostra)

        # funzione per chiudere l'interfaccia homeFornitore ed aprire quella per l'inserimento
        self.fornitoreView.homeFornitori.aggfornitore.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.aggfornitore.clicked.connect(self.passaInserisciFornitore)

        # funzione per chiudere l'interfaccia homeFornitore ed aprire quella per l'eliminazione
        self.fornitoreView.homeFornitori.eliminafornitore.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.eliminafornitore.clicked.connect(self.passaEliminaFornitore)

        # funzione per passare alla ricerca di un fornitore cosi da poterlo modificare
        self.fornitoreView.homeFornitori.modfornitore.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.modfornitore.clicked.connect(self.passaRicercaFornitore)

    def passaInserisciFornitore(self):
        # inizializzazione interfaccia inserimento di un fornitore
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.inserisciFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.fornitoreView.homeFornitori.window.show()

        # funzione per inserire un fornitore
        self.fornitoreView.inserisciFornitore.aggfonritore.clicked.connect(self.inserisciFornitore)

        # funzione per tornare alla home di fornitori
        self.fornitoreView.inserisciFornitore.tornafornitori.clicked.connect(
            self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.inserisciFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def passaEliminaFornitore(self):
        # inizializzazione interfaccia eliminazione di un fornitore
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.eliminaFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.fornitoreView.homeFornitori.window.show()

        # funzione per eliminare un fornitore
        self.fornitoreView.eliminaFornitore.eliminafornitore.clicked.connect(self.eliminaFornitore)

        # funzione per tornare alla home di fornitori
        self.fornitoreView.eliminaFornitore.tornafornitori.clicked.connect(
            self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.eliminaFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def passaRicercaFornitore(self):
        # inizializzazione interfaccia di ricerca di un fornitore
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.ricercaFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.fornitoreView.homeFornitori.window.show()

        # funzione per ricerca di un fornitore
        self.fornitoreView.ricercaFornitore.confermaricercaid.clicked.connect(self.ricercaInfoFornitore)

        # funzione per tornare alla home Fornitori
        self.fornitoreView.ricercaFornitore.tornafornitori.clicked.connect(
            self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.ricercaFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def passaModificaFornitore(self):
        # inizializzazione dell'interfaccia di modifica e caricamento dei lineEdit
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.modificaFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.caricaFornitore()
        self.fornitoreView.homeFornitori.window.show()

        # funzione per modificare un fornitore
        self.fornitoreView.modificaFornitore.salvamodifiche.clicked.connect(self.modificaFornitore)
        self.fornitoreView.modificaFornitore.salvamodifiche.clicked.connect(self.fornitoreView.homeFornitori.window.close)

        # funzione per tornare indietro all'interfaccia home fornitori
        self.fornitoreView.modificaFornitore.tornafornitori.clicked.connect(self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.modificaFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def inserisciFornitore(self):
        if (self.fornitoreView.getInserisciFornitoreLineEdit() == 0):
            self.fornitoreView.idWarn()
        else:
            id_fornitore, nome, email, telefono, settore, citta, via = self.fornitoreView.getInserisciFornitoreLineEdit()
            params = {'id_fornitore': id_fornitore, 'nome': nome, 'email': email, "telefono": telefono, "settore": settore,
                      "citta": citta, "via": via}
            result = self.tableFornitore.insertQuery(params)
            print(result)
            if result == 0:
                self.fornitoreView.messageCorrettoInserimento()
            else:
                self.fornitoreView.messageWarningInserimento()

    def eliminaFornitore(self):
        id_fornitore = self.fornitoreView.getEliminaFornitoreLineEdit()
        result = self.tableFornitore.deleteQuery(id_fornitore)
        print(result)
        if result != 0:
            self.fornitoreView.messageWarningEliminazione()
        else:
            self.fornitoreView.messageCorrettaEliminazione()

    def ricercaInfoFornitore(self):
        id = self.fornitoreView.getRicercaFornitoreLineEdit()
        self.resultSearch = self.tableFornitore.searchQuery(id)

        if self.resultSearch == 0:
            self.fornitoreView.messageWarningRicerca()
            self.passaFornitori()
        else:
            self.passaModificaFornitore()

    def caricaFornitore(self):
        id_fornitore, nome, email, telefono, settore, citta, via = self.resultSearch
        id_fornitore2 = str(id_fornitore)
        self.fornitoreView.modificaFornitore.idfornitore.setText(id_fornitore2)
        self.fornitoreView.modificaFornitore.idfornitore.setEnabled(False)
        self.fornitoreView.modificaFornitore.nomeazienda.setText(nome)
        self.fornitoreView.modificaFornitore.emailazienda.setText(email)
        self.fornitoreView.modificaFornitore.telefonoazienda.setText(telefono)
        self.fornitoreView.modificaFornitore.settore.setText(settore)
        self.fornitoreView.modificaFornitore.cittazienda.setText(citta)
        self.fornitoreView.modificaFornitore.viazienda.setText(via)



    def modificaFornitore(self):
        id_fornitore, nome, email, telefono, settore, citta, via = self.fornitoreView.getModificaLineEdit()
        params = {'id_fornitore': id_fornitore, 'nome': nome, 'email': email, "telefono": telefono, "settore": settore,
                  "citta": citta, "via": via}
        print(params)
        self.tableFornitore.modifyQuery(params)
        self.fornitoreView.messageCorrettaModifica()
        self.passaFornitori()

    def loadTableFornitori(self):
        queryResult = self.tableFornitore.loadData()
        rowindex = 0
        self.fornitoreView.homeFornitori.tabfornitori.setRowCount(50)

        for row in queryResult:
            id = row[0]
            converted_id = str(id)
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(converted_id))
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.fornitoreView.homeFornitori.tabfornitori.setItem(rowindex, 6, QtWidgets.QTableWidgetItem(row[6]))

            rowindex += 1