//UART.H
#ifndef UART_INCLUDE
#define UART_INCLUDE
#include "types.h"

void UART_Init() {

  TMOD |= 0x20; //��ʱ��1����ģʽ2���Զ���װ8λ������
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


/*�첽ͨ���ж�*/
void UART() interrupt 4 {
  if(RI == 1) {
	int i = 0;//������
	num = SBUF;  //ȡ������
	if (num == '[') {
	  while (num != ']') {
	    Received_Buf[i] = num;
	    RI = 0;
	    delay(1);
	    num = SBUF;
	    i++;    
	  }
	  Received_Buf[i] = ']';
	  Received_Buf[i+1] = '\0'; 
	  RI = 0;
	  //JUDGE FANS STAGE
	  if (Received_Buf[5] == '0') FAN_FLAG = 0;
	  else if (Received_Buf[5] == '1') FAN_FLAG = 1;
	  else if (Received_Buf[5] == '2') FAN_FLAG = 2;
	  else if (Received_Buf[5] == '3') FAN_FLAG = 3;
	  else FAN_FLAG = 0;
	  //JUDGE TIME
	  if (Received_Buf[1] >= '6') TIME_FLAG = 0;
	  else TIME_FLAG = 1;
	  if (TIME_FLAG) {
	    TIME_MIN = (Received_Buf[1] - 0x30) * 10 + (Received_Buf[2]-0x30);
	    TIME_SEC = (Received_Buf[3] - 0x30) * 10 + (Received_Buf[4]-0x30);
	  } 
	  //UART_send_string(Received_Buf);
	  for (i=19;i>0;i--)
	    Received_Buf[i] = 0;
	}
	else { RI = 0; }  	
  }
  //���������ϣ������־λ
  if(TI == 1) {	TI = 0; }
}

void test() {
  ES = 0;
  Send_Buf[0] = '[';
  Send_Buf[1] = (TIME_MIN / 10) + 0x30;
  Send_Buf[2] = (TIME_MIN % 10) + 0x30;
  Send_Buf[3] = (TIME_SEC / 10) + 0x30;
  Send_Buf[4] = (TIME_SEC % 10) + 0x30;
  Send_Buf[5] = FAN_FLAG + 0x30;
  Send_Buf[6] = ']';
  Send_Buf[7] = '\0';
  UART_send_string(Send_Buf);
  ES = 1;
}


#endif