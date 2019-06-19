from PyQt5.QtWidgets import *
from gui.tabs import Tabs

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs_table = Tabs(self)
        self.initialize()

    def initialize(self):
        self.resize(1000, 525)
        self.setWindowTitle("ParmenidesGUI")
        self.setCentralWidget(self.tabs_table)
        self.show()