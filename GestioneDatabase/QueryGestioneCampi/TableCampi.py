
from GestioneDatabase.TableInterface import TableInterface

class TableCampi(TableInterface):

    def insertQuery(self, params: dict):
        data_prenotazione = params['data_prenotazione']
        orario_prenotazione = params['orario_prenotazione']
        tipo_campo = params['tipo_campo']
        id_giocatore1 = params['id_giocatore1']
        id_giocatore2 = params['id_giocatore2']
        id_giocatore3 = params['id_giocatore3']
        id_giocatore4 = params['id_giocatore4']

        insertQuery = "INSERT INTO Campi VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (''.join(data_prenotazione),
                                                                                         ''.join(orario_prenotazione),
                                                                                         ''.join(tipo_campo),
                                                                                         ''.join(id_giocatore1),
                                                                                         ''.join(id_giocatore2),
                                                                                         ''.join(id_giocatore3),
                                                                                         ''.join(id_giocatore4))
        if id_giocatore1 == " ":
            return 0
        else:
            self.c.execute(insertQuery)
            self.conn.commit()


    def modifyQuery(self, params: dict):
        pass

    def deleteQuery(self, campo, ora, data):
        deleteQuery = "DELETE  FROM Campi where tipo_campo = '%s' and orario_prenotazione = '%s' and data_prenotazione = '%s' " % (''.join(campo),
                                                                                                                                    ''.join(ora),
                                                                                                                                  ''.join(data))

        self.c.execute(deleteQuery)
        self.conn.commit()


    def loadData(self, data):
        query = "SELECT  id_giocatore1, id_giocatore2, id_giocatore3, id_giocatore4, tipo_campo, orario_prenotazione FROM Campi WHERE data_prenotazione ='%s' " % (''.join(data))
        allReservation = self.c.execute(query)
        self.conn.commit()
        return allReservation

    def searchQuery(self, params: dict):
        pass

    def checkQuery(self, campo, ora, data):
        query = "SELECT id_giocatore1 FROM Campi where tipo_campo = '%s' and orario_prenotazione = '%s' and data_prenotazione = '%s' " % (''.join(campo), ''.join(ora), ''.join(data))
        self.c.execute(query)
        result = self.c.fetchone()
        return result

    def sendReservationMail(self, g1, g2, g3, g4):
        querymail1 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1 and Campi.id_giocatore1 = '%s'" % (
            ''.join(g1))
        querymail2 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore2 and Campi.id_giocatore2 = '%s'" % (
            ''.join(g2))
        querymail3 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore3 and Campi.id_giocatore3 = '%s'" % (
            ''.join(g3))
        querymail4 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore4 and Campi.id_giocatore4 = '%s'" % (
            ''.join(g4))

        self.c.execute(querymail1)
        result1 = self.c.fetchone()

        self.c.execute(querymail2)
        result2 = self.c.fetchone()

        self.c.execute(querymail3)
        result3 = self.c.fetchone()

        self.c.execute(querymail4)
        result4 = self.c.fetchone()

        return result1, result2, result3, result4

    def deleteReservationMail(self, ora, campo, data):
        query1 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" % (''.join(ora),
                                                                                                                                                                                                                                               ''.join(campo),
                                                                                                                                                                                                                                               ''.join(data))

        query2 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" % (
            ''.join(ora),
            ''.join(campo),
            ''.join(data))

        query3 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" % (
            ''.join(ora),
            ''.join(campo),
            ''.join(data))

        query4 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" % (
            ''.join(ora),
            ''.join(campo),
            ''.join(data))


        self.c.execute(query1)
        result1 = self.c.fetchone()

        self.c.execute(query2)
        result2 = self.c.fetchone()

        self.c.execute(query3)
        result3 = self.c.fetchone()

        self.c.execute(query4)
        result4 = self.c.fetchone()

        print(result1)
        print(result2)

        return result1, result2, result3, result4