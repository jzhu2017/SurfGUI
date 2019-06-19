from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize

class IO(QWidget):
    def __init__(self):
        super().__init__()
        # overall layout for tab
        self.layout = QVBoxLayout()

        # text information for tab
        self.inTabTitle = QLabel("Settings File - Input Control")
        self.inTabText = QLabel("Brief instructions here")
        self.outTabTitle = QLabel("Settings File - Output Control")
        self.outTabText = QLabel("Brief instructions here")
        self.empty = QLabel()

        # two checkboxes for input setting
        self.htmlBox = QCheckBox("HTML")
        self.xmlBox = QCheckBox("XML")

        # button to change I/O settings
        self.changeButton = QPushButton("Change I/O Settings", self)
        self.buttonSize = QSize(150, 25)

        self.initialize()

    def initialize(self):
        # changing settings of the text/buttons
        self.inTabTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))
        self.inTabText.setFont(QFont('Sans Serif', 9))
        self.outTabTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))
        self.outTabText.setFont(QFont('Sans Serif', 9))
        self.changeButton.setFixedSize(self.buttonSize)

        # adding everything to the overall layout
        self.setLayout(self.layout)
        self.layout.addWidget(self.inTabTitle)
        self.layout.addWidget(self.inTabText)
        self.layout.addWidget(self.htmlBox)
        self.layout.addWidget(self.xmlBox)
        self.layout.addWidget(self.empty)
        self.layout.addWidget(self.outTabTitle)
        self.layout.addWidget(self.outTabText)
        self.layout.addWidget(self.changeButton)
