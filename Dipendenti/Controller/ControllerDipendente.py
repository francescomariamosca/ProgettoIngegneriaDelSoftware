from PyQt5.QtWidgets import QMainWindow

from Dipendenti.Model.ModelDipendente import ModelDipendente
from PyQt5 import QtWidgets
from Dipendenti.View.DipendentiView import DipendentiView


class ControllerDipendente(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.dipendenteView = DipendentiView()
        self.dipendenteModel = ModelDipendente()
        self.list = []


    def passaDipendenti(self):
        #from Home.View.Home import Home
        #self.home = Home()

        #inizializzazione interfaccia Dipendenti

        self.window = QtWidgets.QMainWindow()
        self.dipendenteView.homeDipendenti.setupUi(self.window)
        self.window.show()

        #funzioni per tornare alla home da gestione dipendenti
        self.dipendenteView.homeDipendenti.tornahome.clicked.connect(self.window.close)
        self.dipendenteView.homeDipendenti.tornahome.clicked.connect(self.home.mostra)

        self.dipendenteView.homeDipendenti.aggiungidip.clicked.connect(self.window.close)

        #funzione per chiudere l'interfaccia homedipendenti all'apertura dell'interfaccia per l'eliminazione
        self.dipendenteView.homeDipendenti.eliminadip.clicked.connect(self.window.close)

        #funzione per chiudere l'interfaccia homedipendenti all'apertura dell'interfaccia per la ricerca dell'utente da modificare
        self.dipendenteView.homeDipendenti.modificainfodip.clicked.connect(self.window.close)

        #funzione per chiamare le funzioni di inserimento,eliminazione e cancellazione
        self.passaBottoniDip()

    #funzione per richiamare i bottoni
    def passaBottoniDip(self):
        self.dipendenteView.homeDipendenti.aggiungidip.clicked.connect(self.passaInserisciDip)
        self.dipendenteView.homeDipendenti.eliminadip.clicked.connect(self.passaEliminaDip)
        self.dipendenteView.homeDipendenti.modificainfodip.clicked.connect(self.passaRicercaDip)

    def passaInserisciDip(self):
        #inizializzazione dell'interfaccia di inserimento
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.inserisciDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.dipendenteView.homeDipendenti.window.show()

        #chiamata della funzione per l'inserimento di un dipendente
        self.dipendenteView.inserisciDip.aggiungidip.clicked.connect(self.inserisciDipendente)

        #funzione per tornare alla Home di gestioneDipendenti
        self.dipendenteView.inserisciDip.tornagestionedip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)
        self.dipendenteView.inserisciDip.tornagestionedip.clicked.connect(self.passaDipendenti)

    def passaEliminaDip(self):
        #funzione per inizializzare l'interfaccia di eliminazione
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.eliminaDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.dipendenteView.homeDipendenti.window.show()
        #funzione per eliminare un dipendente
        self.dipendenteView.eliminaDip.confermaricercacf.clicked.connect(self.eliminaDipendente)

        #funzione per tornare alla Home di gestioneDipendenti
        self.dipendenteView.eliminaDip.tornagestdip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)
        self.dipendenteView.eliminaDip.tornagestdip.clicked.connect(self.passaDipendenti)

    def passaRicercaDip(self):
        #funzione per inizializzare l'interfaccia di ricerca
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.ricercaDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.dipendenteView.homeDipendenti.window.show()

        # funzione per ricercare un dipendente
        self.dipendenteView.ricercaDip.confermaricercacf.clicked.connect(self.ricercaDipendente)
        self.dipendenteView.ricercaDip.confermaricercacf.clicked.connect(self.dipendenteView.homeDipendenti.window.close)

        # funzioni per tornare alla home di gestioneDipendenti
        self.dipendenteView.ricercaDip.tornagestdip.clicked.connect(self.passaDipendenti)
        self.dipendenteView.ricercaDip.tornagestdip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)

    def passaModificaDip(self):
        #funzioni per inizializzare l'interfaccia di modificaDipendente
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.modificaDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.caricaDipendente()
        self.dipendenteView.homeDipendenti.window.show()

        #funzione per modificare il dipendente
        self.dipendenteView.modificaDip.salvamodifichedip.clicked.connect(self.modificaInfoDip)

        #funzione per tornare alla home di gestioneDIpendenti
        self.dipendenteView.modificaDip.tornagestionedip.clicked.connect(self.passaDipendenti)
        self.dipendenteView.modificaDip.tornagestionedip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)






    def inserisciDipendente(self):
        insertQuery = "INSERT INTO Dipendenti VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (''.join(self.dipendenteView.inserisciDip.cf.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.nomedip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.congomedip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.cittadip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.cellularedip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.mansionedip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.oredip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.stipendiodip.text()),
                                                                                                        ''.join(self.dipendenteView.inserisciDip.usernamedip.text()))
        print("lo sto per fare")
        checkQuery = "SELECT cf FROM Dipendenti WHERE cf = '%s'" % (''.join(self.dipendenteView.inserisciDip.cf.text()))
        self.dipendenteModel.c.execute(checkQuery)
        result = self.dipendenteModel.c.fetchone()

        if result == None:
            self.dipendenteModel.c.execute(insertQuery)
            print("l'ho fatto")
            self.dipendenteModel.conn.commit()
            self.dipendenteView.messageInserimentoCorretto()
        else:
            self.dipendenteView.messageWarningInserimento()

    def eliminaDipendente(self):
        queryEliminazione = "DELETE FROM Dipendenti where cf = '%s'" % (''.join(self.dipendenteView.eliminaDip.ricercacf.text()))

        checkQuery = "SELECT cf FROM Dipendenti WHERE cf = '%s'" % (''.join(self.dipendenteView.eliminaDip.ricercacf.text()))

        updateSicurezza = "DELETE FROM sicurezza where nome_dipendente = '%s'" %(''.join(self.dipendenteView.eliminaDip.ricercacf.text()))
        self.dipendenteModel.c.execute(checkQuery)
        result = self.dipendenteModel.c.fetchone()

        if result == None:
            self.dipendenteView.messageWarningEliminazione()
        else:
            self.dipendenteModel.c.execute(queryEliminazione)
            self.dipendenteModel.c.execute(updateSicurezza)
            self.dipendenteModel.conn.commit()
            self.dipendenteView.messageEliminazioneAvvenuta()

    def ricercaDipendente(self):

        searchQuery = "SELECT * FROM Dipendenti where cf = '%s'" % (''.join(self.dipendenteView.ricercaDip.cf.text()))

        checkQuery = "SELECT cf FROM Dipendenti where cf ='%s'" % (''.join(self.dipendenteView.ricercaDip.cf.text()))
        self.dipendenteModel.c.execute(checkQuery)
        result = self.dipendenteModel.c.fetchone()

        if result == None:
            self.dipendenteView.messageWarningRicerca()
            self.passaDipendenti()
        else:
            for row in self.dipendenteModel.c.execute(searchQuery):
                cf = row[0]
                nome = row[1]
                cognome = row[2]
                citta = row[3]
                cellulare = row[4]
                mansione = row[5]
                oredip = row[6]
                stipendio = row[7]
                username = row[8]
                self.list.append(cf)
                self.list.append(nome)
                self.list.append(cognome)
                self.list.append(citta)
                self.list.append(cellulare)
                self.list.append(mansione)
                self.list.append(oredip)
                self.list.append(stipendio)
                self.list.append(username)
                print("fatto")
                print(self.list)
            self.passaModificaDip()

    def caricaDipendente(self):
        cf = self.list[0]
        self.dipendenteView.modificaDip.cf.setText(cf)

        nome = self.list[1]
        self.dipendenteView.modificaDip.nomedip.setText(nome)

        cognome = self.list[2]
        self.dipendenteView.modificaDip.congomedip.setText(cognome)

        citta = self.list[3]
        self.dipendenteView.modificaDip.cittadip.setText(citta)

        cellulare = self.list[4]
        self.dipendenteView.modificaDip.cellularedip.setText(cellulare)

        mansione = self.list[5]
        self.dipendenteView.modificaDip.mansionedip.setText(mansione)

        oredip = self.list[6]
        converted_ore = str(oredip)
        self.dipendenteView.modificaDip.oredip.setText(converted_ore)

        stip = self.list[7]
        converted_stip = str(stip)
        self.dipendenteView.modificaDip.stipendiodip.setText(converted_stip)

        username = self.list[8]
        self.dipendenteView.modificaDip.usernamedip.setText(username)

        self.list.clear()

    def modificaInfoDip(self):
        query = "UPDATE  Dipendenti SET name = '%s', cognome = '%s', citta ='%s', telefono = '%s', mansione = '%s', ore_settimanali = '%s', stip ='%s', username = '%s' WHERE cf = '%s' " % (''.join(self.dipendenteView.modificaDip.nomedip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.congomedip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.cittadip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.cellularedip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.mansionedip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.oredip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.stipendiodip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.usernamedip.text()),
                                                                                                                       ''.join(self.dipendenteView.modificaDip.cf.text()))
        checkquery = "SELECT cf FROM Dipendenti where cf = '%s'" % (''.join(self.dipendenteView.modificaDip.cf.text()))
        self.dipendenteModel.c.execute(checkquery)
        result = self.dipendenteModel.c.fetchone()

        if result == None:
            self.dipendenteView.messageWarningModify()
        else:
            self.dipendenteModel.c.execute(query)
            self.dipendenteModel.conn.commit()
            self.dipendenteView.messageCorrettoModify()


