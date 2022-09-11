import sys
from time import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic

class UI(QWidget):
    def __init__(self):
        self.start()
        self.set()
    
    def start(self):
        self.ui = uic.loadUi('calculator.ui')
        self.ui.show()

    def set(self):
        self.ui.pushbutton0.clicked.connect(lambda: self.click(num=0))
        self.ui.pushbutton1.clicked.connect(lambda: self.click(num=1))
        self.ui.pushbutton2.clicked.connect(lambda: self.click(num=2))
        self.ui.pushbutton3.clicked.connect(lambda: self.click(num=3))
        self.ui.pushbutton4.clicked.connect(lambda: self.click(num=4))
        self.ui.pushbutton5.clicked.connect(lambda: self.click(num=5))
        self.ui.pushbutton6.clicked.connect(lambda: self.click(num=6))
        self.ui.pushbutton7.clicked.connect(lambda: self.click(num=7))
        self.ui.pushbutton8.clicked.connect(lambda: self.click(num=8))
        self.ui.pushbutton9.clicked.connect(lambda: self.click(num=9))

        self.ui.pushbuttonplus.clicked.connect(lambda: self.click_equation('+'))
        self.ui.pushbuttonminus.clicked.connect(lambda: self.click_equation('-'))
        self.ui.pushbuttonmulti.clicked.connect(lambda: self.click_equation('*'))
        self.ui.pushbuttondivide.clicked.connect(lambda: self.click_equation('/'))
        self.ui.pushbuttoncomma.clicked.connect(lambda: self.click('.'))

        self.ui.pushbuttonequal.clicked.connect(lambda: self.answer())
        self.ui.pushbuttonbackspace.clicked.connect(lambda: self.back())
        self.ui.pushbuttonsquare.clicked.connect(lambda: self.square())

    def square(self):
        x = self.ui.label.text()
        x = round(float(x)**0.5, 5)
        self.ui.label.setText(str(x))

    def back(self):
        x = self.ui.label.text()
        x = x[:-1]
        self.ui.label.setText(x)

    def click(self, num=0):
        self.display(text=num)


    def click_equation(self,num):
        global answer1
        self.display(num)    
        answer1 = self.ui.label.text()
        self.ui.label.setText('0')

    def answer(self):
        answer2 = answer1 + self.ui.label.text()
        if '/0' in answer2:
            self.ui.label.setText('ERROR')
        else:
            answer2 = str(eval(answer2))
            self.ui.label.setText(answer2)


    def display(self, text='0'):

        old_text = self.ui.label.text()

        if old_text =='0':
            old_text = ''
        new_text = old_text + str(text)
        self.ui.label.setText(new_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    uiWindow = UI()
    app.exec_()