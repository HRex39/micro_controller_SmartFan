//TYPES.H
#ifndef TYPES_INCLUDED
#define TYPES_INCLUDED

typedef unsigned char uint8;
typedef unsigned int uint16;
uint8 Buf[]="hello world!\n";
uint8 Received_Buf[50] = '0';
uint16 num = 0;

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
sbit DIN   = P2^5;
sbit LOAD  = P2^6;
sbit CLK   = P2^7;
//KeyBoard
sbit K1 = P3^2;
sbit K2 = P3^3;
sbit K3 = P3^6;
sbit K4 = P3^7;
//Time Count
int TIME_COUNT = 0;
bit SET_COUNT = 0;


#endif // TYPES_INCLUDED