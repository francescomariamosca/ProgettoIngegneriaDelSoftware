import sqlite3
from abc import ABC, abstractmethod

class TableInterface(ABC):
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()

    #metodo che viene richiamato per inizializzare una table se non preesistente
    def CreateTables(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS Dipendenti ( cf text PRIMARY KEY, name text not null , cognome text not null, citta text, telefono text, mansione text not null, ore_settimanali integer not null, stip integer not null, username text, FOREIGN KEY(username) REFERENCES Sicurezza (nome_utente))")
        self.c.execute("CREATE TABLE IF NOT EXISTS Fornitori(id_fornitore INTEGER PRIMARY KEY, nome_azienda text NOT NULL, email text, telefono text, settore text, citta text, via text)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Soci(id_socio INTEGER PRIMARY KEY , e_mail text, CF text NOT NULL, nome_cliente text NOT NULL, cognome_cliente text NOT NULL, telefono text, Data_abbonamento text NOT NULL )")

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