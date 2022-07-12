import datetime


from GestioneDatabase.QueryGestioneSoci.TableSoci import TableSoci
from Soci.View.SociView import SociView
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from datetime import date
import smtplib

from Utility.email import email


class LogicaSocio(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.socioView = SociView()
        self.tableSocio = TableSoci()
        self.resultSearch = None
        self.mail = email()
        self.listAbbonamento = []
        self.called = True

    def passaSoci(self):
        #from Home.View.Home import Home
        #self.home = Home()

        self.window = QtWidgets.QMainWindow()
        self.socioView.homeSoci.setupUi(self.window)
        self.loadsocioTable()
        self.window.show()
        if self.called == False:
            self.infoScadenzAbbonamento()


        self.socioView.homeSoci.tornahome.clicked.connect(self.window.close)
        self.socioView.homeSoci.tornahome.clicked.connect(self.home.mostra)

        self.socioView.homeSoci.aggsocio.clicked.connect(self.window.close)

        self.socioView.homeSoci.eliminasocio.clicked.connect(self.window.close)

        self.socioView.homeSoci.modificainfosocio.clicked.connect(self.window.close)

        self.passaBottoniSoci()

    def passaBottoniSoci(self):
        self.socioView.homeSoci.aggsocio.clicked.connect(self.passaInserisciSocio)
        self.socioView.homeSoci.eliminasocio.clicked.connect(self.passaEliminaSocio)
        self.socioView.homeSoci.modificainfosocio.clicked.connect(self.passaRicercaSocio)

    def passaInserisciSocio(self):
        #inizializzazione interfaccia di inserimento
        self.socioView.homeSoci.window = QtWidgets.QMainWindow()
        self.socioView.inserisciSocio.setupUi(self.socioView.homeSoci.window)
        self.socioView.homeSoci.window.show()

        #richiama la funzione per inserire un socio
        self.socioView.inserisciSocio.aggalbo.clicked.connect(self.inserisciSocio)

        #torna indietro alla schermata home dei soci
        self.socioView.inserisciSocio.tornagestionesoci.clicked.connect(self.passaSoci)
        self.socioView.inserisciSocio.tornagestionesoci.clicked.connect(self.socioView.homeSoci.window.close)

    def passaEliminaSocio(self):
        #inizializzazione interfaccia di eliminazione
        self.socioView.homeSoci.window = QtWidgets.QMainWindow()
        self.socioView.eliminaSocio.setupUi(self.socioView.homeSoci.window)
        self.socioView.homeSoci.window.show()

        #richiama la funzione per eliminare un socio
        self.socioView.eliminaSocio.confermaricercaidsocio.clicked.connect(self.eliminaSocio)

        #torna indietro alla schermata home dei soci
        self.socioView.eliminaSocio.tornagestsocio.clicked.connect(self.passaSoci)
        self.socioView.eliminaSocio.tornagestsocio.clicked.connect(self.socioView.homeSoci.window.close)

    def passaRicercaSocio(self):
        #funzione per inizializzare l'interfaccia di ricerca
        self.socioView.homeSoci.window = QtWidgets.QMainWindow()
        self.socioView.ricercaSocio.setupUi(self.socioView.homeSoci.window)
        self.socioView.homeSoci.window.show()

        #funzione per ricercare un socio
        self.socioView.ricercaSocio.confermaid.clicked.connect(self.ricercaSocio)
        self.socioView.ricercaSocio.confermaid.clicked.connect(self.socioView.homeSoci.window.hide)

        #funzione per tornare alla home di gestioneSoci
        self.socioView.ricercaSocio.tornagestdip.clicked.connect(self.passaSoci)
        self.socioView.ricercaSocio.tornagestdip.clicked.connect(self.socioView.homeSoci.window.hide)

    def passaModificaSocio(self):
        #funzione per inizializzare l'interfaccia di modificaSocio
        self.socioView.homeSoci.window = QtWidgets.QMainWindow()
        self.socioView.modificaSocio.setupUi(self.socioView.homeSoci.window)
        #funzione per caricare lineedit
        self.caricaSocio()
        self.socioView.homeSoci.window.show()

        #funzione per modificare un dipendente
        self.socioView.modificaSocio.salvamodifichesocio.clicked.connect(self.modificaSocio)

        #funzione per tornare alla home di gestioneSoci
        self.socioView.modificaSocio.tornagestionesoci.clicked.connect(self.passaSoci)
        self.socioView.modificaSocio.tornagestionesoci.clicked.connect(self.socioView.homeSoci.window.hide)

    def inserisciSocio(self):
        id_socio, e_mail, CF, nome_cliente, cognome_cliente, telefono, Data_abbonamento = self.socioView.getInserisciLineEdit()
        params = {'id_socio': id_socio, 'e_mail': e_mail, 'CF': CF, 'nome_cliente': nome_cliente, 'cognome_cliente': cognome_cliente, 'telefono' : telefono, 'Data_abbonamento': Data_abbonamento}
        date = self.socioView.inserisciSocio.datarinnovo.text()

        if len(date.split("-", 4)) == 3 and date.split("-", 4):
                result = self.tableSocio.insertQuery(params)
                if result == 0:
                    self.socioView.sociInserimentoCorretto()
                else:
                    self.socioView.dateErrore()
        else:
                self.socioView.dateErrore()


    def eliminaSocio(self):

        id_socio = self.socioView.getEliminaLineEdit()
        print(id_socio)
        result = self.tableSocio.deleteQuery(id_socio)
        if result != 0:
            self.socioView.sociEliminazioneWarn()
        else:
            self.socioView.sociEliminazioneCorretto()

    def ricercaSocio(self):
        id_socio = self.socioView.getRicercaLineEdit()
        self.resultSearch = self.tableSocio.searchQuery(id_socio)
        print(self.resultSearch)

        if self.resultSearch == 0:
            self.socioView.sociRicercaWarn()
            self.passaSoci()
        else:
            self.passaModificaSocio()

    def caricaSocio(self):
        print(self.resultSearch)
        id_socio = self.resultSearch[0]
        e_mail = self.resultSearch[1]
        cf = self.resultSearch[2]
        nome_cliente = self.resultSearch[3]
        cognome_cliente = self.resultSearch[4]
        telefono = self.resultSearch[5]
        data_abbonamento = self.resultSearch[6]

        id_socioStr = str(id_socio)

        self.socioView.modificaSocio.idsocio.setText(id_socioStr)
        self.socioView.modificaSocio.idsocio.setEnabled(False)
        self.socioView.modificaSocio.email.setText(e_mail)
        self.socioView.modificaSocio.cfsocio.setText(cf)
        self.socioView.modificaSocio.nome.setText(nome_cliente)
        self.socioView.modificaSocio.cognome.setText(cognome_cliente)
        self.socioView.modificaSocio.telefono.setText(telefono)

        self.socioView.modificaSocio.datarinnovo.setText(data_abbonamento)
        self.socioView.modificaSocio.datarinnovo.setMaxLength(10)


    def modificaSocio(self):
        id_socio, e_mail, CF, nome_cliente, cognome_cliente, telefono, Data_abbonamento = self.socioView.getModificaLineEdit()
        params = {'id_socio': id_socio, 'e_mail': e_mail, 'CF': CF, 'nome_cliente': nome_cliente,
                  'cognome_cliente': cognome_cliente, 'telefono': telefono, 'Data_abbonamento': Data_abbonamento}
        date = self.socioView.modificaSocio.datarinnovo.text()
        print(date)
        if len(date.split("-", 4)) == 3 and date.split("-", 4):
            print("entrato")
            self.tableSocio.modifyQuery(params)
            self.socioView.sociModificaCorretto()
        else:
            self.socioView.sociModificaWarn()



    def infoScadenzAbbonamento(self):
        today = datetime.datetime.today()
        print(today)

        query = "SELECT Data_abbonamento, id_socio, e_mail, nome_cliente, cognome_cliente from Soci"

        for row in self.tableSocio.c.execute(query):
            dataAbbonamento = row[0]
            id_socio = row[1]
            email = row[2]
            nome = row[3]
            cognome = row[4]
            self.listAbbonamento.append((dataAbbonamento, id_socio, email, nome, cognome))
        print(self.listAbbonamento)



        for data, id, email, nome, cognome in self.listAbbonamento:

            result = datetime.datetime.strptime(data, "%Y-%m-%d")
            y = today - result
            delta = datetime.timedelta(335)
            if y > delta:
                self.socioView.scadenzaAbbonamento(id, email)
                self.email.emailScadenzaAbbonamento(email, nome, cognome)

        self.listAbbonamento.clear()
        self.called = True

    def loadsocioTable(self):

        allSoci = self.tableSocio.loadDataCampi()
        rowindex = 0
        self.socioView.homeSoci.tabellasoci.setRowCount(50)

        for row in allSoci:
            id_cliente = row[0]
            converted_id = str(id_cliente)
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(converted_id))
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 5, QtWidgets.QTableWidgetItem(row[5]))
            date = row[6]
            converted_date = str(date)
            self.socioView.homeSoci.tabellasoci.setItem(rowindex, 6, QtWidgets.QTableWidgetItem(converted_date))
            rowindex += 1