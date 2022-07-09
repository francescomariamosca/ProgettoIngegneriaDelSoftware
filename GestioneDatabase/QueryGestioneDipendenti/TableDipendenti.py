
from GestioneDatabase.TableInterface import TableInterface


class TableDipendenti(TableInterface):

    def insertQuery(self, params: dict):
        cf = params['cf']
        nome = params ['nome']
        cognome = params ['cognome']
        citta = params['citta']
        tel = params['tel']
        mansione = params ['mansione']
        ore = params['ore']
        stip = params['stip']
        username = params['username']
        result = self.checkQuery(cf)
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

    def deleteQuery(self, a):
        query = "DELETE FROM Dipendenti WHERE cf = '%s'" % (''.join(a))
        querySicurezza = "DELETE FROM Sicurezza where nome_dipendente = '%s'" % (''.join(a))
        result = self.checkQuery(a)
        if result == None:
            pass
        else:
            self.c.execute(query)
            self.c.execute(querySicurezza)
            self.conn.commit()
            return 0

    def modifyQuery(self, params: dict):

        cf = params['cf']
        nome = params['nome']
        cognome = params['cognome']
        citta = params['citta']
        tel = params['tel']
        mansione = params ['mansione']
        ore = params['ore']
        stip = params['stip']
        username = params['username']
        print(cf)
        print(nome)

        query = "UPDATE  Dipendenti SET name = '%s', cognome = '%s', citta ='%s', telefono = '%s', mansione = '%s', ore_settimanali = '%s', stip ='%s', username = '%s' WHERE cf = '%s' " % (
            ''.join(nome), ''.join(cognome), ''.join(citta), ''.join(tel), ''.join(mansione), ''.join(ore), ''.join(stip), ''.join(username), ''.join(cf))
        self.c.execute(query)
        self.conn.commit()


    def searchQuery(self, cf):
        query = "SELECT * FROM dipendenti WHERE cf = '%s'" % (''.join(cf))
        result = self.checkQuery(cf)
        if result == None:
            return 0
            pass
        else:
            self.c.execute(query)
            data = self.c.fetchone()
            cf = data[0]
            nome = data[1]
            cognome = data[2]
            citta = data[3]
            telefono = data[4]
            mansione = data[5]
            ore = data[6]
            stip = data[7]
            username = data[8]
            return cf, nome, cognome, citta, telefono, mansione, ore, stip, username