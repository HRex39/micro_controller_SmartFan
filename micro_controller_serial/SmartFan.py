# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmartFan.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(584, 580)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 191, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 70, 191, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 130, 191, 31))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_5, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 10, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 80, 101, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 150, 101, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 220, 101, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(310, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(20)
        font.setItalic(False)
        self.timeEdit.setFont(font)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setObjectName("timeEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 20, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(250, 90, 161, 71))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 340, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 200, 181, 61))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 160, 191, 73))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 260, 101, 51))
        self.label_10.setObjectName("label_10")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "智能风扇"))
        self.pushButton.setText(_translate("mainWindow", "发送"))
        self.label.setText(_translate("mainWindow", "波特率："))
        self.comboBox.setItemText(0, _translate("mainWindow", "1200"))
        self.comboBox.setItemText(1, _translate("mainWindow", "2400"))
        self.comboBox.setItemText(2, _translate("mainWindow", "4800"))
        self.comboBox.setItemText(3, _translate("mainWindow", "9600"))
        self.comboBox.setItemText(4, _translate("mainWindow", "14400"))
        self.comboBox.setItemText(5, _translate("mainWindow", "19200"))
        self.comboBox.setItemText(6, _translate("mainWindow", "38400"))
        self.comboBox.setItemText(7, _translate("mainWindow", "57600"))
        self.comboBox.setItemText(8, _translate("mainWindow", "115200"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "COM1"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "COM2"))
        self.comboBox_2.setItemText(2, _translate("mainWindow", "COM3"))
        self.comboBox_2.setItemText(3, _translate("mainWindow", "COM4"))
        self.comboBox_2.setItemText(4, _translate("mainWindow", "COM5"))
        self.comboBox_2.setItemText(5, _translate("mainWindow", "COM6"))
        self.comboBox_2.setItemText(6, _translate("mainWindow", "COM7"))
        self.comboBox_2.setItemText(7, _translate("mainWindow", "COM8"))
        self.label_2.setText(_translate("mainWindow", "串口号："))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "1.5"))
        self.comboBox_3.setItemText(2, _translate("mainWindow", "2"))
        self.label_3.setText(_translate("mainWindow", "停止位："))
        self.comboBox_4.setItemText(0, _translate("mainWindow", "5"))
        self.comboBox_4.setItemText(1, _translate("mainWindow", "6"))
        self.comboBox_4.setItemText(2, _translate("mainWindow", "7"))
        self.comboBox_4.setItemText(3, _translate("mainWindow", "8"))
        self.label_4.setText(_translate("mainWindow", "数据位："))
        self.comboBox_5.setItemText(0, _translate("mainWindow", "无校验"))
        self.comboBox_5.setItemText(1, _translate("mainWindow", "奇校验"))
        self.comboBox_5.setItemText(2, _translate("mainWindow", "偶校验"))
        self.label_5.setText(_translate("mainWindow", "校验位："))
        self.pushButton_2.setText(_translate("mainWindow", "高速运行"))
        self.pushButton_3.setText(_translate("mainWindow", "中速运行"))
        self.pushButton_4.setText(_translate("mainWindow", "低速运行"))
        self.pushButton_5.setText(_translate("mainWindow", "停止运行"))
        self.label_7.setText(_translate("mainWindow", "Time"))
        self.pushButton_6.setText(_translate("mainWindow", "定时设置"))
        self.label_6.setText(_translate("mainWindow", "Created by: HRex on 2020/12/22"))
        self.label_8.setText(_translate("mainWindow", "连接状态："))
        self.label_9.setText(_translate("mainWindow", "未连接"))
        self.label_10.setText(_translate("mainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))