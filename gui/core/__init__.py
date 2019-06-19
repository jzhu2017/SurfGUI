from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

class Core(QWidget):
    def __init__(self):
        super().__init__()
        # creates two overall layouts
        self.layout = QVBoxLayout()
        self.form = QFormLayout()

        # creates text widgets
        self.welcomeTitle = QLabel("Welcome")
        self.welcomeText = QLabel("Welcome text here")
        self.emptyLine = QLabel()
        self.tabTitle = QLabel("Settings File - Core Classes")
        self.tabText = QLabel("Brief instructions here")

        # creates button
        self.buttonSize = QSize(150, 25)
        self.changeButton = QPushButton("Change Core Settings", self)

        # creates input lines
        self.dsLineEdit = QLineEdit()
        self.preLineEdit = QLineEdit()
        self.proLineEdit = QLineEdit()
        self.parLineEdit = QLineEdit()
        self.exLineEdit = QLineEdit()
        self.conLineEdit = QLineEdit()

        self.initialize()

    def initialize(self):
        # sets settings for font
        self.welcomeTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))
        self.welcomeText.setFont(QFont('Sans Serif', 9))
        self.tabTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))
        self.tabText.setFont(QFont('Sans Serif', 9))

        # sets setting for button and connects to method if clicked
        self.changeButton.setFixedSize(self.buttonSize)
        self.changeButton.clicked.connect(self.if_clicked)

        # adds the inputs for the core files to the form
        self.form.addRow(QLabel("Document Source: "), self.dsLineEdit)
        self.form.addRow(QLabel("Preprocessor: "), self.preLineEdit)
        self.form.addRow(QLabel("Processor: "), self.proLineEdit)
        self.form.addRow(QLabel("Parser: "), self.parLineEdit)
        self.form.addRow(QLabel("Extractor: "), self.exLineEdit)
        self.form.addRow(QLabel("Converter: "), self.conLineEdit)

        # adds everything to overall layout
        self.setLayout(self.layout)
        self.layout.addWidget(self.welcomeTitle)
        self.layout.addWidget(self.welcomeText)
        self.layout.addWidget(self.emptyLine)
        self.layout.addWidget(self.tabTitle)
        self.layout.addWidget(self.tabText)
        self.layout.addWidget(self.changeButton)

    def if_clicked(self):
        # disables button and makes the form inputs visible
        self.changeButton.setEnabled(False)
        self.layout.addLayout(self.form)