from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QFont

class Filter(QWidget):
    def __init__(self):
        super().__init__()
        # creates two overall layouts
        self.layout = QVBoxLayout()
        self.form = QFormLayout()

        # title text
        self.tabTitle = QLabel("Settings File - Filtering")
        self.tabText = QLabel("Filtering instructions here")

        # creates up the five inputs
        self.drInputLayout = QHBoxLayout()
        self.drBrowseButton = QPushButton("Browse")
        self.drLineEdit = QLineEdit()

        self.sfInputLayout = QHBoxLayout()
        self.sfBrowseButton = QPushButton("Browse")
        self.sfLineEdit = QLineEdit()

        self.slInputLayout = QHBoxLayout()
        self.slBrowseButton = QPushButton("Browse")
        self.slLineEdit = QLineEdit()

        self.rInputLayout = QHBoxLayout()
        self.rBrowseButton = QPushButton("Browse")
        self.rLineEdit = QLineEdit()

        self.sptInputLayout = QHBoxLayout()
        self.sptBrowseButton = QPushButton("Browse")
        self.sptLineEdit = QLineEdit()

        self.initialize()

    def initialize(self):
        # sets the five inputs and connects them to method if clicked
        self.tabTitle.setFont(QFont('Sans Serif', 13, QFont.Bold))
        self.tabText.setFont(QFont('Sans Serif', 9))
        self.form.addRow(QLabel("Encoding Errors: "), QLineEdit())
        self.form.addRow(QLabel("Replacement Rule: "), QLineEdit())

        self.drInputLayout.addWidget(self.drLineEdit)
        self.drInputLayout.addWidget(self.drBrowseButton)
        self.form.addRow(QLabel("Dependency Relations: "), self.drInputLayout)
        self.drBrowseButton.clicked.connect(self.drGetFile)

        self.sfInputLayout.addWidget(self.sfLineEdit)
        self.sfInputLayout.addWidget(self.sfBrowseButton)
        self.form.addRow(QLabel("Stop Functions: "), self.sfInputLayout)
        self.sfBrowseButton.clicked.connect(self.sfGetFile)

        self.slInputLayout.addWidget(self.slLineEdit)
        self.slInputLayout.addWidget(self.slBrowseButton)
        self.form.addRow(QLabel("Stop List: "), self.slInputLayout)
        self.slBrowseButton.clicked.connect(self.slGetFile)

        self.rInputLayout.addWidget(self.rLineEdit)
        self.rInputLayout.addWidget(self.rBrowseButton)
        self.form.addRow(QLabel("Replacements: "), self.rInputLayout)
        self.rBrowseButton.clicked.connect(self.rGetFile)

        self.sptInputLayout.addWidget(self.sptLineEdit)
        self.sptInputLayout.addWidget(self.sptBrowseButton)
        self.form.addRow(QLabel("Stop Position Tags: "), self.sptInputLayout)
        self.sptBrowseButton.clicked.connect(self.sptGetFile)

        # adding all of the inputs to overall layout
        self.setLayout(self.layout)
        self.layout.addWidget(self.tabTitle)
        self.layout.addWidget(self.tabText)
        self.layout.addLayout(self.form)

    # browses and retrieves file for all five inputs; txt files only
    def drGetFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.txt')
        self.drLineEdit.setText(file)

    def sfGetFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.txt')
        self.sfLineEdit.setText(file)

    def slGetFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.txt')
        self.slLineEdit.setText(file)

    def rGetFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.txt')
        self.rLineEdit.setText(file)

    def sptGetFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.txt')
        self.sptLineEdit.setText(file)

