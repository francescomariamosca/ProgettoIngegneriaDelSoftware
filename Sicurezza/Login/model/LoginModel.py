import sqlite3

class LoginModel():
    def __init__(self):
        self.conn = sqlite3.connect('CentroSportivo.db')
        self.c = self.conn.cursor()
        #self.c.execute("INSERT INTO sicurezza values ('Enrico', '12d', 'PG1') ")
        #self.conn.commit()

        self.c.execute("SELECT * FROM sicurezza")
        print_sicurezza = self.c.fetchall()
        print(print_sicurezza)

    def commit(self):
        self.conn.commit()
        self.c.close()

    def alterTable(self):
        self.c.execute("ALTER TABLE sicurezza ADD COLUMN nome_dipendente text not null ")

    def removeElement(self):
        self.c.execute("DELETE FROM sicurezza where nome_utente = 'Enrico'")