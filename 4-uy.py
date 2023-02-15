from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
app = QApplication([])
oyna = QWidget()
oyna.setFixedSize(300, 300)
oyna.setWindowTitle("Masala-4")
a, b  = [],[]
def go():
    lbl.setText("")
    for i in range(len(edit.text())//2):
        a.append(edit.text()[i])
    for i in range(len(edit1.text())//2):
        b.append(edit1.text()[::-1][i])
    c = ""
    for i in a:
        c = c+i
    for i in b[::-1]:
        c = c+i
    lbl.setText(c)
    a.clear(); b.clear(); c = ''
edit = QLineEdit(oyna)
edit.setGeometry(25, 25, 100, 50)
edit1 = QLineEdit(oyna)
edit1.setGeometry(175, 25, 100, 50)
btn = QPushButton("Go", oyna)
btn.setGeometry(125, 75, 50, 50 )
btn.clicked.connect(go)
lbl = QLabel("", oyna)
lbl.setGeometry(110, 150, 200, 50)
lbl.setStyleSheet("font-size: 25px")
oyna.show()
app.exec_()