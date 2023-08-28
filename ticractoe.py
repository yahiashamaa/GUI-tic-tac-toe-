import PyQt5.QtWidgets as qtw
from degisn import Ui_MainWindow

game = qtw.QApplication([])

class window(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b1.clicked.connect(lambda: self.b1.setText("O"))
        self.b2.clicked.connect(lambda: self.b2.setText("O"))
        self.b3.clicked.connect(lambda: self.b3.setText("O"))
        self.b5.clicked.connect(lambda: self.b5.setText("O"))
        self.b6.clicked.connect(lambda: self.b6.setText("O"))
        self.b7.clicked.connect(lambda: self.b7.setText("O"))
        self.b8.clicked.connect(lambda: self.b8.setText("O"))
        self.b9.clicked.connect(lambda: self.b9.setText("O"))
        self.b10.clicked.connect(lambda: self.b10.setText("O"))

    

win = window()
win.show()
game.exec()

