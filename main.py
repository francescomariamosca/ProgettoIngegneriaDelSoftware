import sys

from Sicurezza.Login.Logica.LoginLogica import LoginLogica
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = LoginLogica()
    sys.exit(app.exec_())

