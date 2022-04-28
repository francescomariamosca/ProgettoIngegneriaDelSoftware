
from GesitoneDatabase.TableInterface import TableInterface


class TableDipendenti(TableInterface):

    def insertQuery(self, params: dict):
        cf = params['cf']
        nome = params ['nome']
        cognome = params ['cognome']
        citta = params['citta']
        tel = params['tel']
        mansione = params ['mansione']
        ore = ['ore']
        stip = ['stip']
        username = ['username']

        result = self.checkQuery(cf)
        print(result)
        if result == None:
            query = "INSERT INTO Dipendenti VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            ''.join(cf), ''.join(nome), ''.join(cognome), ''.join(citta),
            ''.join(tel), ''.join(mansione), ''.join(ore), ''.join(stip),
            ''.join(username))
            print("entrato if")
            self.c.execute(query)
            self.conn.commit()
            return 0
        else:
            print("entrato else")

    def checkQuery(self, a):
        query = "SELECT cf FROM Dipendenti WHERE cf = '%s'" % (''.join(a))
        self.c.execute(query)
        result = self.c.fetchone()
        return result

    def deleteQuery(self, params: dict):
        pass

    def modifyQuery(self, params: dict):
        pass