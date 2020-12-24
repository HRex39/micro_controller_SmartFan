# -*- coding: utf-8 -*-
# Created by HRex on 2020/12/22

import sys
import threading
from time import sleep

from PyQt5.QtCore import QTime
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
SCS = None
ser = None
# Variable ends

# Status Variable
control_stage = 0
time_stage = "9999"
# Variable ends

def high_speed_set():
    global control_stage
    control_stage = 3
    data_send()
def mid_speed_set():
    global control_stage
    control_stage = 2
    data_send()
def low_speed_set():
    global control_stage
    control_stage = 1
    data_send()
def stop_speed_set():
    global control_stage
    control_stage = 0
    data_send()
def stop_time_set():
    global time_stage
    time = ui.timeEdit.time().toString()
    time_stage = str(time[3]+time[4]+time[6]+time[7])
    data_send()

def prog_exit(self):
    app = QApplication(sys.argv)
    app.quit()

def data_send():
    global ser
    try:
        SCS = time_stage + str(control_stage) + "!"
        print(SCS)
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
        result = ser.write(SCS.encode("utf-8"))
        print("写总字节数:", result)

        # READ WHEN WRITE
        sleep(0.1)#TODO:NEED JUDGE，实在不行就定时刷新
        data = ser.read(ser.in_waiting).decode("utf-8")
        print("data="+data)
        if data != None:
            ui.label_10.setText(data)

        ser.close()  # CLOSE SERIAL
        ui.label_9.setText("连接成功！")
    except Exception as e:
        ui.label_9.setText("SEND_ERROR!")

def data_received(thread_name):
    while True:
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
            # OPEN SERIES
            ser = serial.Serial(port=portx, baudrate=bps, bytesize=num_data,
                                parity=num_parity_check, stopbits=num_stop, timeout=timex)

            # 测试用！！
            if ser.in_waiting:
                data_from_c51 = ser.read(ser.in_waiting).decode("utf-8")
                print(data_from_c51)
            ser.close()  # CLOSE SERIAL
            ui.label_10.setText(data_from_c51)
        except Exception as e:
            sleep(0.1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = SmartFan.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Thread
    Received_Thread = threading.Thread(target=data_received, args=("Received_Thread",))
    Received_Thread.start()
    # Set default num
    ui.comboBox.setCurrentIndex(3)
    ui.comboBox_3.setCurrentIndex(0)
    ui.comboBox_4.setCurrentIndex(3)
    ui.comboBox_5.setCurrentIndex(0)
    # Set Maxium Time
    ui.timeEdit.setDisplayFormat("mm:ss")
    ui.timeEdit.setMinimumTime(QTime(00,00,15))
    ui.timeEdit.setMaximumTime(QTime(00,59,59))
    # Link to the menu function
    ui.actionExit.triggered.connect(prog_exit)
    ui.actionOpen.triggered.connect(high_speed_set)
    # Link to the button function
    ui.pushButton.clicked.connect(low_speed_set)
    ui.pushButton_2.clicked.connect(high_speed_set)  #High Speed
    ui.pushButton_3.clicked.connect(mid_speed_set)   #Mid Speed
    ui.pushButton_4.clicked.connect(low_speed_set)   #Low Speed
    ui.pushButton_5.clicked.connect(stop_speed_set)  #Stop
    ui.pushButton_6.clicked.connect(stop_time_set)
    sys.exit(app.exec_())

