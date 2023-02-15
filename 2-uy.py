from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QLineEdit


app = QApplication([])
oyna = QWidget()
oyna.setFixedSize(300, 300)
oyna.setWindowTitle("Masala-2")

lbl = QLabel("Ism", oyna)
lbl.setGeometry(25, 25, 200, 50)
lbl.setStyleSheet("font-size: 25px")


lbl1 = QLabel("Familiya", oyna)
lbl1.setGeometry(25, 125, 200, 50)
lbl1.setStyleSheet("font-size: 25px")

lbl2 = QLabel("Yosh", oyna)
lbl2.setGeometry(25, 225, 200, 50)
lbl2.setStyleSheet("font-size: 25px")

edit = QLineEdit(oyna)
edit.setGeometry(125, 25, 150, 50)
edit.setStyleSheet("font-size: 25px")

edit1 = QLineEdit(oyna)
edit1.setGeometry(125, 125, 150, 50)
edit1.setStyleSheet("font-size: 25px")

edit2 = QLineEdit(oyna)
edit2.setGeometry(125, 225, 150, 50)
edit2.setStyleSheet("font-size: 25px")


oyna.show()
app.exec_()