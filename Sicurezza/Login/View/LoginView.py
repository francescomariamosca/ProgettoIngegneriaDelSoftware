from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Sicurezza.Login.View.LoginInterface import LoginInterface

class LoginView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.window = QtWidgets.QMainWindow()
        self.login = LoginInterface ()
        self.login.setupUi(self.window)
        self.login.mostrapasscheck.stateChanged.connect(self.Checkbox)
        self.window.show()

#Questa funzione gestisce il Checkbox e come il testo viene visualizzato nella lineEdit Password
    def Checkbox(self):
        if self.login.mostrapasscheck.isChecked() == True:
            self.login.password.setEchoMode(QLineEdit.Normal)
            print("cliccato")
        else:
            self.login.password.setEchoMode(QLineEdit.Password)
            print("non cliccato")


#Messaggio di Warning riguardante l'errato inserimento di username e password nell'effettuare il login
    def WarningMessage(self):
        self.warn = QMessageBox.warning(self, " ATTENZIONE! ", "Username e/o password errati, riprova!")