import sqlite3


class ModelDipendente():
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()
        #self.createTableDipendente()
        #self.InsertDip()
        #self.conn.commit()
        self.c.execute("SELECT * FROM Dipendenti")
        fica = self.c.fetchall()
        print(fica)

    #Questa funziona è stata chiamata una sola volta per popolare inizialmente la table Dipendenti
    def InsertDip(self):
        self.c.execute("INSERT INTO Dipendenti VALUES ('PG1', 'Enrico', 'Piergallini', 'sbt', '3339451947', 'troia', '40', '1200', 'Enrico')")

    #Questa funziona è stata chiamata una sola volta per creare la table
    def createTableDipendente(self):
        self.c.execute("CREATE TABLE Dipendenti ( cf text PRIMARY KEY, name text not null , cognome text not null, citta text, telefono text, mansione text not null, ore_settimanali integer not null, stip integer not null, username text, FOREIGN KEY(username) REFERENCES sicurezza (nome_utente))")
