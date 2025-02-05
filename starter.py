from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartWin(object):
    def setupUi(self, StartWin):
        StartWin.setObjectName("StartWin")
        StartWin.resize(725, 473)
        self.next = QtWidgets.QPushButton(StartWin)
        self.next.setGeometry(QtCore.QRect(180, 380, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.label = QtWidgets.QLabel(StartWin)
        self.label.setGeometry(QtCore.QRect(80, 120, 601, 181))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(StartWin)
        QtCore.QMetaObject.connectSlotsByName(StartWin)

    def retranslateUi(self, StartWin):
        _translate = QtCore.QCoreApplication.translate
        StartWin.setWindowTitle(_translate("StartWin", "Dialog"))
        self.next.setText(_translate("StartWin", "Дальше"))
        self.label.setText(_translate("StartWin", "Суть игры заключаеться в том чтобы\n"
" за 5 попыток угадать одно случайное\n"
" число из 12 доступных если ты не\n"
" угадал за 5 попыток то программа закрываеться"))
