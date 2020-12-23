//SmartFan
//HRex 2020/12/23
#include <reg52.h>
#include "fan.h"

uint8 Buf[]="hello world!\n";
uint8 Received_Buf[50] = '0';
uint16 num = 0;
//Flags
int FAN_FLAG = 0;
int TIME_FLAG = 0;
int TIME_MIN = 0;
int TIME_SEC = 0;
//LED
sbit LED_DIN = P1^5;
sbit LED_CS = P1^6;
sbit LED_CLK = P1^7;
//KeyBoard
sbit K1 = P3^2;
sbit K2 = P3^3;
sbit K3 = P3^6;
sbit K4 = P3^7;


void UART_Init() {
  TMOD = 0x20;
  TMOD = 0x20; //定时器0工作模式2，自动重装8位计数器
  TH1 = 0xfd;
  TL1 = 0xfd;//定时器溢出时，会自动将高8位中的值赋值给低8位.比特率9600
  TR1 = 1;
  SM0 = 0;
  SM1 = 1;
  REN = 1;
  EA = 1;
  ES = 1;
}

/*发送一个字符*/
void UART_send_byte(uint8 dat) {
  SBUF = dat;       	//把数据放到SBUF中
  while (TI == 0);		//未发送完毕就等待
  TI = 0;    			//发送完毕后，要把TI重新置0
}
 
/*发送一个字符串*/
void UART_send_string(uint8 *buf) {
  while (*buf != '\0') {
    UART_send_byte(*buf++);
  }
}

/*异步通信中断*/
void UART() interrupt 4 {
  if(RI == 1) {
	int i = 0;//计数器
	num = SBUF;  //取出数据
	while (num != '!') {
	  Received_Buf[i] = num;
	  RI = 0;
	  delay(1);
	  num = SBUF;
	  i++;    
	}
	Received_Buf[i] = '!';
	Received_Buf[i+1] = '\0'; 
	RI = 0;
	//JUDGE FANS STAGE
	if (Received_Buf[4] == '0') FAN_FLAG = 0;
	else if (Received_Buf[4] == '1') FAN_FLAG = 1;
	else if (Received_Buf[4] == '2') FAN_FLAG = 2;
	else if (Received_Buf[4] == '3') FAN_FLAG = 3;
	else FAN_FLAG = 0;
	//JUDGE TIME
	if (Received_Buf[0] > '6') TIME_FLAG = 0;
	else TIME_FLAG = 1;
	if (TIME_FLAG) {
	  TIME_MIN = (Received_Buf[0] - 0x30) * 10 + Received_Buf[1];
	  TIME_SEC = (Received_Buf[2] - 0x30) * 10 + Received_Buf[3];
	} 
	UART_send_string(Received_Buf);
	for (i=49;i>0;i--)
	  Received_Buf[i] = 0;
  }
  //如果发送完毕，清除标志位
  if(TI == 1) {							   
    TI = 0;       
  }
}
//K1:STOP K2:调整
void key_select() {
  if (K1 == 0) {
    delay(10);
	if (K1 == 0) { FAN_FLAG = 0; }
  }
  else if (K2 == 0) {
  	delay(10);
	if (K2 == 0) {
	  FAN_FLAG ++;
	  FAN_FLAG = FAN_FLAG % 4;
	  if (FAN_FLAG == 0) { FAN_FLAG ++; }
	}
  }
  else if (K3 == 0) {
    delay(10);
  }

}

void main() {
	
  UART_Init();
  while (1) {
    key_select();
    switch(FAN_FLAG) {
	  case 0: fan_stop();break;
	  case 1: fan_low();break;
	  case 2: fan_mid();break;
	  case 3: fan_high();break;
	  default:fan_stop();break;
	}// switch


  }// while
}// main

