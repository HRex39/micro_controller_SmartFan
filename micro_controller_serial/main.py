# -*- coding: utf-8 -*-
# Created by HRex on 2020/12/22

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import serial

import SmartFan

# Global Variable
portx = 0   #端口号
bps = 0     #波特率
num_data = 0    #数据位
num_stop = 0    #停止位
num_parity_check = 0    #校验位
timex = 0.1   #超时设置
# Variable ends


def prog_exit(self):
    self.close()

def data_send():
    try:
        # DATA PROCEED
        portx = ui.comboBox_2.currentText()
        bps = ui.comboBox.currentText()
        num_data = ui.comboBox_4.currentText()
        if num_data == "5": num_data = serial.FIVEBITS
        if num_data == "6": num_data = serial.SIXBITS
        if num_data == "7": num_data = serial.SEVENBITS
        if num_data == "8": num_data = serial.EIGHTBITS
        num_stop = ui.comboBox_3.currentText()
        if num_stop == "1": num_stop = serial.STOPBITS_ONE
        if num_stop == "1.5": num_stop = serial.STOPBITS_ONE_POINT_FIVE
        if num_stop == "2": num_stop = serial.STOPBITS_TWO
        num_parity_check = ui.comboBox_5.currentText()
        if num_parity_check == "无校验": num_parity_check = serial.PARITY_NONE
        if num_parity_check == "奇校验": num_parity_check = serial.PARITY_ODD
        if num_parity_check == "偶校验": num_parity_check = serial.PARITY_EVEN

        print(portx,bps,num_data,num_stop,num_parity_check)
        # OPEN SERIES
        ser = serial.Serial(port=portx, baudrate=bps, bytesize=num_data,
                            parity=num_parity_check, stopbits=num_stop,timeout=timex)
        # WRITE
        result = ser.write("SENDING...".encode("utf-8"))
        print("写总字节数:", result)
        ser.close()  # CLOSE SERIAL
        ui.label_9.setText("连接成功！")
    except Exception as e:
        ui.label_9.setText("ERROR")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = SmartFan.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #Set default num
    ui.comboBox.setCurrentIndex(3)
    ui.comboBox_3.setCurrentIndex(0)
    ui.comboBox_4.setCurrentIndex(3)
    ui.comboBox_5.setCurrentIndex(0)
    #Link to the menu function
    ui.actionExit.triggered.connect(prog_exit)
    ui.actionOpen.triggered.connect(data_send)
    #Link to the button function
    ui.pushButton.clicked.connect(data_send)
    sys.exit(app.exec_())

