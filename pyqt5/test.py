import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import string
#print("na mehet")

class MainWindow(qtw.QWidget):
    def __init__(self,var_title):
        super().__init__()
        self.setWindowTitle(var_title)
        self.setLayout(qtw.QVBoxLayout())
        #label
        my_label = qtw.QLabel("Tulajdonkeppen megy")
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)
        #Entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)
        #button
        my_button = qtw.QPushButton("Nem mered",clicked = lambda:nyomva())
        self.layout().addWidget(my_button)

        #mutasd az appot
        self.show()

        #fgv ide
        def nyomva():
            my_label.setText(my_entry.text())
            my_entry.setText("")

string_title = "Ez lehetne a cim"

app = qtw.QApplication([])
mw = MainWindow(string_title)

if __name__ == "__main__":
    app.exec_()

