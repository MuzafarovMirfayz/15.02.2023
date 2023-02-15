from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


app = QApplication([])
oyna = QWidget()
oyna.setFixedSize(300, 300)
oyna.setWindowTitle("Masala-3")
lst = [input("Ismingizni kiriting-> "), input("Familayangizni kiriting-> "), input("Yoshingizni kiriting-> ")]
def ism():
    lbl.setText(lst[0])
def fam():
    lbl.setText(lst[1])
def yosh():
    lbl.setText(lst[2])
lbl = QLabel(oyna)
lbl.setGeometry(100, 25, 200, 50)
lbl.setStyleSheet("font-size: 25px")
but = QPushButton("I", oyna)
but.setGeometry(25, 150, 50, 100)
but.clicked.connect(ism)
but1 = QPushButton("F", oyna)
but1.setGeometry(125, 150, 50, 100)
but1.clicked.connect(fam)
but2 = QPushButton("Y", oyna)
but2.setGeometry(225, 150, 50, 100)
but2.clicked.connect(yosh)
oyna.show()
app.exec_()