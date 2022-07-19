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
        result = self.tableSicurezza.searchQuery(params)

        if result == 0:
            self.loginView.WarningMessage()
            return 0
        else:
            self.loginView.window.close()
            self.home.mostra()
            return 1
