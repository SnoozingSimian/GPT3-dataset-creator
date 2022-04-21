# Built ins
import os

# Local imports
from src.data_parser import parse_data
from src.data_stack import DataStack

# Third party imports
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, dataDir, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.dataStack = DataStack()
        self.mainWidget = QWidget()
        self.dataDir = dataDir

        if not os.path.exists(self.dataDir):
            raise FileNotFoundError()
        
        self.setCentralWidget(self.mainWidget)
        self.initUI()

    def initUI(self):
        actions = QLabel('Actions')
        emotes = QLabel('Emotes')
        prompt = QLabel('Prompt')
        answer = QLabel('Answer')
        file = QLabel('Filename')

        self.actionsEdit = QLineEdit()
        self.emotesEdit = QLineEdit()
        self.fileEdit = QLineEdit()
        self.promptEdit = QTextEdit()
        self.answerEdit = QTextEdit()

        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(actions, 1, 0)
        grid.addWidget(self.actionsEdit, 2, 0)
        grid.addWidget(emotes, 1, 2)
        grid.addWidget(self.emotesEdit, 2, 2)
        grid.addWidget(prompt, 5, 0)
        grid.addWidget(self.promptEdit, 6, 0, 3, 1)
        grid.addWidget(answer, 5, 2)
        grid.addWidget(self.answerEdit, 6, 2, 3, 3)
        grid.addWidget(file, 11, 0)
        grid.addWidget(self.fileEdit, 11, 2)            

        addBtn = QPushButton("Add Another")
        addBtn.clicked.connect(self.addData)
        grid.addWidget(addBtn, 13, 0)

        saveBtn = QPushButton("Save")
        saveBtn.clicked.connect(self.saveDataset)
        grid.addWidget(saveBtn, 13, 2)
        
        self.mainWidget.setLayout(grid)        
        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle("GPT3 Dataset Creator")
        self.statusBar()


    # Escape key closes window
    def keyPressEvent(self, e):    
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()


    def addData(self):
        # data = get_data() -> data sent from the window
        data = {}
        data['actions'] = self.actionsEdit.text()
        data['emotes'] = self.emotesEdit.text()
        data['prompt'] = self.promptEdit.toPlainText()
        data['answer'] = self.answerEdit.toPlainText()

        parsed_data = parse_data(data)
        self.dataStack.pushData(parsed_data)

        self.promptEdit.setText("")
        self.answerEdit.setText("")


    def saveDataset(self):
        filename = self.fileEdit.text()

        os.makedirs("data", 711, exist_ok = True)
        
        msg, status = self.dataStack.writeToFile(os.path.join(self.dataDir, filename))
        message = f"{msg}\nstatus = {status}"
        self.statusBar().showMessage(message)
        
        self.actionsEdit.setText("")
        self.emotesEdit.setText("")
        self.fileEdit.setText("")
        self.promptEdit.setText("")
        self.answerEdit.setText("")
