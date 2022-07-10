from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from GestioneDatabase.QuerySicurezza.TableSicurezza import TableSicurezza
from Sicurezza.GestioneUtente.View.UtentiView import UtentiView


class ControllerUtente(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.utenteView = UtentiView()
        self.tableUtente = TableSicurezza()
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
        nome_utente = self.utenteView.getEliminaLineEdit()
        result = self.tableUtente.deleteQuery(nome_utente)
        print(result)
        if result == 0:
            self.utenteView.warnElimina()
        if result == 1:
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
        cf = self.utenteView.getRircercaLineEdit()

        result = self.tableUtente.checkExistingcf(cf)

        if result == 0:
            self.utenteView.warnRicerca()
            self.passaGestioneUtenti()
        else:
            self.list.append(cf)
            self.passaInserisciUtente()

    def creaUtente(self):
        passwordsCheck = self.utenteView.checkPasswords()

        if passwordsCheck:
            username, password = self.utenteView.getInsertLineEdit()
            cf = self.list[0]
            params = {'nome_utente' : username, 'pass': password,'nome_dipendente':cf }
            result = self.tableUtente.insertQuery(params)

            if result == 1:
                self.utenteView.correttoInserimento()
            if result == 2:
                self.utenteView.warnMaxOneUser()
            else:
                self.utenteView.warnUtenteEsistente()
        else:
            self.utenteView.warnInserimento()

