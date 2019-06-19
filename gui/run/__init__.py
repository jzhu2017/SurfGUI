from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QFont

class Run(QWidget):
    def __init__(self):
        super().__init__()
        # creates the two overall layouts
        self.layout = QVBoxLayout()
        self.form = QFormLayout()

        # creates widgets necessary for the CSV name input
        self.csvLayout = QFormLayout()
        self.csvLineEdit = QLineEdit()

        # creates text widgets
        self.tabTitle = QLabel("Argument Inputs (Required)")
        self.tabText = QLabel("Filtering instructions here")
        self.fileText = QLabel("Files Inputted: ")
        self.empty = QLabel()

        # creates layout and inputs for browsing and submitting input files
        self.inputLayout = QHBoxLayout()
        self.browse = QPushButton("Browse", self)
        self.submit = QPushButton("Submit", self)
        self.inputLineEdit = QLineEdit()

        # creates layout and inputs for running/loading/saving the program with the given settings
        self.runLayout = QHBoxLayout()
        self.run = QPushButton("Run", self)
        self.load = QPushButton("Load Settings", self)
        self.save = QPushButton("Save Settings", self)

        # creates widgets for displaying the outputs
        self.outTitle = QLabel("Output:")
        self.outText = QTextEdit()

        self.initialize()

    def initialize(self):
        # sets settings for font widgets
        self.tabTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))
        self.tabText.setFont(QFont('Sans Serif', 9))
        self.outTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))

        # setting and adding file input widgets to the larger layout
        self.inputLayout.addWidget(self.inputLineEdit)
        self.inputLayout.addWidget(self.browse)
        self.inputLayout.addWidget(self.submit)
        self.form.addRow(QLabel("Input Files: "), self.inputLayout)
        self.browse.clicked.connect(self.browseGetFile)

        # adding widgets to the larger runLayout
        self.runLayout.addWidget(self.run)
        self.runLayout.addWidget(self.load)
        self.runLayout.addWidget(self.save)

        # creating input for CSV file name
        self.csvLayout.addRow(QLabel("CSV File Name: "), self.csvLineEdit)

        # sets the output box to read only
        self.outText.setReadOnly(True)

        # adds everything to the overall layer
        self.setLayout(self.layout)
        self.layout.addWidget(self.tabTitle)
        self.layout.addWidget(self.tabText)
        self.layout.addLayout(self.form)
        self.layout.addWidget(self.fileText)
        self.layout.addLayout(self.csvLayout)
        self.layout.addLayout(self.runLayout)
        self.layout.addWidget(self.empty)
        self.layout.addWidget(self.outTitle)
        self.layout.addWidget(self.outText)

    # browses and retrieves file for input to parmenides
    def browseGetFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.txt')
        self.inputLineEdit.setText(file)