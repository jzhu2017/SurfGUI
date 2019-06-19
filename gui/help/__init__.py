from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QFont

class Help(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Add help info here")

        self.initialize()

    def initialize(self):
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)