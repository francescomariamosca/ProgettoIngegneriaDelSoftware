
from GestioneDatabase.TableInterface import TableInterface

class TableSoci(TableInterface):

    def insertQuery(self, params: dict):
        id_socio = params['id_socio']
        email = params['e_mail']
        cf = params['CF']
        nome = params['nome_cliente']
        cognome = params['cognome_cliente']
        tel = params['telefono']
        data = params['Data_abbonamento']
        result = self.checkQuery(id_socio)
        if result == None:
            query = "INSERT INTO Soci VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
                ''.join(id_socio), ''.join(email), ''.join(cf), ''.join(nome), ''.join(cognome),
                ''.join(tel), ''.join(data))
            self.c.execute(query)
            self.conn.commit()
            return 0


    def checkQuery(self, a):
        query = "SELECT id_socio FROM Soci WHERE id_socio = '%s'" % (''.join(a))
        self.c.execute(query)
        result = self.c.fetchone()
        return result

    def deleteQuery(self, a):
        query = "DELETE FROM Soci WHERE id_socio = '%s'" % (''.join(a))
        result = self.checkQuery(a)
        if result == None:
            pass
        else:
            self.c.execute(query)
            self.conn.commit()
            return 0

    def modifyQuery(self, params: dict):
        id_socio = params['id_socio']
        email = params['e_mail']
        cf = params['CF']
        nome = params['nome_cliente']
        cognome = params['cognome_cliente']
        tel = params['telefono']
        data = params['Data_abbonamento']

        query = "UPDATE Soci SET e_mail = '%s', CF = '%s', nome_cliente = '%s', cognome_cliente = '%s', telefono = '%s', Data_abbonamento = '%s' WHERE id_socio = '%s'" % (
            ''.join(email), ''.join(cf), ''.join(nome), ''.join(cognome), ''.join(tel), ''.join(data), ''.join(id_socio))
        self.c.execute(query)
        self.conn.commit()

    def searchQuery(self, id_socio):
        query = "SELECT * FROM Soci WHERE id_socio = '%s'" % (''.join(id_socio))
        result = self.checkQuery(id_socio)
        if result == None:
            return 0
            pass
        else:
            self.c.execute(query)
            data = self.c.fetchone()
            id_socio = data[0]
            e_mail = data[1]
            CF = data[2]
            nome_cliente = data[3]
            cognome_cliente = data[4]
            telefono = data[5]
            data_abbonamento = data[6]
            return id_socio, e_mail, CF, nome_cliente, cognome_cliente, telefono, data_abbonamento

    def loadData(self):
        query = "SELECT * FROM Soci"
        allSoci = self.c.execute(query)
        self.conn.commit()
        #number = allSoci.fetchall()
        return allSoci #number

    def countSoci(self):
        countQuery = "SELECT COUNT(CF) FROM Soci"
        number = self.c.execute(countQuery)
        number.fetchone()[0]
        return number

    def loadDataCampi(self):
        query = "SELECT id_socio, nome_cliente, cognome_cliente FROM Soci"
        allSoci = self.c.execute(query)
        self.conn.commit()
        return allSoci