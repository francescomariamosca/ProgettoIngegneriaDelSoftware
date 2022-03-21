import sys

from Sicurezza.Login.Controller.LoginController import LoginController
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = LoginController()
    sys.exit(app.exec_())

