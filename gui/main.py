import sys
from PyQt5.QtWidgets import QApplication
from gui.app import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = App()
    sys.exit(app.exec_())