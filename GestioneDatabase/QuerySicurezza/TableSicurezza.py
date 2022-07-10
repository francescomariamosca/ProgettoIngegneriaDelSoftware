from GestioneDatabase.QueryGestioneDipendenti.TableDipendenti import TableDipendenti
from GestioneDatabase.TableInterface import TableInterface

class TableSicurezza(TableInterface):

    def insertQuery(self, params: dict):
        tableDipendente = TableDipendenti()

        username = params['nome_utente']
        password = params['pass']
        cf = params['nome_dipendente']

        print(username, password, cf)

        insertQuery = "INSERT INTO sicurezza VALUES ('%s', '%s', '%s')" % (''.join(username),
                                                                    ''.join(password),
                                                                    ''.join(cf))
        result = self.checkQuery(username)
        print("risultato")
        print(result)
        if result == None:
            existingUser = self.checkExistingUser(cf)
            if existingUser == None:
                self.c.execute(insertQuery)
                self.conn.commit()
                tableDipendente.updateDipendenti(username, cf)
                return 1
            else:
                return 2
        else:
            return 0





    def deleteQuery(self, a):
        deleteQuery = "DELETE FROM sicurezza where nome_utente = '%s'" % (''.join(a))
        result = self.checkQuery(a)
        print(result)
        if result == None:
            return 0
        else:
            self.c.execute(deleteQuery)
            self.conn.commit()
            return 1

    def modifyQuery(self, params: dict):
        #non è possibile modificare un utente
        pass

    def searchQuery(self, params: dict):
        #per tenere continuita con il codice ho deciso di chiamarla searchquery
        #è in realta la query che controlla la presenza di username e password in fase
        #di login
        username = params['nome_utente']
        password = params['pass']
        query =  "SELECT * FROM  sicurezza WHERE nome_utente = '%s' and pass = '%s'" \
                 %(''.join(username), ''.join(password))

        self.c.execute(query)
        result = self.c.fetchone()

        if result == None:
            return 0
        else:
            return 1


    def checkQuery(self, a):
        query = "SELECT nome_utente, nome_dipendente from sicurezza where nome_utente = '%s' " % (''.join(a))
        self.c.execute(query)
        result = self.c.fetchone()
        print(result)
        return result

    def checkExistingcf(self, cf):
        tableDipendente = TableDipendenti()
        resultCheck = tableDipendente.checkQuery(cf)

        if resultCheck == None:
            return 0
            pass
        else:
            return 1

    def checkExistingUser(self,  cf):
        query = "SELECT nome_dipendente from sicurezza where nome_dipendente = '%s' " % (''.join(cf))
        self.c.execute(query)
        result = self.c.fetchone()
        print(result)
        return result


