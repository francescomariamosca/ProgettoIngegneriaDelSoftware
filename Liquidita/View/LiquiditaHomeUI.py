# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LiquiditàUrlodelSium.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class LiquiditaHomeUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.idsocio = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.idsocio.setFont(font)
        self.idsocio.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(221, 214, 73);\n"
                                   "border: 3px solid white;")
        self.idsocio.setText("")
        self.idsocio.setObjectName("idsocio")
        self.gridLayout.addWidget(self.idsocio, 4, 1, 1, 1)
        self.tipologia = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tipologia.setFont(font)
        self.tipologia.setStyleSheet("border-radius: 20px;\n"
                                     "background-color: rgb(221, 214, 73);\n"
                                     "border: 3px solid white;")
        self.tipologia.setObjectName("tipologia")
        self.tipologia.addItem("")
        self.tipologia.addItem("")
        self.gridLayout.addWidget(self.tipologia, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.categorie = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.categorie.setFont(font)
        self.categorie.setStyleSheet("border-radius: 20px;\n"
                                     "background-color: rgb(221, 214, 73);\n"
                                     "border: 3px solid white;")
        self.categorie.setObjectName("categorie")
        self.categorie.addItem("")
        self.categorie.addItem("")
        self.categorie.addItem("")
        self.categorie.addItem("")
        self.categorie.addItem("")
        self.gridLayout.addWidget(self.categorie, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.importo = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.importo.setFont(font)
        self.importo.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(221, 214, 73);\n"
                                   "border: 3px solid white;")
        self.importo.setText("")
        self.importo.setObjectName("importo")
        self.gridLayout.addWidget(self.importo, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.idfornitore = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.idfornitore.setFont(font)
        self.idfornitore.setStyleSheet("border-radius: 20px;\n"
                                       "background-color: rgb(221, 214, 73);\n"
                                       "border: 3px solid white;")
        self.idfornitore.setText("")
        self.idfornitore.setObjectName("idfornitore")
        self.gridLayout.addWidget(self.idfornitore, 2, 1, 1, 1)
        self.id_transazione = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_transazione.sizePolicy().hasHeightForWidth())
        self.id_transazione.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.id_transazione.setFont(font)
        self.id_transazione.setStyleSheet("border-radius: 10px;\n"
                                "background-color: rgb(221, 214, 73);\n"
                                "border: 3px solid white;")
        self.id_transazione.setText("")
        self.id_transazione.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.id_transazione.setObjectName("note")
        self.gridLayout.addWidget(self.id_transazione, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5 , 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.eliminaEntrata = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliminaEntrata.sizePolicy().hasHeightForWidth())
        self.eliminaEntrata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.eliminaEntrata.setFont(font)
        self.eliminaEntrata.setStyleSheet("QPushButton{\n"
                                        "border-radius: 20px;\n"
                                        "background-color: rgb(221, 214, 73);\n"
                                        "border: 3px solid white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgb(255, 255, 155);\n"
                                        "}\n"
                                        "")
        self.eliminaEntrata.setObjectName("insentrata_2")
        self.horizontalLayout.addWidget(self.eliminaEntrata)
        self.insentrata = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insentrata.sizePolicy().hasHeightForWidth())
        self.insentrata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.insentrata.setFont(font)
        self.insentrata.setStyleSheet("QPushButton{\n"
                                      "border-radius: 20px;\n"
                                      "background-color: rgb(221, 214, 73);\n"
                                      "border: 3px solid white;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgb(255, 255, 155);\n"
                                      "}\n"
                                      "")
        self.insentrata.setObjectName("insentrata")
        self.horizontalLayout.addWidget(self.insentrata)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabliquidita = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabliquidita.sizePolicy().hasHeightForWidth())
        self.tabliquidita.setSizePolicy(sizePolicy)
        self.tabliquidita.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabliquidita.setFont(font)
        self.tabliquidita.setStyleSheet("border-radius: 2px;\n"
                                        "background-color: rgb(221, 214, 73);\n"
                                        "border: 1px solid white;")
        self.tabliquidita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabliquidita.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tabliquidita.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabliquidita.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tabliquidita.setObjectName("tabliquidita")
        self.tabliquidita.setColumnCount(6)
        self.tabliquidita.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabliquidita.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabliquidita.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabliquidita.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        item.setFont(font)
        self.tabliquidita.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        item.setFont(font)
        self.tabliquidita.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabliquidita.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_2.addWidget(self.tabliquidita)
        self.tabsoci = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabsoci.setFont(font)
        self.tabsoci.setStyleSheet("border-radius: 2px;\n"
                                   "background-color: rgb(221, 214, 73);\n"
                                   "border: 1px solid white;")
        self.tabsoci.setObjectName("tabsoci")
        self.tabsoci.setColumnCount(2)
        self.tabsoci.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabsoci.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabsoci.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.tabsoci)
        self.tabfornitori = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabfornitori.setFont(font)
        self.tabfornitori.setStyleSheet("border-radius: 2px;\n"
                                        "background-color: rgb(221, 214, 73);\n"
                                        "border: 1px solid white;")
        self.tabfornitori.setObjectName("tabfornitori")
        self.tabfornitori.setColumnCount(2)
        self.tabfornitori.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabfornitori.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabfornitori.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.tabfornitori)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.tornahome = QtWidgets.QCommandLinkButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.tornahome.setFont(font)
        self.tornahome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "")
        icon = QtGui.QIcon.fromTheme("null")
        self.tornahome.setIcon(icon)
        self.tornahome.setObjectName("tornahome")
        self.gridLayout_2.addWidget(self.tornahome, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tipologia.setItemText(0, _translate("MainWindow", "ENTRATA"))
        self.tipologia.setItemText(1, _translate("MainWindow", "USCITA"))
        self.label_10.setText(_translate("MainWindow", "Tipologia"))
        self.categorie.setItemText(0, _translate("MainWindow", "Quota Sociale"))
        self.categorie.setItemText(1, _translate("MainWindow", "Utenze"))
        self.categorie.setItemText(2, _translate("MainWindow", "Sponsorizzazioni"))
        self.categorie.setItemText(3, _translate("MainWindow", "Stipendi"))
        self.categorie.setItemText(4, _translate("MainWindow", "Pagamento Fornitori"))
        self.label_9.setText(_translate("MainWindow", "Categoria"))
        self.label_4.setText(_translate("MainWindow", "ID Socio"))
        self.label_2.setText(_translate("MainWindow", "Importo"))
        self.label_11.setText(_translate("MainWindow", "ID Fornitore"))
        self.label_5.setText(_translate("MainWindow", "ID Movimento:"))
        self.eliminaEntrata.setText(_translate("MainWindow", "Elimina Movimento"))
        self.insentrata.setText(_translate("MainWindow", "Inserisci nella Liquidità"))
        self.label_8.setText(_translate("MainWindow", "Gestione Liquidità"))
        item = self.tabliquidita.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.tabliquidita.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "€"))
        item = self.tabliquidita.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipologia"))
        item = self.tabliquidita.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID Socio"))
        item = self.tabliquidita.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID Fornitore"))
        item = self.tabliquidita.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabsoci.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Socio"))
        item = self.tabsoci.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome Socio"))
        item = self.tabfornitori.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Fornitore"))
        item = self.tabfornitori.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome Fornitore"))
        self.tornahome.setText(_translate("MainWindow", "Torna alla Home"))
