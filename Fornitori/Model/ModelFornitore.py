import sqlite3

class ModelFornitore():
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM Fornitori")
        result = self.c.fetchall()
        print(result)

    def createTable(self):
        self.c.execute("CREATE TABLE Fornitori(id_fornitore INTEGER PRIMARY KEY, nome_azienda text NOT NULL, email text, telefono text, settore text, citta text, via text)")
        self.conn.commit()

    def popultateDb(self):
        self.c.execute("INSERT INTO Fornitori VALUES(1, 'Azienda SPA', 'francescomaria.bolt@gmail.com', '', 'Rifornimento materiale',' SBT', 'Via Alcide de Gasperi 19')")
        self.conn.commit()