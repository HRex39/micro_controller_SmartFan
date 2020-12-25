# micro_controller_SmartFan
单片机控制智能风扇  
上位机采用PyQt开发  
下位机采用Keil开发
上下位机之间通过串口进行数传 
## 关于串口通讯
采用特定的数据协议进行解析：  
```

[MMSSX]

MM指设定的时钟数，SS指设定的秒钟数，X指风扇的档位，
"[" 是数据传输的起始位，"]" 是数据传输的停止位。

```
## micro_controller_serial

## micro_controller_c51


