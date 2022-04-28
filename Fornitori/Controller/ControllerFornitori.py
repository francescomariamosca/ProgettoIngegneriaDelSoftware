from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from Fornitori.Model.ModelFornitore import ModelFornitore
from Fornitori.View.FornitoriView import FornitoriView

class ControllerFornitori(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.fornitoreView = FornitoriView()
        self.fornitoreModel = ModelFornitore()
        self.list = []

    def passaFornitori(self):
        #inizializza interfaccia fornitori

        self.window = QtWidgets.QMainWindow()
        self.fornitoreView.homeFornitori.setupUi(self.window)
        self.window.show()

        #funzione per tornare alla home
        self.fornitoreView.homeFornitori.tornahome.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.tornahome.clicked.connect(self.home.mostra)

        #funzione per chiudere l'interfaccia homeFornitore ed aprire quella per l'inserimento
        self.fornitoreView.homeFornitori.aggfornitore.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.aggfornitore.clicked.connect(self.passaInserisciFornitore)

        # funzione per chiudere l'interfaccia homeFornitore ed aprire quella per l'eliminazione
        self.fornitoreView.homeFornitori.eliminafornitore.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.eliminafornitore.clicked.connect(self.passaEliminaFornitore)

        #funzione per passare alla ricerca di un fornitore cosi da poterlo modificare
        self.fornitoreView.homeFornitori.modfornitore.clicked.connect(self.window.close)
        self.fornitoreView.homeFornitori.modfornitore.clicked.connect(self.passaRicercaFornitore)


    def passaInserisciFornitore(self):
        #inizializzazione interfaccia inserimento di un fornitore
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.inserisciFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.fornitoreView.homeFornitori.window.show()

        #funzione per inserire un fornitore
        self.fornitoreView.inserisciFornitore.aggfonritore.clicked.connect(self.inserisciFornitore)

        #funzione per tornare alla home di fornitori
        self.fornitoreView.inserisciFornitore.tornafornitori.clicked.connect(self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.inserisciFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def passaEliminaFornitore(self):
        #inizializzazione interfaccia eliminazione di un fornitore
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.eliminaFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.fornitoreView.homeFornitori.window.show()

        #funzione per eliminare un fornitore
        self.fornitoreView.eliminaFornitore.eliminafornitore.clicked.connect(self.eliminaFornitore)

        #funzione per tornare alla home di fornitori
        self.fornitoreView.eliminaFornitore.tornafornitori.clicked.connect(self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.eliminaFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def passaRicercaFornitore(self):
        #inizializzazione interfaccia di ricerca di un fornitore
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.ricercaFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.fornitoreView.homeFornitori.window.show()

        #funzione per ricerca di un fornitore
        self.fornitoreView.ricercaFornitore.confermaricercaid.clicked.connect(self.ricercaInfoFornitore)

        #funzione per tornare alla home Fornitori
        self.fornitoreView.ricercaFornitore.tornafornitori.clicked.connect(self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.ricercaFornitore.tornafornitori.clicked.connect(self.passaFornitori)

    def passaModificaFornitore(self):
        #inizializzazione dell'interfaccia di modifica e caricamento dei lineEdit
        self.fornitoreView.homeFornitori.window = QtWidgets.QMainWindow()
        self.fornitoreView.modificaFornitore.setupUi(self.fornitoreView.homeFornitori.window)
        self.caricaFornitore()
        self.fornitoreView.homeFornitori.window.show()

        #funzione per modificare un fornitore
        self.fornitoreView.modificaFornitore.salvamodifiche.clicked.connect(self.modificaFornitore)

        #funzione per tornare indietro all'interfaccia home fornitori
        self.fornitoreView.modificaFornitore.tornafornitori.clicked.connect(self.fornitoreView.homeFornitori.window.close)
        self.fornitoreView.modificaFornitore.tornafornitori.clicked.connect(self.passaFornitori)


    def inserisciFornitore(self):
        insertQuery = "INSERT INTO Fornitori VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (''.join(self.fornitoreView.inserisciFornitore.idfornitore.text()),
                                                                                            ''.join(self.fornitoreView.inserisciFornitore.nomeazienda.text()),
                                                                                            ''.join(self.fornitoreView.inserisciFornitore.emailazienda.text()),
                                                                                            ''.join(self.fornitoreView.inserisciFornitore.telefonoazienda.text()),
                                                                                            ''.join(self.fornitoreView.inserisciFornitore.settore.text()),
                                                                                            ''.join(self.fornitoreView.inserisciFornitore.cittazienda.text()),
                                                                                            ''.join(self.fornitoreView.inserisciFornitore.viazienda.text()))

        checkquery = "SELECT id_fornitore FROM Fornitori where id_fornitore = '%s'" % (''.join(self.fornitoreView.inserisciFornitore.idfornitore.text()))
        self.fornitoreModel.c.execute(checkquery)
        result = self.fornitoreModel.c.fetchone()

        if result == None:
            self.fornitoreModel.c.execute(insertQuery)
            self.fornitoreModel.conn.commit()
            self.fornitoreView.messageCorrettoInserimento()
        else:
            self.fornitoreView.messageWarningInserimento()

    def eliminaFornitore(self):
        queryEliminazione = "DELETE FROM Fornitori WHERE id_fornitore = '%s'" % (''.join(self.fornitoreView.eliminaFornitore.ricercaidfornitore.text()))

        checkQuery = "SELECT id_fornitore FROM Fornitori WHERE id_fornitore = '%s'" % (''.join(self.fornitoreView.eliminaFornitore.ricercaidfornitore.text()))

        self.fornitoreModel.c.execute(checkQuery)
        result = self.fornitoreModel.c.fetchone()

        if result == None:
            self.fornitoreView.messageWarningEliminazione()
        else:
            self.fornitoreModel.c.execute(queryEliminazione)
            self.fornitoreModel.conn.commit()
            self.fornitoreView.messageCorrettaEliminazione()

    def ricercaInfoFornitore(self):
        searchQuery = "SELECT * FROM Fornitori WHERE id_fornitore = '%s'" % (''.join(self.fornitoreView.ricercaFornitore.ricercaidfornitore.text()))

        checkQuery = " SELECT id_fornitore FROM Fornitori WHERE id_fornitore = '%s'" % (''.join(self.fornitoreView.ricercaFornitore.ricercaidfornitore.text()))
        self.fornitoreModel.c.execute(checkQuery)
        result = self.fornitoreModel.c.fetchone()

        if result == None:
            self.fornitoreView.messageWarningEliminazione()
            self.passaFornitori()
        else:
            for row in self.fornitoreModel.c.execute(searchQuery):
                id = row[0]
                nome = row[1]
                email = row[2]
                telefono = row [3]
                settore = row[4]
                citta = row[5]
                via = row[6]
                self.list.append(id)
                self.list.append(nome)
                self.list.append(email)
                self.list.append(telefono)
                self.list.append(settore)
                self.list.append(citta)
                self.list.append(via)
                print(self.list)

            self.passaModificaFornitore()

    def caricaFornitore(self):
        id = self.list[0]
        conv_id = str(id)
        self.fornitoreView.modificaFornitore.idfornitore.setText(conv_id)

        nome = self.list[1]
        self.fornitoreView.modificaFornitore.nomeazienda.setText(nome)

        email = self.list[2]
        self.fornitoreView.modificaFornitore.emailazienda.setText(email)

        telefono = self.list[3]
        self.fornitoreView.modificaFornitore.telefonoazienda.setText(telefono)

        settore = self.list[4]
        self.fornitoreView.modificaFornitore.settore.setText(settore)

        citta = self.list[5]
        self.fornitoreView.modificaFornitore.cittazienda.setText(citta)

        via = self.list[6]
        self.fornitoreView.modificaFornitore.viazienda.setText(via)

        self.list.clear()

    def modificaFornitore(self):
        modifyQuery = "UPDATE Fornitori SET nome_azienda = '%s', email = '%s', telefono = '%s', settore = '%s', citta = '%s', via = '%s' WHERE id_fornitore = '%s'"% (''.join(self.fornitoreView.modificaFornitore.nomeazienda.text()),
                                                                                                                                                                      ''.join(self.fornitoreView.modificaFornitore.emailazienda.text()),
                                                                                                                                                                      ''.join(self.fornitoreView.modificaFornitore.telefonoazienda.text()),
                                                                                                                                                                      ''.join(self.fornitoreView.modificaFornitore.settore.text()),
                                                                                                                                                                      ''.join(self.fornitoreView.modificaFornitore.cittazienda.text()),
                                                                                                                                                                      ''.join(self.fornitoreView.modificaFornitore.viazienda.text()),
                                                                                                                                                                      ''.join(self.fornitoreView.modificaFornitore.idfornitore.text()))

        checkQuery = "SELECT id_fornitore FROM Fornitori WHERE id_fornitore = '%s'" % (''.join(self.fornitoreView.modificaFornitore.idfornitore.text()))
        self.fornitoreModel.c.execute(checkQuery)
        result = self.fornitoreModel.c.fetchone()

        if result == None:
            self.fornitoreView.messageWarningModifica()

        else:
            self.fornitoreModel.c.execute(modifyQuery)
            self.fornitoreModel.conn.commit()
            self.fornitoreView.messageCorrettaModifica()
