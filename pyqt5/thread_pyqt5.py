import serial
from PyQt5.QtCore import pyqtSignal, QThread

class serialThreadClass(QThread):
    mesaj = pyqtSignal(str)

    def __init__(self, parent=None):
        super(serialThreadClass,self).__init__(parent)
        self.serl = serial.Serial()
                self.serl = serial.Serial()



    def run(self):
        qwe = 1
