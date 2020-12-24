//TYPES.H
#ifndef TYPES_INCLUDED
#define TYPES_INCLUDED

typedef unsigned char uint8;
typedef unsigned int uint16;

//Fans
sbit IN3 = P2^0;
sbit IN4 = P2^1;
//Light
sbit L1 = P1^0;
sbit L2 = P1^1;
sbit L3 = P1^2;
sbit L4 = P1^3;
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


#endif // TYPES_INCLUDED