import sqlite3

class ModelCampi():
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()
        #self.inserisci()
        self.c.execute("SELECT * FROM Campi")
        result = self.c.fetchall()
        print(result)


    def createTable(self):
        self.c.execute("CREATE TABLE Campi (data_prenotazione text not null, orario_prenotazione text not null, tipo_campo text not null, id_giocatore1 text not null, id_giocatore2 text, id_giocatore3 text, id_giocatore4 text, PRIMARY KEY (data_prenotazione, orario_prenotazione, tipo_campo))")
        self.conn.commit()

    def insertValues(self):
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '19-20', 'Calcetto', 'Mario', '', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '12-13', 'Campo 2 (Terra Rossa)', '1', '', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '13-14', 'Campo 2 (Terra Rossa)', '4', '', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '20-21', 'Calcetto', 'Giuseppe', '', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '17-18', 'Padel 1', '2', '', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '12-13', 'Padel 2', '3', '', '', '')")

        self.conn.commit()

    def inserisci(self):
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '17-18', 'Padel 2', '4', '', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '18-19', 'Padel 2', '4', '5', '', '')")
        self.c.execute("INSERT INTO Campi VALUES('2022-03-10', '20-21', 'Padel 2', '4', '', '', '')")
        self.conn.commit()



