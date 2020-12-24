# -*- coding: utf-8 -*-
# Created by HRex on 2020/12/22
import re
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
SERIAL_STATUS = 0
# Variable ends

# Status Variable
control_stage = 0
time_stage = "9999"
min_stage = "00"
sec_stage = "00"
fan_stage = 0
# Variable ends

def high_speed_set():
    global control_stage
    control_stage = 3
def mid_speed_set():
    global control_stage
    control_stage = 2
def low_speed_set():
    global control_stage
    control_stage = 1
def stop_speed_set():
    global control_stage
    control_stage = 0
def stop_time_set():
    global time_stage
    time = ui.timeEdit.time().toString()
    time_stage = str(time[3]+time[4]+time[6]+time[7])
def data_from_c51_set(data):
    global min_stage,sec_stage,fan_stage
    find_data = re.findall('(?<=!).*?(?=!)',data)
    current_stage = int(find_data[-1])
    if int(current_stage / 100) <= 60:
        fan_stage = int(current_stage % 10)
        current_stage = int(current_stage / 10)
        min_stage = int(current_stage / 100)
        sec_stage = int(current_stage % 100)
    else:
        fan_stage = int(current_stage % 10)
        min_stage = 0
        sec_stage = 0

    if fan_stage == 0:
        ui.label_13.setText("STOP")
    elif fan_stage == 1:
        ui.label_13.setText("LOW")
    elif fan_stage == 2:
        ui.label_13.setText("MID")
    elif fan_stage == 3:
        ui.label_13.setText("HIGH")

def prog_exit(self):
    app = QApplication(sys.argv)
    app.quit()

def data_clear():
    ui.textBrowser.clear()

def data_send():
    global ser, SERIAL_STATUS
    if SERIAL_STATUS == 1:
        try:
            SCS = time_stage + str(control_stage) + "!"
            print(SCS)
            ui.label_12.setText(SCS)
            # WRITE
            result = ser.write(SCS.encode("utf-8"))
            print("写总字节数:", result)
            ui.label_11.setText("连接成功！")
        except Exception as e:
            ui.label_11.setText("SEND_ERROR!")
    else:
        ui.label_11.setText("串口未开启，发送失败！")

def data_received(thread_name):
    global ser, SERIAL_STATUS
    while True:
        if SERIAL_STATUS == 1:
            ui.label_10.setText("串口已开启，准备接收")
            try:
                if ser.in_waiting:
                    data_from_c51 = ser.read(ser.in_waiting).decode("utf-8")
                    sleep(0.02)
                    print(data_from_c51)
                    data_from_c51_set(data_from_c51)
                    ui.textBrowser.insertPlainText(data_from_c51)
            except Exception as e:
                ui.label_10.setText("ERROR!!!!")
            data_from_c51 = None
        else:
            ui.label_10.setText("串口未开启，接收失败")
        ui.lcdNumber_3.display(str(min_stage) + ":" + str(sec_stage))

def serial_open():
    global ser, SERIAL_STATUS
    if SERIAL_STATUS == 0:
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

            print(portx, bps, num_data, num_stop, num_parity_check)

            # OPEN SERIES
            ser = serial.Serial(port=portx, baudrate=bps, bytesize=num_data,
                                parity=num_parity_check, stopbits=num_stop, timeout=timex)
            ui.label_9.setText("已连接上"+portx)
            SERIAL_STATUS = 1
        except serial.SerialException:
            ui.label_9.setText("连接"+portx+"失败")
            SERIAL_STATUS = 0
        ui.pushButton.setText("关闭串口")
    else:
        try:
            ser.close()
            ui.label_9.setText("关闭成功")
            ui.pushButton.setText("打开串口")
            SERIAL_STATUS = 0
        except Exception as e:
            ui.label_9.setText("关闭失败")
            SERIAL_STATUS = 1




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
    ui.lcdNumber_3.setDigitCount(5)
    # Set Maxium Time
    ui.timeEdit.setDisplayFormat("mm:ss")
    ui.timeEdit.setMinimumTime(QTime(00,00,15))
    ui.timeEdit.setMaximumTime(QTime(00,59,59))
    # Link to the menu function
    ui.actionExit.triggered.connect(prog_exit)
    ui.actionOpen.triggered.connect(high_speed_set)
    # Link to the button function
    ui.pushButton.clicked.connect(serial_open)      #Open Serial
    ui.pushButton_2.clicked.connect(high_speed_set)  #High Speed
    ui.pushButton_3.clicked.connect(mid_speed_set)   #Mid Speed
    ui.pushButton_4.clicked.connect(low_speed_set)   #Low Speed
    ui.pushButton_5.clicked.connect(stop_speed_set)  #Stop
    ui.pushButton_6.clicked.connect(stop_time_set)
    ui.pushButton_7.clicked.connect(data_send)
    ui.pushButton_8.clicked.connect(data_clear)
    sys.exit(app.exec_())

