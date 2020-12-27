# micro_controller_SmartFan
## 单片机控制智能风扇  
上位机采用PyQt开发  
  
下位机采用Keil开发
  
上下位机之间通过串口进行数传 
## 关于串口通讯
采用特定的数据协议进行解析：  
```
[MMSSX]
```
MM指设定的时钟数，SS指设定的秒钟数，X指风扇的档位，  
"[" 是数据传输的起始位，"]" 是数据传输的停止位。  
  
## micro_controller_serial
### Requirements
Python3    
PyQt    
PyQt-tools  
    
#### Windows    
```
pip install PyQt5
pip install PyQt5-tools
cd ~/micro_controller_SmartFan/micro_controller_serial
python3 main.py
```
#### Linux
```
sudo apt-get install python3-pyqt5
sudo apt-get install qt5-default qttools5-dev-tools
cd ~/micro_controller_SmartFan/micro_controller_serial
python3 main.py
```
## micro_controller_c51
代码结构：  
```
|__ main.c
    |__ fan.h
    |__ key.h
    |__ led.h
    |__ timer.h
    |__ uart.h
    |__ types.h
```
## Environmrnt
```
Keil 4 IDE
STC-ICP 烧录程序
CH340 Driver 驱动
```
### About Keil in Linux
https://blog.csdn.net/best_xiaolong/article/details/88801656
