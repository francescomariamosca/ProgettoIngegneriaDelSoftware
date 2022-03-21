import datetime

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

from Campi.Model.ModelCampi import ModelCampi
from Campi.View.CampiView import CampiView
from PyQt5.QtCore import QDate
from datetime import date


class ControllerCampi(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.viewCampi = CampiView()
        self.modelCampi = ModelCampi()
        self.datePy = ''
        self.list = []

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
        self.passaBottoniCampi()

    def passaBottoniCampi(self):
        self.viewCampi.vistaPrenotazioni.visualizzaprenotazioni.clicked.connect(self.passaVisualizzaCampi)

    def passaVisualizzaCampi(self):
        self.viewCampi.vistaPrenotazioni.window = QtWidgets.QMainWindow()
        self.viewCampi.vistaCampi.setupUi(self.viewCampi.vistaPrenotazioni.window)
        self.uploadTable()
        self.viewCampi.vistaPrenotazioni.window.show()

        #funzioni per farlo funzionare
        self.changeLabel()

        #funzioni per tornare indietro alla home prenotazioni
        self.viewCampi.vistaCampi.tornahome.clicked.connect(self.passaCampi)
        self.viewCampi.vistaCampi.tornahome.clicked.connect(self.viewCampi.vistaPrenotazioni.window.close)

    def ottieniData(self):
        #prendiamo la data, la carichiamo su una variabile e la pasisamo alla funzione per visualizzare i campi, cambia
        #la label e poi la utilizziamo per il database. Il bottone ci fa passare all'altra finestra
        result = self.viewCampi.vistaPrenotazioni.setgiorno.date().toPyDate()
        self.datePy = result.strftime("%Y-%m-%d")



    def changeLabel(self):
        self.viewCampi.vistaCampi.annomesegiorno.setText(self.datePy)


    def uploadTable(self):
        query = "SELECT  id_giocatore1, id_giocatore2, id_giocatore3, id_giocatore4, tipo_campo, orario_prenotazione FROM Campi WHERE data_prenotazione ='%s' " % (''.join(self.datePy))
        rowIndex = 0
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
                self.viewCampi.vistaCampi.calcetto.setItem(time, 0, QtWidgets.QTableWidgetItem(id1))

