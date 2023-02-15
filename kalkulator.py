from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
app = QApplication([])
oyna = QWidget()
oyna.setFixedSize(400, 450)
a = ""
def son1():
    lbl.setText(lbl.text()+"1")
def son2():
    lbl.setText(lbl.text()+"2")
def son3():
    lbl.setText(lbl.text()+"3")
def son4():
    lbl.setText(lbl.text() +"4")
def son5():
    lbl.setText(lbl.text() +"5")
def son6():
    lbl.setText(lbl.text() +"6")
def son7():
    lbl.setText(lbl.text() +"7")
def son8():
    lbl.setText(lbl.text() +"8")
def son9():
    lbl.setText(lbl.text() +"9")
def son0():
    lbl.setText(lbl.text() +"0")
def sonv():
    lbl.setText(lbl.text() +".")
def ko():
    if len(lbl.text())>0:
        if lbl.text()[-1] == '-' or lbl.text()[-1] == '+' or lbl.text()[-1] == '/' or lbl.text().count("*")!=0:
            c =lbl.text()[::-1].replace(lbl.text()[-1], "", 1)
            lbl.setText(c[::-1]+"*")
        else: 
            lbl.setText(lbl.text() +"*")
    else:
            lbl.setText("0*")
def bo():
    if len(lbl.text())>0:
        if lbl.text()[-1] == '-' or lbl.text()[-1] == '+' or lbl.text()[-1] == '*' or lbl.text().count("/")!=0:
            c =lbl.text()[::-1].replace(lbl.text()[-1], "", 1)
            lbl.setText(c[::-1]+"/")
        else: 
            lbl.setText(lbl.text() +"/")
    else:
            lbl.setText("0/")
def qo():
    if len(lbl.text())>0:
        if lbl.text()[-1] == '-' or lbl.text()[-1] == '/' or lbl.text()[-1] == '*'  or lbl.text().count("+")!=0:
            c =lbl.text()[::-1].replace(lbl.text()[-1], "", 1)
            lbl.setText(c[::-1]+"+")
        else: 
            lbl.setText(lbl.text() +"+")
    else:
            lbl.setText("0+")
def ay():
    if len(lbl.text())>0:
        if lbl.text()[-1] == '+' or lbl.text()[-1] == '/' or lbl.text()[-1] == '*'  or lbl.text().count("-")!=0:
            c =lbl.text()[::-1].replace(lbl.text()[-1], "", 1)
            lbl.setText(c[::-1]+"-")
        else: 
            lbl.setText(lbl.text() +"-")
    else:
            lbl.setText("0-")
def c():
    if len(lbl.text())>0:
        lbl.setText(lbl.text()[::-1].replace(lbl.text()[-1], "", 1)[::-1])
def ac():
    lbl.setText("")
def tengla():
    try:
        uzb = lbl.text()
        if lbl.text().count('*')>0 and lbl.text().count('/')==0:
            b = lbl.text().split('*')
            ac()
            if b[0].count(".")>0:
                c = float(b[0])*float(b[1])
            elif b[1].count(".")>0:
                c = float(b[0])*float(b[1])
            else:
                c = int(b[0])*int(b[1])
            if c==int(c):
                lbl.setText(str(int(c)))
            else:
                lbl.setText(str(c))
        elif lbl.text().count('/')>0:
            b = lbl.text().split('/')
            ac()
            if int(b[1])==0:
                lbl.setText("Error")
            else:
                if b[0].count(".")>0:
                    c = float(b[0])/float(b[1])
                elif b[1].count(".")>0:
                    c = float(b[0])/float(b[1])
                else:
                    c = int(b[0])/int(b[1])
                if c==int(c):
                    lbl.setText(str(int(c)))
                else:
                    lbl.setText(str(c))
        elif lbl.text().count('+')>0:
            b = lbl.text().split('+')
            ac()
            if b[0].count(".")>0:
                c = float(b[0])+float(b[1])
            elif b[1].count(".")>0:
                c = float(b[0])+float(b[1])
            else:
                c = int(b[0])+int(b[1])
            if c==int(c):
                lbl.setText(str(int(c)))
            else:
                lbl.setText(str(c))
        elif lbl.text().count('-')>0:
            b = lbl.text().split('-')
            ac()
            if b[0].count(".")>0:
                c = float(b[0])-float(b[1])
            elif b[1].count(".")>0:
                c = float(b[0])-float(b[1])
            else:
                c = int(b[0])-int(b[1])
            if c==int(c):
                lbl.setText(str(int(c)))
            else:
                lbl.setText(str(c))
    except:
        lbl.setText(uzb)
