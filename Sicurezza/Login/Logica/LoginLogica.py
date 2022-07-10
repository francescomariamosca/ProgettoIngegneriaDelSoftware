from GestioneDatabase.QuerySicurezza.TableSicurezza import TableSicurezza
from Home.View.Home import Home
from Sicurezza.Login.View.LoginView import LoginView


class LoginLogica():
    def __init__(self):
        self.loginView = LoginView()
        self.tableSicurezza = TableSicurezza()
        self.home = Home()
        self.loginView.login.logbutton.clicked.connect(self.CheckLogin)

    def CheckLogin(self):
        username, password = self.loginView.getLoginLineEdit()
        params = {'nome_utente': username, 'pass': password}
        result = self.tableSicurezza.modifyQuery(params)

        if result == 0:
            self.loginView.WarningMessage()
            print("male")
        else:
            self.loginView.window.close()
            self.home.mostra()
            #self.loginView.warn = QMessageBox.warning(self, "Login", "Username e/o password errati!")
            print("bene")