import sys
from PyQt4 import QtGui, QtCore

class windowGUI:
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.window = QtGui.QWidget()
        self.setMenuBar()       
        
    def setMenuBar(self):
        self.menuBar = QtGui.QMenuBar(self.window)  
        self.setFileMenu()
        self.setTraductorMenu()

    def setFileMenu(self):        
        self.fileMenu = self.menuBar.addMenu('File')
        # Open option
        self.openFileAction = QtGui.QAction( 'Open file', self.window )
        self.fileMenu.addAction(self.openFileAction)
        self.openFileAction.triggered.connect( lambda: self.openFileDialog() )
        # Save option
        self.saveFileAction = QtGui.QAction( 'Save file', self.window )
        self.fileMenu.addAction(self.saveFileAction)
        self.saveFileAction.triggered.connect( lambda: self.saveFileDialog() )
        # Save as option
        self.saveAsFileAction = QtGui.QAction( 'Save As...', self.window )
        self.fileMenu.addAction(self.saveAsFileAction)
        self.saveAsFileAction.triggered.connect( lambda: self.saveAsFileDialog() )
        # Close option
        self.closeFileAction = QtGui.QAction( 'Close file', self.window )
        self.fileMenu.addAction(self.closeFileAction)
        self.closeFileAction.triggered.connect( lambda: self.closeFileDialog() )
        # Exit option

    def openFileDialog(self):
        self.openFileName = QtGui.QFileDialog.getOpenFileName( self.window, 'Open file', '~', 'Programs (*.prg)')
    
    def saveFileDialog(self):
        self.saveFileName = QtGui.QFileDialog.getSaveFileName( self.window, 'Save file', '~' )

    def saveAsFileDialog(self):
        self.saveAsFileName = QtGui.QFileDialog.getSaveFileNameAndFilter( self.window, 'Save As..', '~')
    
    def closeFileDialog(self):
        self.closeFileName = QtGui.QFileDialog.getExistingDirectory( self.window, 'Close file', '~', quit ) 

    def setTraductorMenu(self):
        self.traductorMenu = self.menuBar.addMenu('Traductor')    

    def showWindow(self):
        self.window.setWindowTitle('Code Translator')
        self.window.setWindowIcon( QtGui.QIcon ('../icons/logo/icons8-google-code.png') )
        # resizing the window to W:90% x H:80% of the screen
        screenWidth = self.screen.width()
        screenHeight = self.screen.height()
        self.window.resize( screenWidth*.9, screenHeight*.8 ) 
        # moving the window to the center of the screen
        windowWidth = self.window.frameSize().width()
        windowHeight = self.window.frameSize().height()
        self.window.move( screenWidth/2 - windowWidth/2, screenHeight/2 - windowHeight/2 )

        self.window.show()  
        sys.exit(self.app.exec_())   

