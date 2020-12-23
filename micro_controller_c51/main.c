//SmartFan
//HRex 2020/12/23
#include <reg52.h>
#include "fan.h"

uint8 Buf[]="hello world!\n";
uint8 Received_Buf[50] = '0';
uint16 num = 0;
//Flags
FAN_FLAG = 0;

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
  TMOD = 0x20; //��ʱ��0����ģʽ2���Զ���װ8λ������
  TH1 = 0xfd;
  TL1 = 0xfd;//��ʱ�����ʱ�����Զ�����8λ�е�ֵ��ֵ����8λ.������9600
  TR1 = 1;
  SM0 = 0;
  SM1 = 1;
  REN = 1;
  EA = 1;
  ES = 1;
}

/*����һ���ַ�*/
void UART_send_byte(uint8 dat) {
  SBUF = dat;       	//�����ݷŵ�SBUF��
  while (TI == 0);		//δ������Ͼ͵ȴ�
  TI = 0;    			//������Ϻ�Ҫ��TI������0
}
 
/*����һ���ַ���*/
void UART_send_string(uint8 *buf) {
  while (*buf != '\0') {
    UART_send_byte(*buf++);
  }
}

void UART() interrupt 4 {
  if(RI == 1) {
	int i = 0;//������
	num = SBUF;  //ȡ������
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

	UART_send_string(Received_Buf);
	for (i=49;i>0;i--)
	  Received_Buf[i] = 0;
  }
  //����������
  if(TI == 1) {							   
    TI = 0;       //�����־λ
  }
}

void main() {
	
  UART_Init();
  while (1) {
    
	switch(FAN_FLAG) {
	  case 0: fan_stop();break;
	  case 1: fan_low();break;
	  case 2: fan_mid();break;
	  case 3: fan_high();break;
	  default:fan_stop();break;
	}// switch

  }	


}// main

