from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from game import Ui_MainWindow
from  starter import Ui_StartWin
from random import choice

app = QtWidgets.QApplication(sys.argv)

StartWindow = QtWidgets.QMainWindow()
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
start = Ui_StartWin()
start.setupUi(StartWindow)
ui.setupUi(MainWindow)
StartWindow.show()
group_btn = None
win_btn = None
counter = 5
def one():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.one_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.one_bt.hide()
def  two():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.two_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.two_bt.hide()
def three():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.three_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.three_bt.hide()
def four():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.four_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.four_bt.hide()

def five():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.five_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.five_bt.hide()
def six():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.six_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.six_bt.hide()

def seven():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.seven_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.seven_bt.hide()

def eight():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.eight_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.eight_bt.hide()
def nine():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.nine_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.nine_bt.hide()
def ten():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.ten_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.ten_bt.hide()
def eleven():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.eleven_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.label_2.setText('Программа закрываеться')
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.eleven_bt.hide()
def twelve():
    global group_btn 
    global win_btn 
    global counter
    
    if  counter <= 1:
        ui.reesult_text.setText('ПОРАЖЕНИЕ')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setText('Программа закрываеться')
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
    if win_btn == ui.twelve_bt:
        ui.reesult_text.setText('ПОБЕДА')
        ui.one_bt.hide()
        ui.two_bt.hide()
        ui.three_bt.hide()
        ui.four_bt.hide()
        ui.five_bt.hide()
        ui.six_bt.hide()
        ui.seven_bt.hide()
        ui.eight_bt.hide()
        ui.nine_bt.hide()
        ui.ten_bt.hide()
        ui.eleven_bt.hide()
        ui.twelve_bt.hide()
        ui.label_2.setText('Программа закрываеться')
        ui.label_2.setGeometry(QtCore.QRect(200, 10, 691, 41))
        ui.count.hide()
        QtCore.QTimer.singleShot(6000, lambda: sys.exit())
        
    counter -= 1
    ui.count.setText(str(counter))
    ui.twelve_bt.hide()
def click_next():
    global group_btn
    global win_btn
    global counter
    ui.setupUi(MainWindow)
    StartWindow.close()
    MainWindow.show()
    ui.count.setText(str(counter))
    group_btn = [ui.one_bt,ui.two_bt,ui.three_bt,ui.four_bt,ui.five_bt,ui.six_bt,ui.seven_bt,ui.eight_bt,ui.nine_bt,ui.ten_bt,ui.eleven_bt,ui.twelve_bt]
    win_btn =  choice(group_btn)
    
    ui.one_bt.clicked.connect(one)
    ui.two_bt.clicked.connect(two)
    ui.three_bt.clicked.connect(three)
    ui.four_bt.clicked.connect(four)
    ui.five_bt.clicked.connect(five)
    ui.six_bt.clicked.connect(six)
    ui.seven_bt.clicked.connect(seven)
    ui.eight_bt.clicked.connect(eight)
    ui.nine_bt.clicked.connect(nine)
    ui.ten_bt.clicked.connect(ten)
    ui.eleven_bt.clicked.connect(eleven)
    ui.twelve_bt.clicked.connect(twelve)


start.next.clicked.connect(click_next)


sys.exit(app.exec_())