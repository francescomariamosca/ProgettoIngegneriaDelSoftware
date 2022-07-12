
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from Campi.Model.ModelCampi import ModelCampi
from Campi.View.CampiView import CampiView
from PyQt5.QtCore import QDate
from datetime import date

from GestioneDatabase.QueryGestioneSoci.TableSoci import TableSoci
from Utility.email import email


class ControllerCampi(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.viewCampi = CampiView()
        self.modelCampi = ModelCampi()
        self.tableSoci = TableSoci()
        self.mail = email()
        self.datePy = ''
        self.list = []
        self.campo = ''
        self.ora = ''
        self.listEmail = []


    def passaCampi(self):
        #from Home.View.Home import Home
        #self.home = Home()

        #inizializzazione interfaccia campi
        self.window = QtWidgets.QMainWindow()
        self.viewCampi.vistaPrenotazioni.setupUi(self.window)
        self.window.show()
        self.viewCampi.vistaPrenotazioni.setgiorno.dateChanged.connect(self.ottieniData)


        self.viewCampi.vistaPrenotazioni.tornahome.clicked.connect(self.home.mostra)
        self.viewCampi.vistaPrenotazioni.tornahome.clicked.connect(self.window.hide)

        #funzioni per passare
        self.viewCampi.vistaPrenotazioni.visualizzaprenotazioni.clicked.connect(self.window.close)
        self.viewCampi.vistaPrenotazioni.visualizzaprenotazioni.clicked.connect(self.passaVisualizzaCampi)

    def passaVisualizzaCampi(self):
        self.viewCampi.vistaPrenotazioni.window = QtWidgets.QMainWindow()
        self.viewCampi.vistaCampi.setupUi(self.viewCampi.vistaPrenotazioni.window)
        self.uploadTableCampi()
        self.loadTableSoci()
        self.viewCampi.vistaPrenotazioni.window.show()
        self.cambiaLabel()
        self.passaElimina()


    def passaElimina(self):
        #funzione per eliminare una prenotazione
        self.viewCampi.vistaCampi.eliminaprenotazione.clicked.connect(self.eliminaPrenotazione)
        self.viewCampi.vistaCampi.eliminaprenotazione.clicked.connect(self.viewCampi.vistaPrenotazioni.window.close)
        self.viewCampi.vistaCampi.eliminaprenotazione.clicked.connect(self.passaVisualizzaCampi)

        #funzioni per effettuare una prenotazione
        self.viewCampi.vistaCampi.prenotacampo.clicked.connect(self.controllaDisponibilita)

        #funzioni per tornare indietro alla home prenotazioni
        self.viewCampi.vistaCampi.tornahome.clicked.connect(self.passaCampi)
        self.viewCampi.vistaCampi.tornahome.clicked.connect(self.viewCampi.vistaPrenotazioni.window.close)

    def passaInserisciGiocatori(self):
        self.window = QtWidgets.QMainWindow()
        self.viewCampi.inserisciGiocatori.setupUi(self.window)
        self.window.show()
        self.checkCampo()

        self.viewCampi.inserisciGiocatori.confermaprenot.clicked.connect(self.inserisciGiocatori)
        self.viewCampi.inserisciGiocatori.confermaprenot.clicked.connect(self.window.close)
        self.viewCampi.inserisciGiocatori.confermaprenot.clicked.connect(self.passaVisualizzaCampi)

    def ottieniData(self):
        #prendiamo la data, la carichiamo su una variabile e la pasisamo alla funzione per visualizzare i campi, cambia
        #la label e poi la utilizziamo per il database. Il bottone ci fa passare all'altra finestra
        result = self.viewCampi.vistaPrenotazioni.setgiorno.date().toPyDate()
        self.datePy = result.strftime("%Y-%m-%d")
        print(self.datePy)



    def cambiaLabel(self):
        self.viewCampi.vistaCampi.annomesegiorno.setText(self.datePy)

    def eliminaPrenotazione(self):
        self.campo = self.viewCampi.vistaCampi.setcampo.currentText()
        self.ora = self.viewCampi.vistaCampi.setora.currentText()

        deleteQuery = "DELETE  FROM Campi where tipo_campo = '%s' and orario_prenotazione = '%s' " % (''.join(self.campo),
                                                                                                      ''.join(self.ora))


        self.invioMailCancellazione()
        self.modelCampi.c.execute(deleteQuery)
        self.modelCampi.conn.commit()
        self.viewCampi.correttaCancellazione()

    def controllaDisponibilita(self):
        self.campo = self.viewCampi.vistaCampi.setcampo.currentText()
        self.ora = self.viewCampi.vistaCampi.setora.currentText()

        checkQuery = "SELECT id_giocatore1 FROM Campi where tipo_campo = '%s' and orario_prenotazione = '%s' and data_prenotazione = '%s' " % (''.join(self.campo),
                                                                                                                                                ''.join(self.ora),
                                                                                                                                               ''.join(self.datePy))

        self.modelCampi.c.execute(checkQuery)
        result = self.modelCampi.c.fetchone()
        print (result)

        if result == None:
            self.passaInserisciGiocatori()
            print(self.campo, self.ora)

        else:
            self.viewCampi.warnPrenotazione()



    def inserisciGiocatori(self):
        insertQuery = "INSERT INTO Campi VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (''.join(self.datePy),
                                                                                         ''.join(self.ora),
                                                                                         ''.join(self.campo),
                                                                                         ''.join(self.viewCampi.inserisciGiocatori.G1.text()),
                                                                                         ''.join(self.viewCampi.inserisciGiocatori.G2.text()),
                                                                                         ''.join(self.viewCampi.inserisciGiocatori.G3.text()),
                                                                                         ''.join(self.viewCampi.inserisciGiocatori.G4.text()))


        if self.viewCampi.inserisciGiocatori.G1.text() == " ":
            self.viewCampi.warnPrenotazione()
        else:
            self.modelCampi.c.execute(insertQuery)
            self.modelCampi.conn.commit()
            self.viewCampi.correttoInserimento()
            self.invioMailPrenotazione()

    def checkCampo(self):
        if self.campo == "Calcetto":
            print("entrato")
            self.viewCampi.inserisciGiocatori.G2.setEnabled(False)
            self.viewCampi.inserisciGiocatori.G3.setEnabled(False)
            self.viewCampi.inserisciGiocatori.G4.setEnabled(False)

    def invioMailPrenotazione(self):
        id1= self.viewCampi.inserisciGiocatori.G1.text()
        id2= self.viewCampi.inserisciGiocatori.G2.text()
        id3= self.viewCampi.inserisciGiocatori.G3.text()
        id4= self.viewCampi.inserisciGiocatori.G4.text()



        querymail1 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1 and Campi.id_giocatore1 = '%s'" %(''.join(id1))
        querymail2 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore2 and Campi.id_giocatore2 = '%s'" %(''.join(id2))
        querymail3 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore3 and Campi.id_giocatore3 = '%s'" %(''.join(id3))
        querymail4 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore4 and Campi.id_giocatore4 = '%s'" %(''.join(id4))


        self.modelCampi.c.execute(querymail1)
        result1 = self.modelCampi.c.fetchone()

        self.modelCampi.c.execute(querymail2)
        result2 = self.modelCampi.c.fetchone()

        self.modelCampi.c.execute(querymail3)
        result3 = self.modelCampi.c.fetchone()

        self.modelCampi.c.execute(querymail4)
        result4 = self.modelCampi.c.fetchone()

        if result1 == None:
            pass
        else:
            mail = result1[0]
            name = result1 [1]
            cognome = result1 [2]
            print("fatto")
            print(mail)

            if mail == "":
                pass
            else:
                self.mail.emailPrenotazioneAvvenuta(mail, name, cognome, self.datePy, self.ora, self.campo)
            print("ok")

        if result2 == None:
            pass
        else:
            mail = result2[0]
            name = result2[1]
            cognome = result2[2]

            if mail == "":
                pass
            else:
                self.mail.emailPrenotazioneAvvenuta(mail, name, cognome, self.datePy, self.ora, self.campo)
            print("ok")

        if result3 == None:
            pass
        else:
            mail = result3[0]
            name = result3[1]
            cognome = result3[2]

            if mail == "":
                pass
            else:
                self.mail.emailPrenotazioneAvvenuta(mail, name, cognome, self.datePy, self.ora, self.campo)
            print("ok")

        if result4 == None:
            pass
        else:
            mail = result4[0]
            name = result4[1]
            cognome = result4[2]

            if mail == "":
                pass
            else:
                self.mail.emailPrenotazioneAvvenuta(mail, name, cognome, self.datePy, self.ora, self.campo)
            print("ok")

    def invioMailCancellazione(self):
        self.campo = self.viewCampi.vistaCampi.setcampo.currentText()
        self.ora = self.viewCampi.vistaCampi.setora.currentText()
        query1 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore1  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" %(''.join(self.ora),
                                                                                                                                                                                                                                              ''.join(self.campo),
                                                                                                                                                                                                                                              ''.join(self.datePy))
        self.modelCampi.c.execute(query1)
        result1 = self.modelCampi.c.fetchone()
        print(result1)

        query2 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore2  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" %(''.join(self.ora),
                                                                                                                                                                                                                                              ''.join(self.campo),
                                                                                                                                                                                                                                              ''.join(self.datePy))
        self.modelCampi.c.execute(query2)
        result2 = self.modelCampi.c.fetchone()
        print(result2)


        query3 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore3  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" %(''.join(self.ora),
                                                                                                                                                                                                                                              ''.join(self.campo),
                                                                                                                                                                                                                                              ''.join(self.datePy))
        self.modelCampi.c.execute(query3)
        result3 = self.modelCampi.c.fetchone()

        query4 = "SELECT Soci.e_mail, Soci.nome_cliente, Soci.cognome_cliente FROM Soci, Campi WHERE Soci.id_socio = Campi.id_giocatore4  and Campi.orario_prenotazione='%s'and Campi.tipo_campo = '%s' and Campi.data_prenotazione = '%s'" %(''.join(self.ora),
                                                                                                                                                                                                                                              ''.join(self.campo),
                                                                                                                                                                                                                                              ''.join(self.datePy))
        self.modelCampi.c.execute(query4)
        result4 = self.modelCampi.c.fetchone()


        if result1 == None:
            pass
        else:
            print("entrato")
            mail = result1[0]
            nome = result1[1]
            cognome = result1[2]

            if mail == "":
                pass
            else:
             self.mail.emailPrenotazioneCancellata(mail, nome, cognome, self.datePy, self.ora, self.campo)
            print("fatto")

        if result2 == None:
            pass
        else:
            print("entrato")
            mail = result2[0]
            nome = result2[1]
            cognome = result2[2]

            if mail == "":
                pass
            else:
                self.mail.emailPrenotazioneCancellata(mail, nome, cognome, self.datePy, self.ora, self.campo)
            print("fatto")

        if result3 == None:
            pass
        else:
            print("entrato")
            mail = result3[0]
            nome = result3[1]
            cognome = result3[2]

            if mail == "":
                pass
            else:
             self.mail.emailPrenotazioneCancellata(mail, nome, cognome, self.datePy, self.ora, self.campo)
            print("fatto")

        if result4 == None:
            pass
        else:
            print("entrato")
            mail = result4[0]
            nome = result4[1]
            cognome = result4[2]

            if mail == "":
                pass
            else:
                self.mail.emailPrenotazioneCancellata(mail, nome, cognome, self.datePy, self.ora, self.campo)
            print("fatto")


    def uploadTableCampi(self):
            query = "SELECT  id_giocatore1, id_giocatore2, id_giocatore3, id_giocatore4, tipo_campo, orario_prenotazione FROM Campi WHERE data_prenotazione ='%s' " % (''.join(self.datePy))
            for row in self.modelCampi.c.execute(query):
                player1 = row[0]
                player2 = row[1]
                player3 = row[2]
                player4 = row[3]
                campo = row[4]
                orario = row[5]
                self.list.append((player1,player2, player3, player4, campo, orario))

            for id1, id2, id3, id4, field, time in self.list:
                if field == 'Calcetto':
                    if time == '9-10':
                        self.viewCampi.vistaCampi.calcetto.setItem(0, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '10-11':
                        self.viewCampi.vistaCampi.calcetto.setItem(1, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '11-12':
                        self.viewCampi.vistaCampi.calcetto.setItem(2, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '12-13':
                        self.viewCampi.vistaCampi.calcetto.setItem(3, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '13-14':
                        self.viewCampi.vistaCampi.calcetto.setItem(4, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '14-15':
                        self.viewCampi.vistaCampi.calcetto.setItem(5, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '15-16':
                        self.viewCampi.vistaCampi.calcetto.setItem(6, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '16-17':
                        self.viewCampi.vistaCampi.calcetto.setItem(7, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '17-18':
                        self.viewCampi.vistaCampi.calcetto.setItem(8, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '18-19':
                        self.viewCampi.vistaCampi.calcetto.setItem(9, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '19-20':
                        self.viewCampi.vistaCampi.calcetto.setItem(10, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '20-21':
                        self.viewCampi.vistaCampi.calcetto.setItem(11, 0, QtWidgets.QTableWidgetItem(id1))
                    elif time == '21-22':
                        self.viewCampi.vistaCampi.calcetto.setItem(12, 0, QtWidgets.QTableWidgetItem(id1))

                elif field == 'Padel 1 ':

                    if time == '9-10':
                        self.viewCampi.vistaCampi.campipadel.setItem(0, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '10-11':
                        self.viewCampi.vistaCampi.campipadel.setItem(1, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '11-12':
                        self.viewCampi.vistaCampi.campipadel.setItem(2, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '12-13':
                        self.viewCampi.vistaCampi.campipadel.setItem(3, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '13-14':
                        self.viewCampi.vistaCampi.campipadel.setItem(4, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '14-15':
                        self.viewCampi.vistaCampi.campipadel.setItem(5, 0, QtWidgets.QTableWidgetItem( id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '15-16':
                        self.viewCampi.vistaCampi.campipadel.setItem(6, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '16-17':
                        self.viewCampi.vistaCampi.campipadel.setItem(7, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '17-18':
                        self.viewCampi.vistaCampi.campipadel.setItem(8, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '18-19':
                        self.viewCampi.vistaCampi.campipadel.setItem(9, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '19-20':
                        self.viewCampi.vistaCampi.campipadel.setItem(10, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '20-21':
                        self.viewCampi.vistaCampi.campipadel.setItem(11, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '21-22':
                        self.viewCampi.vistaCampi.campipadel.setItem(12, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))

                elif field == 'Padel 2':

                        if time == '9-10':
                            self.viewCampi.vistaCampi.campipadel.setItem(0, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '10-11':
                            self.viewCampi.vistaCampi.campipadel.setItem(1, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '11-12':
                            self.viewCampi.vistaCampi.campipadel.setItem(2, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '12-13':
                            self.viewCampi.vistaCampi.campipadel.setItem(3, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '13-14':
                            self.viewCampi.vistaCampi.campipadel.setItem(4, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '14-15':
                            self.viewCampi.vistaCampi.campipadel.setItem(5, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '15-16':
                            self.viewCampi.vistaCampi.campipadel.setItem(6, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '16-17':
                            self.viewCampi.vistaCampi.campipadel.setItem(7, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '17-18':
                            self.viewCampi.vistaCampi.campipadel.setItem(8, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '18-19':
                            self.viewCampi.vistaCampi.campipadel.setItem(9, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '19-20':
                            self.viewCampi.vistaCampi.campipadel.setItem(10, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '20-21':
                            self.viewCampi.vistaCampi.campipadel.setItem(11, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))
                        elif time == '21-22':
                            self.viewCampi.vistaCampi.campipadel.setItem(12, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " +id4 ))

                elif field == 'Campo CENTRALE (Terra Rossa)':

                            if time == '9-10':
                                self.viewCampi.vistaCampi.campitennis.setItem(0, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '10-11':
                                self.viewCampi.vistaCampi.campitennis.setItem(1, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '11-12':
                                self.viewCampi.vistaCampi.campitennis.setItem(2, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '12-13':
                                self.viewCampi.vistaCampi.campitennis.setItem(3, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '13-14':
                                self.viewCampi.vistaCampi.campitennis.setItem(4, 0, QtWidgets.QTableWidgetItem( id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '14-15':
                                self.viewCampi.vistaCampi.campitennis.setItem(5, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '15-16':
                                self.viewCampi.vistaCampi.campitennis.setItem(6, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '16-17':
                                self.viewCampi.vistaCampi.campitennis.setItem(7, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '17-18':
                                self.viewCampi.vistaCampi.campitennis.setItem(8, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '18-19':
                                self.viewCampi.vistaCampi.campitennis.setItem(9, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '19-20':
                                self.viewCampi.vistaCampi.campitennis.setItem(10, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '20-21':
                                self.viewCampi.vistaCampi.campitennis.setItem(11, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                            elif time == '21-22':
                                self.viewCampi.vistaCampi.campitennis.setItem(12, 0, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))

                elif field == 'Campo 2 (Terra Rossa)':

                    if time == '9-10':
                        self.viewCampi.vistaCampi.campitennis.setItem(0, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '10-11':
                        self.viewCampi.vistaCampi.campitennis.setItem(1, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '11-12':
                        self.viewCampi.vistaCampi.campitennis.setItem(2, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '12-13':
                        self.viewCampi.vistaCampi.campitennis.setItem(3, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '13-14':
                        self.viewCampi.vistaCampi.campitennis.setItem(4, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '14-15':
                        self.viewCampi.vistaCampi.campitennis.setItem(5, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '15-16':
                        self.viewCampi.vistaCampi.campitennis.setItem(6, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '16-17':
                        self.viewCampi.vistaCampi.campitennis.setItem(7, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '17-18':
                        self.viewCampi.vistaCampi.campitennis.setItem(8, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '18-19':
                        self.viewCampi.vistaCampi.campitennis.setItem(9, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '19-20':
                        self.viewCampi.vistaCampi.campitennis.setItem(10, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '20-21':
                        self.viewCampi.vistaCampi.campitennis.setItem(11, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))
                    elif time == '21-22':
                        self.viewCampi.vistaCampi.campitennis.setItem(12, 1, QtWidgets.QTableWidgetItem(id1 + " " + id2 + " " + id3 + " " + id4))

            self.list.clear()

    def loadTableSoci(self):
        result = self.tableSoci.loadData()
        rowindex = 0
        self.viewCampi.vistaCampi.tabellasocicampi.setRowCount(80)

        for row in result:
            id = row[0]
            converted_id = str(id)
            self.viewCampi.vistaCampi.tabellasocicampi.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(converted_id))
            self.viewCampi.vistaCampi.tabellasocicampi.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[1] + " " + row[2]))
            rowindex += 1