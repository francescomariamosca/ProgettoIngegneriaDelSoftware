import sqlite3
from abc import ABC, abstractmethod

class TableInterface(ABC):
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()
        self.CreateTables()

    #metodo che viene richiamato per inizializzare una table se non preesistente
    def CreateTables(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS Dipendenti ( cf text PRIMARY KEY, name text not null , cognome text not null, citta text, telefono text, mansione text not null, ore_settimanali integer not null, stip integer not null, username text, FOREIGN KEY(username) REFERENCES sicurezza (nome_utente))")
        self.c.execute("CREATE TABLE IF NOT EXISTS Fornitori (id_fornitore INTEGER PRIMARY KEY, nome_azienda text NOT NULL, email text, telefono text, settore text, citta text, via text)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Soci(id_socio INTEGER PRIMARY KEY , e_mail text, CF text NOT NULL, nome_cliente text NOT NULL, cognome_cliente text NOT NULL, telefono text, Data_abbonamento text NOT NULL )")
        self.c.execute("CREATE TABLE IF NOT EXISTS sicurezza(nome_utente text PRIMARY KEY, pass text not null , nome_dipendente text not null)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Campi (data_prenotazione text not null, orario_prenotazione text not null, tipo_campo text not null, id_giocatore1 text not null, id_giocatore2 text, id_giocatore3 text, id_giocatore4 text, PRIMARY KEY (data_prenotazione, orario_prenotazione, tipo_campo))")
        self.c.execute("CREATE TABLE IF NOT EXISTS Liquidita (id_transazione INTEGER PRIMARY KEY , tipologia text NOT NULL , categoria text NOT NULL, importo int not null, socio integer, fornitore integer )")


    @abstractmethod
    def checkQuery(self, a):
        pass

    @abstractmethod
    def insertQuery(self, params: dict):
        pass

    @abstractmethod
    def deleteQuery(self, params: dict):
        pass

    @abstractmethod
    def modifyQuery(self, params: dict):
        pass

    @abstractmethod
    def searchQuery(self, params: dict):
        pass

    @abstractmethod
    def loadData(self):
        pass