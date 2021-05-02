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

        my_label2 = qtw.QLabel("Masik")
        my_label2.setFont(qtg.QFont('Helvetica',20))

        self.layout().addWidget(my_label)
        self.layout().addWidget(my_label2)

        #Entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)
        #button
        my_button = qtw.QPushButton("Nem mered",clicked = lambda:nyomva())
        self.layout().addWidget(my_button)

        my_button2 = qtw.QPushButton("Masik", clicked = lambda: lista())
        self.layout().addWidget(my_button2)

        #Combo box
        combo_box0 = qtw.QComboBox(self)
        combo_box0.addItems(["Chose0", "Chose1", "Chose2", "Chose3"])
        self.layout().addWidget(combo_box0)


        #mutasd az appot
        self.show()

        #fgv ide
        def nyomva():
            my_label.setText(my_entry.text())
            my_entry.setText("")

        def lista():
            my_label2.setText( f'You choose this: {combo_box0.currentIndex()}')

string_title = "Ez lehetne a cim"

if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow(string_title)
    app.exec_()


