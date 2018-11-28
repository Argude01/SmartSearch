import sys
from PyQt4.QtGui import *
from core.lexicon import ls

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Smart Search")
        self.screen = QDesktopWidget().screenGeometry()
        self.window = QWidget()
        #Widgets
        vbox=QVBoxLayout(self)
        hbox=QHBoxLayout()

        self.combo = QComboBox()        
        self.line = QLineEdit()
        self.button = QPushButton('Search')
        self.openDB = QPushButton('Open Directory')
        self.labelDB = QLabel('DataBase location: ')
        self.labelCombo = QLabel("")
        self.labelLine = QLabel('')

        hbox.addWidget(self.line)        
        hbox.addWidget(self.button)       
        
        vbox.addWidget(self.openDB)
        vbox.addWidget(self.labelDB)
        vbox.addLayout(hbox)
        vbox.addWidget(self.labelLine)
        vbox.addWidget(self.combo)
        vbox.addWidget(self.labelCombo)
        
        #self.combo.currentIndexChanged.connect(self.slot_1)    
        self.openDB.clicked.connect(
            lambda: self.slot_openDB()
        )
        self.combo.currentIndexChanged.connect(            
            lambda: self.slot_1()
        )
        self.line.textChanged.connect(
            lambda: self.labelLine.setText('Searching... '+self.line.text())
        )
        self.button.clicked.connect(
            lambda: self.slot_3()
        )

    def slot_1(self):
        file = open('./db/'+self.combo.currentText(), 'r')
        self.labelCombo.setText('Result: '+file.read())
        #self.labelCombo.setText(self.combo.currentText())
    def slot_3(self):
        lista = ls('./db/')
        for item in lista:
            self.combo.addItem(item)
    def slot_openDB(self):
        directory = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        self.labelDB.setText('DataBase location: '+directory)

app = QApplication([])
w = Widget()
w.show()
sys.exit(app.exec_())