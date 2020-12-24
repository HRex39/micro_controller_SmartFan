//LED.H
#ifndef LED_INCLUDED
#define LED_INCLUDED

#include "types.h"

//�Ĵ����궨��
 
#define DECODE_MODE  0x09   //������ƼĴ���
 
#define INTENSITY    0x0A   //���ȿ��ƼĴ���
 
#define SCAN_LIMIT   0x0B   //ɨ����޼Ĵ���
 
#define SHUT_DOWN    0x0C   //�ض�ģʽ�Ĵ���
 
#define DISPLAY_TEST 0x0F   //���Կ��ƼĴ���        
 
//��������
 
void Write7219(unsigned char address,unsigned char dat);
 
void Initial(void);
 
//��ַ�����ݷ����ӳ���
 
void Write7219(unsigned char address,unsigned char dat)
 
{  
 
    unsigned char i;
 
    LOAD=0;    //����Ƭѡ�ߣ�ѡ������
 
    //���͵�ַ
 
    for (i=0;i<8;i++)        //��λѭ��8��             
 
    {  
 
       CLK=0;        //����ʱ������
 
       DIN=(bit)(address&0x80); //ÿ��ȡ���ֽ�     
 
       address<<=1;             //����һλ
 
       CLK=1;        //ʱ�������أ����͵�ַ
 
    }
 
    //��������
 
    for (i=0;i<8;i++)              
 
    {  
 
       CLK=0;
 
       DIN=(bit)(dat&0x80);    
 
       dat<<=1; 
 
       CLK=1;        //ʱ�������أ���������
 
    }
 
    LOAD=1;    //���ͽ�������������������                      
 
}
 
//MAX7219��ʼ��������MAX7219�ڲ��Ŀ��ƼĴ���
 
void LED_Init(void)                
 
{
	
	int i = 0;
	 
    Write7219(SHUT_DOWN,0x01);         //������������ģʽ��0xX1��
 
    Write7219(DISPLAY_TEST,0x00);      //ѡ����ģʽ��0xX0��
 
    Write7219(DECODE_MODE,0xff);       //ѡ��ȫ����ģʽ
 
    Write7219(SCAN_LIMIT,0x07);        //8ֻLEDȫ��
 
    Write7219(INTENSITY,0x04);          //���ó�ʼ����
	
    for (i = 1; i < 9; i++)

	{

        Write7219(i,9);
		  
    }
	     
}

void led_out() {
  Write7219(1,TIME_SEC % 10);
  Write7219(2,TIME_SEC / 10);
  Write7219(3,TIME_MIN % 10 + 128);
  Write7219(4,TIME_MIN / 10);
  Write7219(5,15);
  Write7219(6,15);
  Write7219(7,15);
  Write7219(8,FAN_FLAG);
}
#endif // LED_INCLUDED