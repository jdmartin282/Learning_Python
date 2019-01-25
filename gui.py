import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import QIcon


__version__ = '1.0.0'


class Application(QMainWindow):
    def __init__(self, title, left=40, top=40, width=640, height=480):
        super().__init__()
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.mainMenu = self.menuBar()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createMenuBar()
        button = QPushButton('Click me', self)
        button.setToolTip('Thank you for thinking about me')
        button.clicked.connect(self.temp)
        button.move(0, 20)

    def temp(self):
        self.updateStatus('Test')

    def createMenuBar(self):
        self.createFileMenu()
        self.createEditMenu()
        self.createViewMenu()
        self.createSearchMenu()
        self.createToolsMenu()
        self.createHelpMenu()

    def createFileMenu(self):
        fileMenu = self.mainMenu.addMenu('File')

        newButton = QAction(QIcon('new.png'), 'New', self)
        newButton.setShortcut('Ctrl+N')
        newButton.setStatusTip('Create New Character')
        newButton.triggered.connect(self.createNewCharacter)

        saveButton = QAction(QIcon('save.png'), 'Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.setStatusTip('Save Character')
        saveButton.triggered.connect(self.createNewCharacter)

        loadButton = QAction(QIcon('load.png'), 'Load', self)
        loadButton.setShortcut('Ctrl+L')
        loadButton.setStatusTip('Load Character')
        loadButton.triggered.connect(self.createNewCharacter)

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        fileMenu.addAction(newButton)
        fileMenu.addAction(saveButton)
        fileMenu.addAction(loadButton)
        fileMenu.addAction(exitButton)

    def createEditMenu(self):
        editMenu = self.mainMenu.addMenu('Edit')

    def createViewMenu(self):
        viewMenu = self.mainMenu.addMenu('View')

    def createSearchMenu(self):
        searchMenu = self.mainMenu.addMenu('Search')

    def createToolsMenu(self):
        toolsMenu = self.mainMenu.addMenu('Tools')

    def createHelpMenu(self):
        helpMenu = self.mainMenu.addMenu('Help')

    # TODO: Create New Character Logic
    def createNewCharacter(self):
        pass

    def updateStatus(self, statusMessage):
        self.statusBar().showMessage(statusMessage)


if __name__ == '__main__':
        app = QApplication(sys.argv)
        mainPage = Application(title=f'Dungeons & Dragons - Character Creator - Version: {__version__}')
        mainPage.updateStatus('In Development')
        mainPage.show()
        sys.exit(app.exec_())
