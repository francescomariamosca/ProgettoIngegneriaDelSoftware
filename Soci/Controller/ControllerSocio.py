import datetime

from Soci.Model.ModelSocio import ModelSocio
from Soci.View.SociView import SociView
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from datetime import date
import smtplib

from Utility.email import email


class ControllerSocio(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.socioView = SociView()
        self.socioModel = ModelSocio()
        self.mail = email()
        self.list = []
        self.listAbbonamento = []
        self.called = True

    def passaSoci(self):
        #from Home.View.Home import Home
        #self.home = Home()

        self.window = QtWidgets.QMainWindow()
        self.socioView.homeSoci.setupUi(self.window)
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
        insertquery= "INSERT INTO Soci VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (''.join(self.socioView.inserisciSocio.idsocio.text()),
                                                                                        ''.join(self.socioView.inserisciSocio.email.text()),
                                                                                        ''.join(self.socioView.inserisciSocio.cfsocio.text()),
                                                                                        ''.join(self.socioView.inserisciSocio.nome.text()),
                                                                                        ''.join(self.socioView.inserisciSocio.cognome.text()),
                                                                                        ''.join(self.socioView.inserisciSocio.telefono.text()),
                                                                                        ''.join(self.socioView.inserisciSocio.datarinnovo.text()))

        checkQuery = "SELECT id_socio FROM Soci where id_socio = '%s'" % (''.join(self.socioView.inserisciSocio.idsocio.text()))
        self.socioModel.c.execute(checkQuery)
        result = self.socioModel.c.fetchone()
        date = self.socioView.inserisciSocio.datarinnovo.text()

        if result == None:
            if len(date.split("-", 4)) == 3 and date.split("-", 4):
                self.socioModel.c.execute(insertquery)
                self.socioModel.conn.commit()
                self.socioView.sociInserimentoCorretto()
            else:
                self.socioView.dateErrore()
        else:
            self.socioView.sociInserimentoWarn()


    def eliminaSocio(self):

        queryEliminazione = "DELETE FROM Soci where id_socio = '%s'" % (''.join(self.socioView.eliminaSocio.ricercaid.text()))

        checkQuery = "SELECT id_socio FROM Soci where id_socio = '%s'" % (''.join(self.socioView.eliminaSocio.ricercaid.text()))
        self.socioModel.c.execute(checkQuery)
        result = self.socioModel.c.fetchone()

        if result == None:
            self.socioView.sociEliminazioneWarn()

        else:
            self.socioModel.c.execute(queryEliminazione)
            self.socioModel.conn.commit()
            self.socioView.sociEliminazioneCorretto()

    def ricercaSocio(self):
        checkQuery = "SELECT id_socio FROM Soci where id_socio = '%s'" % (''.join(self.socioView.ricercaSocio.ricercaid.text()))

        searchQuery = "SELECT * FROM Soci where id_socio = '%s'" % (''.join(self.socioView.ricercaSocio.ricercaid.text()))

        self.socioModel.c.execute(checkQuery)
        result = self.socioModel.c.fetchone()

        if result == None:
            self.socioView.sociRicercaWarn()
            self.passaSoci()
        else:
            for row in self.socioModel.c.execute(searchQuery):
                id_socio = row[0]
                email = row[1]
                cf = row[2]
                nome = row[3]
                cognome = row[4]
                telefono = row[5]
                data = row[6]
                self.list.append(id_socio)
                self.list.append(email)
                self.list.append(cf)
                self.list.append(nome)
                self.list.append(cognome)
                self.list.append(telefono)
                self.list.append(data)
            self.passaModificaSocio()

    def caricaSocio(self):
        id_socio = self.list[0]
        converted_id = str(id_socio)
        self.socioView.modificaSocio.idsocio.setText(converted_id)

        email = self.list[1]
        self.socioView.modificaSocio.email.setText(email)

        cf = self.list[2]
        self.socioView.modificaSocio.cfsocio.setText(cf)

        nome = self.list[3]
        self.socioView.modificaSocio.nome.setText(nome)

        cognome = self.list[4]
        self.socioView.modificaSocio.cognome.setText(cognome)

        tel = self.list[5]
        self.socioView.modificaSocio.telefono.setText(tel)

        rinnovo = self.list[6]
        converted_rinnovo = str(rinnovo)
        self.socioView.modificaSocio.datarinnovo.setText(converted_rinnovo)

        self.list.clear()

    def modificaSocio(self):
        modifyQuery = "UPDATE Soci SET e_mail = '%s', CF = '%s', nome_cliente = '%s', cognome_cliente = '%s', telefono = '%s', Data_abbonamento = '%s' WHERE id_socio = '%s'" % (''.join(self.socioView.modificaSocio.email.text()),
         ''.join(self.socioView.modificaSocio.cfsocio.text()),
         ''.join(self.socioView.modificaSocio.nome.text()),
         ''.join(self.socioView.modificaSocio.cognome.text()),
         ''.join(self.socioView.modificaSocio.telefono.text()),
         ''.join(self.socioView.modificaSocio.datarinnovo.text()),
         ''.join(self.socioView.modificaSocio.idsocio.text()))

        checkQuery = "SELECT id_socio from Soci where id_socio = '%s'" % (''.join(self.socioView.modificaSocio.idsocio.text()))
        self.socioModel.c.execute(checkQuery)
        result = self.socioModel.c.fetchone()

        if result == None:
            self.socioView.sociModificaWarn()
        else:
            self.socioModel.c.execute(modifyQuery)
            self.socioModel.conn.commit()
            self.socioView.sociModificaCorretto()

    def infoScadenzAbbonamento(self):
        today = datetime.datetime.today()
        print(today)

        query = "SELECT Data_abbonamento, id_socio, e_mail, nome_cliente, cognome_cliente from Soci"

        for row in self.socioModel.c.execute(query):
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