def fo():
    try:
        if lbl.text().count("/")>0:
            if lbl.text().count('.')==0:
                f = str(int(lbl.text().split("/")[1])/100)
                for i in range(len(lbl.text().split("/")[1])):
                    c()
                lbl.setText(lbl.text()+f)
            else:
                f = str(float(lbl.text().split("/")[1])/100)
                for i in range(len(lbl.text().split("/")[1])):
                    c()
                lbl.setText(lbl.text()+f)
        elif lbl.text().count('*')>0:
            if lbl.text().count('.')==0:
                f = str(int(lbl.text().split("*")[1])/100)
                for i in range(len(lbl.text().split("*")[1])):
                    c()
                lbl.setText(lbl.text()+f)
            else:
                f = str(float(lbl.text().split("*")[1])/100)
                for i in range(len(lbl.text().split("*")[1])):
                    c()
                lbl.setText(lbl.text()+f)                
        elif lbl.text().count('+')>0:
            if lbl.text().count('.')==0:
                f = str(int(lbl.text().split("*")[1])/100)
                for i in range(len(lbl.text().split("+")[1])):
                    c()
                lbl.setText(lbl.text()+f)
            else:
                f = str(float(lbl.text().split("*")[1])/100)
                for i in range(len(lbl.text().split("+")[1])):
                    c()
                lbl.setText(lbl.text()+f)                
        elif lbl.text().count('-')>0:
            if lbl.text().count('.')==0:
                f = str(int(lbl.text().split("-")[1])/100)
                for i in range(len(lbl.text().split("-")[1])):
                    c()
                lbl.setText(lbl.text()+f)
            else:
                f = str(float(lbl.text().split("-")[1])/100)
                for i in range(len(lbl.text().split("-")[1])):
                    c()
                lbl.setText(lbl.text()+f)
        else:
            if lbl.text().count('.')==0:
                f = str(int(lbl.text())/100)
                for i in range(len(lbl.text())):
                    c()
                lbl.setText(lbl.text()+f)
            else:
                f = str(float(lbl.text())/100)
                for i in range(len(lbl.text())):
                    c()
                lbl.setText(lbl.text()+f)                
    except:
        pass
lbl = QLabel("", oyna)
lbl.setGeometry(150, 10, 490, 100)
lbl.setStyleSheet("color:black; font-size: 25px")
butac = QPushButton('AC', oyna)
butac.setGeometry(25, 150, 50, 50)
butac.clicked.connect(ac)
butc = QPushButton('<x]', oyna)
butc.setGeometry(125, 150, 50, 50)
butc.clicked.connect(c)
butf = QPushButton('%', oyna)
butf.setGeometry(225, 150, 50, 50)
butf.clicked.connect(fo)
butb = QPushButton('/', oyna)
butb.setGeometry(325, 150, 50, 50)
butb.clicked.connect(bo)
but7 = QPushButton('7', oyna)
but7.setGeometry(25, 200, 50, 50)
but7.clicked.connect(son7)
but8 = QPushButton('8', oyna)
but8.setGeometry(125, 200, 50, 50)
but8.clicked.connect(son8)
but9 = QPushButton('9', oyna)
but9.setGeometry(225, 200, 50, 50)
but9.clicked.connect(son9)
butk = QPushButton('*', oyna)
butk.setGeometry(325, 200, 50, 50)
butk.clicked.connect(ko)
but4 = QPushButton('4', oyna)
but4.setGeometry(25, 250, 50, 50)
but4.clicked.connect(son4)
but5 = QPushButton('5', oyna)
but5.setGeometry(125, 250, 50, 50)
but5.clicked.connect(son5)
but6 = QPushButton("6",oyna)
but6.setGeometry(225, 250, 50, 50)
but6.clicked.connect(son6)
buta = QPushButton('-', oyna)
buta.setGeometry(325, 250, 50, 50)
buta.clicked.connect(ay)
but1 = QPushButton('1', oyna)
but1.setGeometry(25, 300, 50, 50)
but1.clicked.connect(son1)
but2 = QPushButton('2', oyna)
but2.setGeometry(125, 300, 50, 50)
but2.clicked.connect(son2)
but3 = QPushButton("3",oyna)
but3.setGeometry(225, 300, 50, 50)
but3.clicked.connect(son3)
butq = QPushButton('+', oyna)
butq.setGeometry(325, 300, 50, 50)
butq.clicked.connect(qo)
but0 = QPushButton('0', oyna)
but0.setGeometry(125, 350, 50, 50)
but0.clicked.connect(son0)
butv = QPushButton(".",oyna)
butv.setGeometry(225, 350, 50, 50)
butv.clicked.connect(sonv)
butt = QPushButton('=', oyna)
butt.setGeometry(325, 350, 50, 50)
butt.clicked.connect(tengla)
oyna.show()
app.exec_()