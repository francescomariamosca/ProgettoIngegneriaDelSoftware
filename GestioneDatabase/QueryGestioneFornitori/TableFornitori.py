from GestioneDatabase.TableInterface import TableInterface

class TableFornitori(TableInterface):

    def checkQuery(self, a):
        query = "SELECT id_fornitore from Fornitori where id_fornitore = '%s'" % (''.join(a))
        self.c.execute(query)
        result = self.c.fetchone()
        print(result)
        return result

    def insertQuery(self, params: dict):
        print(params)
        id_fornitore = params['id_fornitore']
        nome = params['nome']
        email = params['email']
        telefono = params['telefono']
        settore = params['settore']
        citta = params['citta']
        via = params['via']
        result = self.checkQuery(id_fornitore)
        print(result)
        if result == None:
            query = "INSERT INTO Fornitori VALUES('%s','%s','%s','%s','%s','%s','%s')" % (
                ''.join(id_fornitore), ''.join(nome), ''.join(email), ''.join(telefono),
                ''.join(settore),''.join(citta), ''.join(via)
            )
            self.c.execute(query)
            self.conn.commit()
            return 0

    def deleteQuery(self, a):
        query = "DELETE FROM Fornitori WHERE id_fornitore = '%s'" % (''.join(a))
        result = self.checkQuery(a)
        if result == None:
            pass
        else:
            self.c.execute(query)
            self.conn.commit()
            return 0


    def modifyQuery(self, params: dict):
        id_fornitore = params['id_fornitore']
        nome = params['nome']
        email = params['email']
        telefono = params['telefono']
        settore = params['settore']
        citta = params['citta']
        via = params['via']
        query = "UPDATE Fornitori SET  nome_azienda = '%s', email = '%s',telefono = '%s', settore= '%s', citta= '%s', via = '%s' WHERE id_fornitore = '%s'" % (
            ''.join(nome), ''.join(email), ''.join(telefono), ''.join(settore), ''.join(citta), ''.join(via), ''.join(id_fornitore),)
        self.c.execute(query)
        self.conn.commit()

    def searchQuery(self, a):
        query = "SELECT * FROM Fornitori where id_fornitore = '%s'" % (''.join(a))
        result = self.checkQuery(a)
        if result == None:
            return 0
            pass
        else:
            self.c.execute(query)
            data = self.c.fetchone()
            id_fornitore = data[0]
            nome = data[1]
            email = data[2]
            telefono = data[3]
            settore = data[4]
            citta = data[5]
            via = data[6]
            return id_fornitore, nome, email, telefono, settore, citta, via


    def loadData(self):
        pass