from GestioneDatabase.QueryGestioneFornitori.TableFornitori import TableFornitori
from GestioneDatabase.QueryGestioneSoci.TableSoci import TableSoci
from GestioneDatabase.TableInterface import TableInterface

class TableLiquidita(TableInterface):

    def insertQuery(self, params: dict, flag):
        id = params['id_transazione']
        tipologia = params['tipologia']
        categoria = params['categoria']
        importo = params['importo']
        socio = params['socio']
        fornitore = params['fornitore']

        query = "INSERT INTO Liquidita VALUES ('%s','%s','%s','%s','%s','%s')" % (
            ''.join(id), ''.join(tipologia), ''.join(categoria),
            ''.join(importo), ''.join(socio), ''.join(fornitore),
        )
        result = self.checkQuery(socio, fornitore, flag)
        if result == 1:
            checkQuery = "SELECT * FROM Liquidita where id_transazione = '%s' " % (''.join(id))
            self.c.execute(checkQuery)
            result = self.c.fetchone()
            print(result)
            if result != None:
                return 0
            else:
                print("dentro")
                self.c.execute(query)
                self.conn.commit()
        else:
            return 0

    def checkQuery(self, a, b, flag):
        tableSoci = TableSoci()
        tableFornitori = TableFornitori()
        if flag is True:
            if a == "":
                return 1
            else:
                resultSoci = tableSoci.checkQuery(a)
                if resultSoci == None:
                    return 0
                else:
                    return 1

        if flag is False:
            if b == "":
                return 1
            else:
                resultFornitori = tableFornitori.checkQuery(b)
                if resultFornitori == None:
                    return 0
                else:
                    return 1


    def deleteQuery(self, a):
        query = "DELETE FROM Liquidita WHERE id_transazione = '%s' " % (''.join(a))
        checkQuery = "SELECT * FROM Liquidita where id_transazione = '%s' " % (''.join(a))
        self.c.execute(checkQuery)
        result = self.c.fetchone()
        print(result)
        if result == None:
            return 0
        else:
            print("dentro")
            self.c.execute(query)
            self.conn.commit()



    def modifyQuery(self, params: dict):
        pass

    def loadData(self):
        query = "SELECT * FROM Liquidita"
        allTransaizoni = self.c.execute(query)
        self.conn.commit()
        print(allTransaizoni)
        return allTransaizoni

    def searchQuery(self, params: dict):
        pass