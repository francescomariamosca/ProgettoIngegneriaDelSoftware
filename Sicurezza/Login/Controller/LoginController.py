
from Home.View.Home import Home
from Sicurezza.Login.View.LoginView import LoginView
from Sicurezza.Login.model.LoginModel import LoginModel


class LoginController():
    def __init__(self):
        self.loginView = LoginView()
        self.modelView = LoginModel()
        self.home = Home()
        self.loginView.login.logbutton.clicked.connect(self.CheckLogin)

    def CheckLogin(self):
        query =  "SELECT * FROM  sicurezza WHERE nome_utente = '%s' and pass = '%s'" % (''.join( self.loginView.login.username.text()),
                                                                                          ''.join(self.loginView.login.password.text()))
        self.modelView.c.execute(query)
        result = self.modelView.c.fetchone()

        if result == None :
            self.loginView.WarningMessage()
            print("male")
        else:
            self.loginView.window.close()
            self.home.mostra()
            #self.loginView.warn = QMessageBox.warning(self, "Login", "Username e/o password errati!")
            print("bene")



