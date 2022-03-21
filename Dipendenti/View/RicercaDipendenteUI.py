

from PyQt5 import QtCore, QtGui, QtWidgets


class RicercaDipendenteUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 139)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.cf = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.cf.setFont(font)
        self.cf.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"")
        self.cf.setText("")
        self.cf.setObjectName("cf")
        self.gridLayout.addWidget(self.cf, 1, 0, 1, 1)
        self.tornagestdip = QtWidgets.QCommandLinkButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tornagestdip.setFont(font)
        self.tornagestdip.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tornagestdip.setObjectName("tornagestdip")
        self.gridLayout.addWidget(self.tornagestdip, 2, 0, 1, 1)
        self.confermaricercacf = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confermaricercacf.sizePolicy().hasHeightForWidth())
        self.confermaricercacf.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.confermaricercacf.setFont(font)
        self.confermaricercacf.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.confermaricercacf.setObjectName("confermaricercacf")
        self.gridLayout.addWidget(self.confermaricercacf, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inserisci il C.F. del dipendente:"))
        self.tornagestdip.setText(_translate("MainWindow", "Torna a Gestione dipendenti"))
        self.confermaricercacf.setText(_translate("MainWindow", "CONFERMA"))
