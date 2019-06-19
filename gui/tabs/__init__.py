from PyQt5.QtWidgets import *
from gui.core import Core
from gui.filter import Filter
from gui.io import IO
from gui.run import Run
from gui.help import Help

class Tabs(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # creates the widget that will contain the five tabs
        self.tabs = QTabWidget()

        # creates the five tabs
        self.coreTab = QWidget()
        self.filterTab = QWidget()
        self.ioTab = QWidget()
        self.runTab = QWidget()
        self.helpTab = QWidget()

        # creates the layout
        self.layout = QVBoxLayout()
        self.initialize()

        # initializes the five tabs
        self.coreTabUI()
        self.filterTabUI()
        self.ioTabUI()
        self.runTabUI()
        self.helpTabUI()

        # adds the tabs to the layout
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def initialize(self):
        # adds the five tabs to the tabs widget
        self.tabs.addTab(self.coreTab, "Core Settings")
        self.tabs.addTab(self.filterTab, "Filter Settings")
        self.tabs.addTab(self.ioTab, "I/O Settings")
        self.tabs.addTab(self.runTab, "Run")
        self.tabs.addTab(self.helpTab, "Help")

    def coreTabUI(self):
        # initializes the core tab
        self.coreTab.layout = QFormLayout()
        self.coreTab.layout.addWidget(Core())
        self.coreTab.setLayout(self.coreTab.layout)

    def filterTabUI(self):
        # initializes the filter tab
        self.filterTab.layout = QFormLayout()
        self.filterTab.layout.addWidget(Filter())
        self.filterTab.setLayout(self.filterTab.layout)

    def ioTabUI(self):
        # initializes the i/o tab
        self.ioTab.layout = QFormLayout()
        self.ioTab.layout.addWidget(IO())
        self.ioTab.setLayout(self.ioTab.layout)

    def runTabUI(self):
        # initializes the run tab
        self.runTab.layout = QFormLayout()
        self.runTab.layout.addWidget(Run())
        self.runTab.setLayout(self.runTab.layout)

    def helpTabUI(self):
        # initializes the help tab
        self.helpTab.layout = QFormLayout()
        self.helpTab.layout.addWidget(Help())
        self.helpTab.setLayout(self.helpTab.layout)