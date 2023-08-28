import PyQt5.QtWidgets as qtw
from degisn import Ui_MainWindow

game = qtw.QApplication([])

class window(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.counter = 0

        self.b1.clicked.connect(lambda: self.clicker(self.b1))
        self.b2.clicked.connect(lambda: self.clicker(self.b2))
        self.b3.clicked.connect(lambda: self.clicker(self.b3))
        self.b5.clicked.connect(lambda: self.clicker(self.b5))
        self.b6.clicked.connect(lambda: self.clicker(self.b6))
        self.b7.clicked.connect(lambda: self.clicker(self.b7))
        self.b8.clicked.connect(lambda: self.clicker(self.b8))
        self.b9.clicked.connect(lambda: self.clicker(self.b9))
        self.b10.clicked.connect(lambda: self.clicker(self.b10))

    def clicker(self, b):
         if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
         else:
            mark = "O"
            self.label.setText("X's Turn")
         b.setText(mark)

         self.counter += 1



    

win = window()
win.show()
game.exec()

