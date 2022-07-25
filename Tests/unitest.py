from Soci.Logica.LogicaSocio import LogicaSocio
from GestioneDatabase.QuerySicurezza.TableSicurezza import TableSicurezza
from Sicurezza.Login.Logica.LoginLogica import LoginLogica
import sqlite3
import unittest


#classe per effettuare i test sul Login

class TestSoftware(unittest.TestCase):

    def setUp(self):

        conn = sqlite3.connect('CentroSportivo.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS sicurezza(nome_utente text PRIMARY KEY, pass text not null , nome_dipendente text not null)")
        queryinserisciutente = "INSERT INTO sicurezza VALUES ('usertest','pass','nometest')"
        c.execute(queryinserisciutente)
        conn.commit()

        c.execute("CREATE TABLE IF NOT EXISTS Soci(id_socio INTEGER PRIMARY KEY , e_mail text, CF text NOT NULL, nome_cliente text NOT NULL, cognome_cliente text NOT NULL, telefono text, Data_abbonamento text NOT NULL )")
        queryinseriscisoci = "INSERT INTO Soci VALUES ('8', 'test@socio.com','CFTEST', 'testnome', 'testcognome', '5362728', '18-07-2022')"
        c.execute(queryinseriscisoci)
        conn.commit()

    def tearDown(self):
        conn = sqlite3.connect('CentroSportivo.db')
        c = conn.cursor()
        queryeliminautente = "DELETE FROM sicurezza WHERE nome_utente = 'usertest'"
        queryeliminasocio = "DELETE FROM Soci WHERE id_socio = '8'"
        c.execute(queryeliminautente)
        c.execute(queryeliminasocio)
        conn.commit()

    # testo che se sbaglio la password non effettuo il login
    def test_logincorretto(self):
        class LoginViewMockUp:
            def getLoginLineEdit(self):
                return 'usertest', 'pass_sbagliata'
            def WarningMessage(self):
                pass

        class LoginLogicaMockUp(LoginLogica):
            def __init__(self):
                self.loginView = LoginViewMockUp()
                self.tableSicurezza = TableSicurezza()
        loginlogica = LoginLogicaMockUp()
        checkresult = loginlogica.CheckLogin()
        self.assertEqual(checkresult,0)



    #testo la modifica dei dati di un socio
    def test_modificaCredenzialiSocio(self):

        class SocioViewMockUp:
            def __init__(self):
                class DataRinnovoMockUp:
                    def text(self):
                        return '2022-10-03'
                class ModificaSocioMockUp:
                    datarinnovo = DataRinnovoMockUp()
                self.modificaSocio = ModificaSocioMockUp()
            def getModificaLineEdit(self):
                return '8', 'newtest@socio.com','NEWCFTEST', 'newtestnome', 'newtestcognome', '86346445', '2022-10-03'
            def sociModificaCorretto(self):
                pass


        class LogicaSocioMockUp(LogicaSocio):
           def init_view(self):
               self.socioView = SocioViewMockUp()

        logicasocio = LogicaSocioMockUp(None)
        checkmodifica = logicasocio.modificaSocio()

        self.assertEqual(checkmodifica,1)


if __name__ == '__main__':
    unittest.main()
