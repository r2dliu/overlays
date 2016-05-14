import sys
import webbrowser
from bs4 import BeautifulSoup
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 600, 250)
        self.setWindowTitle("Scoreboard")
        self.setWindowIcon(QtGui.QIcon('pic.png'))

        close = QtGui.QAction("Quit", self)
        close.setShortcut("Ctrl+Q")
        close.setStatusTip('Leave The App')
        close.triggered.connect(self.close_application)

        about = QtGui.QAction("About", self)
        about.setShortcut("Ctrl+H")
        about.setStatusTip('About this app')
        about.triggered.connect(self.display_info)
        
        self.initUI()

    def initUI(self):
            
        scoreFont = QtGui.QFont()
        scoreFont.setBold(True)
        scoreFont.setPointSize(32)
        
        labelP1 = QtGui.QLabel("Player 1", self)
        labelP1.move(15, 20)
        labelP2 = QtGui.QLabel("Player 2", self)
        labelP2.move(530, 20)

        labelA = QtGui.QLabel("Misc. 1", self)
        labelA.move(25, 125)
        labelB = QtGui.QLabel("Camera", self)
        labelB.move(530, 125)
        labelC = QtGui.QLabel("Match", self)
        labelC.move(23, 160)
        labelD = QtGui.QLabel("Misc. 2", self)
        labelD.move(530, 160)
        labelE = QtGui.QLabel("Misc. 3", self)
        labelE.move(23, 195)
        labelF = QtGui.QLabel("Misc. 4", self)
        labelF.move(530, 195)
        
        self.textboxP1 = QtGui.QLineEdit(self)
        self.textboxP1.move(80, 20)
        self.textboxP1.resize(150,30)
        self.textboxP2 = QtGui.QLineEdit(self)
        self.textboxP2.move(370, 20)
        self.textboxP2.resize(150,30)

        self.textboxA = QtGui.QLineEdit(self)
        self.textboxA.move(80, 125)
        self.textboxA.resize(150,30)
        self.textboxB = QtGui.QLineEdit(self)
        self.textboxB.move(370, 125)
        self.textboxB.resize(150,30)
        self.textboxC = QtGui.QLineEdit(self)
        self.textboxC.move(80, 160)
        self.textboxC.resize(150,30)
        self.textboxD = QtGui.QLineEdit(self)
        self.textboxD.move(370, 160)
        self.textboxD.resize(150,30)
        self.textboxE = QtGui.QLineEdit(self)
        self.textboxE.move(80, 195)
        self.textboxE.resize(150,30)
        self.textboxF = QtGui.QLineEdit(self)
        self.textboxF.move(370, 195)
        self.textboxF.resize(150,30)
        
        self.scoreP1 = QtGui.QLineEdit(self)
        self.scoreP1.move(130, 60)
        self.scoreP1.resize(50, 50)
        self.scoreP1.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreP1.setFont(scoreFont)
        self.scoreP1.setText("0");

        self.scoreP2 = QtGui.QLineEdit(self)
        self.scoreP2.move(420, 60)
        self.scoreP2.resize(50, 50)
        self.scoreP2.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreP2.setFont(scoreFont)
        self.scoreP2.setText("0");
        
        p1plus = QtGui.QPushButton(">", self)
        p1plus.clicked.connect(self.increment_P1)
        p1plus.resize(40, 20)
        p1plus.move(180, 75)
        p1minus = QtGui.QPushButton("<", self)
        p1minus.clicked.connect(self.decrement_P1)
        p1minus.resize(40, 20)
        p1minus.move(90, 75)
        p2plus = QtGui.QPushButton(">", self)
        p2plus.clicked.connect(self.increment_P2)
        p2plus.resize(40, 20)
        p2plus.move(470, 75)
        p2minus = QtGui.QPushButton("<", self)
        p2minus.clicked.connect(self.decrement_P2)
        p2minus.resize(40, 20)
        p2minus.move(380, 75)

        swap = QtGui.QPushButton("Swap", self)
        swap.clicked.connect(self.swap)
        swap.resize(100, 30)
        swap.move(250, 20)

        reset = QtGui.QPushButton("Reset", self)
        reset.clicked.connect(self.reset)
        reset.resize(100, 40)
        reset.move(250, 65)

        save = QtGui.QPushButton("Update", self)
        save.clicked.connect(self.save)
        save.resize(100, 100)
        save.move(250, 125)
        self.show()

    def increment_P1(self):
        num = self.scoreP1.text().toInt()
        if num[0] < 9:
            new = num[0] + 1
        else:
            new = num[0]
        self.scoreP1.setText(str(new))

    def decrement_P1(self):
        num = self.scoreP1.text().toInt()
        if num[0] > 0:
            new = num[0] - 1
        else:
            new = num[0]
        self.scoreP1.setText(str(new))

    def increment_P2(self):
        num = self.scoreP2.text().toInt()
        if num[0] < 9:
            new = num[0] + 1
        else:
            new = num[0]
        self.scoreP2.setText(str(new))

    def decrement_P2(self):
        num = self.scoreP2.text().toInt()
        if num[0] > 0:
            new = num[0] - 1
        else:
            new = num[0]
        self.scoreP2.setText(str(new))
            
    def swap(self):
        p1 = self.textboxP1.text()
        p2 = self.textboxP2.text()
        self.textboxP1.setText(p2)
        self.textboxP2.setText(p1)

    def reset(self):
        self.textboxP1.setText("")
        self.textboxP2.setText("")
        self.scoreP1.setText("0")
        self.scoreP2.setText("0")

    def save(self):
        with open("info/player1.txt", "w") as text_file:
            text_file.write("%s" % self.textboxP1.text())

        with open("info/player2.txt", "w") as text_file:
            text_file.write("%s" % self.textboxP2.text())

        with open("info/pscore.txt", "w") as text_file:
            text_file.write("%s" % self.scoreP1.text())

        with open("info/p2score.txt", "w") as text_file:
            text_file.write("%s" % self.scoreP2.text())

        with open("info/match.txt", "w") as text_file:
            text_file.write("%s" % self.textboxA.text())

        with open("info/names.txt", "w") as text_file:
            text_file.write("%s" % self.textboxB.text())

        htmlDoc = open('part1.html',"r+")
        soup = BeautifulSoup(htmlDoc, "html.parser")
        soup.find("span", {"id": "matchinfo1"}).string = str("%s" % self.textboxC.text())
        soup.find("span", {"id": "matchinfo2"}).string = str("%s" % self.textboxE.text())
        soup.find("span", {"id": "eventinfo1"}).string = str("%s" % self.textboxD.text())
        soup.find("span", {"id": "eventinfo2"}).string = str("%s" % self.textboxF.text())
		
        htmlDoc.close()
	
        html = soup.prettify("utf-8")
        with open("part1.html", "w") as file:
            file.write(html)

    def display_info(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Zhiyuan Liu, 2016. MyScoreboard.")
        msgBox.exec_()
        
    def close_application(self):
        sys.exit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()
    sys.exit()

main()
