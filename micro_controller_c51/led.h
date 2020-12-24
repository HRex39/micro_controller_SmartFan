//LED.H
#ifndef LED_INCLUDED
#define LED_INCLUDED
#include "types.h"

uint16 tcount;
uint8 m;
uint8 second,minute,hour;
//unsigned char code = 我定义的数据要放在ROM（程序存储区）里面，写入后就不能再更改
unsigned char code fseg[]={0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90};
unsigned char code segbit[]={0x80,0x40,0x20,0x10,0x08,0x04,0x02,0x01};







#endif // LED_INCLUDED