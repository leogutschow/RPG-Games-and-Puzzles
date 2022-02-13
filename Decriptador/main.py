from Scripts import Enigma_Main
import sys
from UI.main_window import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from playsound import playsound
from threading import Thread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.AdiBtn1.clicked.connect(self.add)
        self.AdiBtn2.clicked.connect(self.add)
        self.AdiBtn3.clicked.connect(self.add)
        self.TiraBtn1.clicked.connect(self.tira)
        self.TiraBtn2.clicked.connect(self.tira)
        self.TiraBtn3.clicked.connect(self.tira)
        self.CryptBtn.clicked.connect(self.crypt)


    def play_sound(self):
        playsound('Sounds/gear_sound.mp3')

    def add(self):
        obj = self.sender()
        thread = Thread(target=self.play_sound).start() 
        if obj.objectName() == "AdiBtn1":
            if int(self.RotorLabel1.text()) < 25:
                self.RotorLabel1.setText(str(int(self.RotorLabel1.text())+1))
                             
        if obj.objectName() == "AdiBtn2":
            if int(self.RotorLabel2.text()) < 25:
                self.RotorLabel2.setText(str(int(self.RotorLabel2.text())+1))
                

        if obj.objectName() == "AdiBtn3":
            if int(self.RotorLabel3.text()) < 25:
                self.RotorLabel3.setText(str(int(self.RotorLabel3.text())+1))
                

    def tira(self):
        obj = self.sender()
        thread = Thread(target=self.play_sound).start() 
        if obj.objectName() == "TiraBtn1":
            if int(self.RotorLabel1.text()) > 0:
                self.RotorLabel1.setText(str(int(self.RotorLabel1.text())-1))
               

        if obj.objectName() == "TiraBtn2":
            if int(self.RotorLabel2.text()) > 0:
                self.RotorLabel2.setText(str(int(self.RotorLabel2.text())-1))
                

        if obj.objectName() == "TiraBtn3":
            if int(self.RotorLabel3.text()) > 0:
                self.RotorLabel3.setText(str(int(self.RotorLabel3.text())-1))
                

    def crypt(self):
        text = self.CryptLine.toPlainText()
        thread = Thread(target=self.play_sound).start()
        pos_rotor = self.RotorLabel1.text() + "," + self.RotorLabel2.text() + "," + self.RotorLabel3.text()
        self.DecryptLine.setText(Enigma_Main.enigma(pos_rotor, text))
        
    
    

if __name__ ==  "__main__":
    qt = QApplication(sys.argv)
    app = MainWindow()
    app.show()
    qt.exec_()

    