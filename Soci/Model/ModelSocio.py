import sqlite3

class ModelSocio():
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()


        #self.alterTable()
        self.c.execute("SELECT * FROM Soci")
        result = self.c.fetchall()
        print(result)

    def alterTable(self):
        self.c.execute("CREATE TABLE Soci(id_socio INTEGER PRIMARY KEY , e_mail text, CF text NOT NULL, nome_cliente text NOT NULL, cognome_cliente text NOT NULL, telefono text, Data_abbonamento text NOT NULL )")
        self.conn.commit()