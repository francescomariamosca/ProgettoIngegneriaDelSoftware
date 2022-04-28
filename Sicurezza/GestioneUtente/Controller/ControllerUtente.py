from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from Sicurezza.GestioneUtente.View.UtentiView import UtentiView
from Sicurezza.Login.model.LoginModel import LoginModel


class ControllerUtente(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.utenteView = UtentiView()
        self.utenteModel = LoginModel()
        self.list = []

    def passaGestioneUtenti(self):
        #from Home.View.Home import Home
        #self.home = Home()

        #inizializzazione interfaccia GestioneUtenti
        self.window = QtWidgets.QMainWindow()
        self.utenteView.homeUtente.setupUi(self.window)
        self.window.show()

        #funzioni per tornare alla home
        self.utenteView.homeUtente.tornahome.clicked.connect(self.window.close)
        self.utenteView.homeUtente.tornahome.clicked.connect(self.home.mostra)

        #funzione per chiudere la window quando si ricerca un utente
        self.utenteView.homeUtente.aggutente.clicked.connect(self.window.close)

        #funzione per chiudere la window quando si elimina un utente
        self.utenteView.homeUtente.eliminautente.clicked.connect(self.window.close)

        self.passaBottoniUtente()

    def passaBottoniUtente(self):
        self.utenteView.homeUtente.aggutente.clicked.connect(self.passaCheckUtente)
        self.utenteView.homeUtente.eliminautente.clicked.connect(self.passaElimina)

    def passaElimina(self):
        #inizializzazione interfaccia eliminazione utente
        self.utenteView.homeUtente.window = QtWidgets.QMainWindow()
        self.utenteView.eliminaUtente.setupUi(self.utenteView.homeUtente.window)
        self.utenteView.homeUtente.window.show()

        #funzioni per eliminare l'utente
        self.utenteView.eliminaUtente.confermaricercauser.clicked.connect(self.eliminaUtente)

        #funzioni per tornare dall'interfaccia di eliminazione a alla home Utenti
        self.utenteView.eliminaUtente.tornahome.clicked.connect(self.utenteView.homeUtente.window.close)
        self.utenteView.eliminaUtente.tornahome.clicked.connect(self.passaGestioneUtenti)

    def eliminaUtente(self):
        deleteQuery = "DELETE FROM sicurezza where nome_utente = '%s'" % (''.join(self.utenteView.eliminaUtente.ricercauser.text()))

        checkquery = "SELECT nome_utente FROM sicurezza WHERE nome_utente = '%s'" % (''.join(self.utenteView.eliminaUtente.ricercauser.text()))
        self.utenteModel.c.execute(checkquery)
        result = self.utenteModel.c.fetchone()
        if result == None:
            self.utenteView.warnElimina()
        else:
            self.utenteModel.c.execute(deleteQuery)
            self.utenteModel.conn.commit()
            self.utenteView.correttoEliminazione()


    def passaCheckUtente(self):
        #inizializzazione interfaccia esistenza utente
        self.utenteView.homeUtente.window = QtWidgets.QMainWindow()
        self.utenteView.ricercaCf.setupUi(self.utenteView.homeUtente.window)
        self.utenteView.homeUtente.window.show()

        #funzioni per la ricerca di un utente tramite il codice fiscale del dipendente ad adesso associato
        self.utenteView.ricercaCf.confermaricercacfdip.clicked.connect(self.esistenzaDipendente)
        self.utenteView.ricercaCf.confermaricercacfdip.clicked.connect(self.utenteView.homeUtente.window.close)

        #funzione per passare dall'interfaccia di ricerca alla home Utenti
        self.utenteView.ricercaCf.tornahome.clicked.connect(self.utenteView.homeUtente.window.close)
        self.utenteView.ricercaCf.tornahome.clicked.connect(self.passaGestioneUtenti)

    def passaInserisciUtente(self):
        self.utenteView.ricercaCf.window = QtWidgets.QMainWindow()
        self.utenteView.inserisciUtente.setupUi(self.utenteView.ricercaCf.window)
        self.utenteView.ricercaCf.window.show()

        #funzioni per l'inserimento dell'utente
        self.utenteView.inserisciUtente.creautente.clicked.connect(self.creaUtente)

        #funzioni per tornare alla home GestioneUtenti
        self.utenteView.inserisciUtente.tornahome.clicked.connect(self.utenteView.ricercaCf.window.close)
        self.utenteView.inserisciUtente.tornahome.clicked.connect(self.passaGestioneUtenti)


    def esistenzaDipendente(self):
        existQuery = "SELECT cf FROM Dipendenti WHERE cf = '%s'" % (''.join(self.utenteView.ricercaCf.ricercacfdip.text()))

        self.utenteModel.c.execute(existQuery)
        result = self.utenteModel.c.fetchone()
        if result == None:
            self.utenteView.warnRicerca()
            self.passaGestioneUtenti()
        else:
            cf = self.utenteView.ricercaCf.ricercacfdip.text()
            self.list.append(cf)
            self.passaInserisciUtente()

    def creaUtente(self):
        query = "SELECT nome_utente from sicurezza where nome_utente = '%s' " % (''.join(self.utenteView.inserisciUtente.username.text()))
        self.utenteModel.c.execute(query)
        print("fatto")
        result = self.utenteModel.c.fetchone()
        print(result)

        if result == None:

            if self.utenteView.inserisciUtente.password.text() == self.utenteView.inserisciUtente.confermapassword.text():
                insertQuery = "INSERT INTO sicurezza VALUES ('%s', '%s', '%s')" % (''.join(self.utenteView.inserisciUtente.username.text()),
                                                                               ''.join(self.utenteView.inserisciUtente.password.text()),
                                                                               ''.join(self.list[0]))
                self.utenteModel.c.execute(insertQuery)
                self.utenteModel.conn.commit()

                updateDip = "UPDATE Dipendenti SET username = '%s' WHERE cf ='%s' " % (''.join(self.utenteView.inserisciUtente.username.text()),
                                                                                   ''.join(self.list[0]))
                self.list.clear()
                self.utenteModel.c.execute(updateDip)
                self.utenteModel.conn.commit()
                self.utenteView.correttoInserimento()

            else:
                self.utenteView.warnInserimento()
        else:
            self.utenteView.warnUtenteEsistente()
