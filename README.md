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
    
#### Windows(Linux)    
```
(sudo)pip install PyQt5
(sudo)pip install PyQt5-tools
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
本人开发用电脑配置：ThinkPad-T480, i5-8250U, Windows10, 16G DDR4 2400, 256G + 1T  
//Qt跨平台，Linux也可以用Wine来解决，故实际应该都可以运行
