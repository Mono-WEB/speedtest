from PyQt5 import QtCore, QtGui, QtWidgets
import speedtest

s = speedtest.Speedtest()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 200)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dwn_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dwn_btn.setGeometry(QtCore.QRect(80, 110, 89, 25))
        self.dwn_btn.setStyleSheet("color: rgb(46, 194, 126);")
        self.dwn_btn.setObjectName("dwn_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(46, 194, 126)")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.get_speed()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpeedTest"))
        self.dwn_btn.setText(_translate("MainWindow", "Запустити"))
        self.label.setText(_translate("MainWindow", "Швидкість:"))
        self.label_2.setText(_translate("MainWindow", "0"))

    def get_speed(self):
        self.dwn_btn.clicked.connect(self.upload_speed)

    def upload_speed(self):
        result = str(s.download()).split(".")

        mega_b = int(result[0]) / 1000000
        kilo_b = int(result[1][:2])

        if mega_b >= 1:
            d_speed = str(mega_b).split(".")[0] + "." + str(kilo_b) + " mb/sec"
            self.label_2.setText(str(d_speed))
        else:
            d_speed = "0." + str(mega_b).split(".")[1][:2] + " mb/sec"
            self.label_2.setText(str(d_speed))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())