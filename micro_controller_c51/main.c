//SmartFan
//HRex 2020/12/23
#include <reg52.h>
typedef unsigned char uint8;
typedef unsigned int uint16;

uint8 Buf[]="hello world!\n";
uint8 Received_Buf[50] = '0';
uint16 num = 0;
//Flags

//Fans
sbit IN3 = P0^0;
sbit IN4 = P0^1;
sbit ENB = P0^2;
//Light
sbit L1 = P1^0;
sbit L2 = P1^1;
sbit L3 = P1^2;
sbit L4 = P1^3;
//LED
sbit LED_DIN = P1^5;
sbit LED_CS = P1^6;
sbit LED_CLK = P1^7;
//KeyBoard
sbit K1 = P3^2;
sbit K2 = P3^3;
sbit K3 = P3^6;
sbit K4 = P3^7;

void delay(uint16 n) {
  uint16 x,y;
  for (x=n;x>0;x--)
  	for (y=114;y>0;y--);
}

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
	RI = 0;
	//num = SBUF;  //ȡ������
	//RI = 0;

	UART_send_string(Received_Buf);
	for (i=49;i>0;i--)
	  Received_Buf[i] = 0;
	delay(100);
  }
  //����������
  if(TI == 1) {							   
    TI = 0;       //�����־λ
  }
}

void main() {
	
  UART_Init();
  while (1) {
    L1 = 0;
  
  
  }	


}

