//LED.H
#ifndef LED_INCLUDED
#define LED_INCLUDED

#include "types.h"

//寄存器宏定义
 
#define DECODE_MODE  0x09   //译码控制寄存器
 
#define INTENSITY    0x0A   //亮度控制寄存器
 
#define SCAN_LIMIT   0x0B   //扫描界限寄存器
 
#define SHUT_DOWN    0x0C   //关断模式寄存器
 
#define DISPLAY_TEST 0x0F   //测试控制寄存器        
 
//函数声明
 
void Write7219(unsigned char address,unsigned char dat);
 
void Initial(void);
 
//地址、数据发送子程序
 
void Write7219(unsigned char address,unsigned char dat)
 
{  
 
    unsigned char i;
 
    LOAD=0;    //拉低片选线，选中器件
 
    //发送地址
 
    for (i=0;i<8;i++)        //移位循环8次             
 
    {  
 
       CLK=0;        //清零时钟总线
 
       DIN=(bit)(address&0x80); //每次取高字节     
 
       address<<=1;             //左移一位
 
       CLK=1;        //时钟上升沿，发送地址
 
    }
 
    //发送数据
 
    for (i=0;i<8;i++)              
 
    {  
 
       CLK=0;
 
       DIN=(bit)(dat&0x80);    
 
       dat<<=1; 
 
       CLK=1;        //时钟上升沿，发送数据
 
    }
 
    LOAD=1;    //发送结束，上升沿锁存数据                      
 
}
 
//MAX7219初始化，设置MAX7219内部的控制寄存器
 
void LED_Init(void)                
 
{
	
	int i = 0;
	 
    Write7219(SHUT_DOWN,0x01);         //开启正常工作模式（0xX1）
 
    Write7219(DISPLAY_TEST,0x00);      //选择工作模式（0xX0）
 
    Write7219(DECODE_MODE,0xff);       //选用全译码模式
 
    Write7219(SCAN_LIMIT,0x07);        //8只LED全用
 
    Write7219(INTENSITY,0x04);          //设置初始亮度
	
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