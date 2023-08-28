import PyQt5.QtWidgets as qtw
from degisn import Ui_MainWindow
import random
from wait_for import wait_for  

game = qtw.QApplication([])

class window(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        x = int(input("1) 1 vs 1 \n2) 1 Vs Computer")) 
        self.setupUi(self)
        self.button_list = [self.b1,self.b2,self.b3,self.b5,self.b6,self.b7,self.b8,self.b9,self.b10]
        self.counter = 0
        if x == 1:
            self.b1.clicked.connect(lambda: self.clicker(self.b1))
            self.b2.clicked.connect(lambda: self.clicker(self.b2))
            self.b3.clicked.connect(lambda: self.clicker(self.b3))
            self.b5.clicked.connect(lambda: self.clicker(self.b5))
            self.b6.clicked.connect(lambda: self.clicker(self.b6))
            self.b7.clicked.connect(lambda: self.clicker(self.b7))
            self.b8.clicked.connect(lambda: self.clicker(self.b8))
            self.b9.clicked.connect(lambda: self.clicker(self.b9))
            self.b10.clicked.connect(lambda: self.clicker(self.b10))
        elif x == 2:

            self.b1.clicked.connect(lambda: self.b1.setText("O"))
            self.b2.clicked.connect(lambda: self.b2.setText("O"))
            self.b3.clicked.connect(lambda: self.b3.setText("O"))
            self.b5.clicked.connect(lambda: self.b5.setText("O"))
            self.b6.clicked.connect(lambda: self.b6.setText("O"))
            self.b7.clicked.connect(lambda: self.b7.setText("O"))
            self.b8.clicked.connect(lambda: self.b8.setText("O"))
            self.b9.clicked.connect(lambda: self.b9.setText("O"))
            self.b10.clicked.connect(lambda: self.b10.setText("O"))

            self.b1.clicked.connect(lambda: self.button_list.remove(self.b1))
            self.b2.clicked.connect(lambda: self.button_list.remove(self.b2))
            self.b3.clicked.connect(lambda:  self.button_list.remove(self.b3))
            self.b5.clicked.connect(lambda: self.button_list.remove(self.b5))
            self.b6.clicked.connect(lambda: self.button_list.remove(self.b6))
            self.b7.clicked.connect(lambda: self.button_list.remove(self.b7))
            self.b8.clicked.connect(lambda: self.button_list.remove(self.b8))
            self.b9.clicked.connect(lambda: self.button_list.remove(self.b9))
            self.b10.clicked.connect(lambda: self.button_list.remove(self.b10))
            
            self.b1.clicked.connect(lambda: self.comp_choice())
            self.b2.clicked.connect(lambda: self.comp_choice())
            self.b3.clicked.connect(lambda: self.comp_choice())
            self.b5.clicked.connect(lambda: self.comp_choice())
            self.b6.clicked.connect(lambda: self.comp_choice())
            self.b7.clicked.connect(lambda: self.comp_choice())
            self.b8.clicked.connect(lambda: self.comp_choice())
            self.b9.clicked.connect(lambda: self.comp_choice())
            self.b10.clicked.connect(lambda: self.comp_choice())
            
    def comp_choice(self):
                    counter = 0
                    while True:
                                        
                        self.computer_choice = random.choice(self.button_list)
                        if self.computer_choice.text() != "O" and self.computer_choice.text() != "X":
                            self.computer_choice.setText("X")
                            counter=0
                            break
                        else:
                             counter+=1
                             if counter == 200:
                                  break
                             
                             continue
                             
                              
    
                     
                     
                     
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

