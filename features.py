import sys
from PyQt4.QtGui import *
from core.lexicon import ls

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Tutorial")

        #Widgets
        vbox=QVBoxLayout(self)
        hbox=QHBoxLayout()

        self.combo = QComboBox()
        #lista = ['lista_1', 'lista_2', 'lista_3', 'lista_4']
        
        self.line = QLineEdit()
        self.button = QPushButton('Search')
        self.labelCombo = QLabel("")
        self.labelLine = QLabel('')

        hbox.addWidget(self.labelCombo)
        hbox.addWidget(self.labelLine)
        hbox.addWidget(self.button)

        vbox.addWidget(self.combo)
        vbox.addWidget(self.line)
        vbox.addLayout(hbox)
        #self.combo.currentIndexChanged.connect(self.slot_1)    
        self.combo.currentIndexChanged.connect(            
            lambda: self.slot_1()
        )
        self.line.textChanged.connect(
            lambda: self.labelLine.setText(self.line.text())
        )
        self.button.clicked.connect(
            lambda: self.slot_3()
        )

    def slot_1(self):
        file = open('./db/'+self.combo.currentText(), 'r')
        self.labelCombo.setText(file.read())
        #self.labelCombo.setText(self.combo.currentText())
    def slot_3(self):
        lista = ls('./db/')
        for item in lista:
            self.combo.addItem(item)
        

app = QApplication([])
w = Widget()
w.show()
sys.exit(app.exec_())