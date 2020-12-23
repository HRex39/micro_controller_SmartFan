//Fan.h
//Control Fan
//Created by HRex on 2020/12/23
#ifndef FAN_INCLUDED
#define FAN_INCLUDED
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

void delay(uint16 n) {
  uint16 x,y;
  for (x=n;x>0;x--)
  	for (y=114;y>0;y--);
}

void fan_stop() {
  L1 = 0;
  L2 = 0;
  L3 = 0;
  L4 = 0;
  IN3 = 0;
  IN4 = 0;
  delay(100);
}

void fan_low() {
  L1 = 0;
  IN3 = 1;IN4 = 0;
  delay(30);
  IN3 = 0;IN4 = 0;
  delay(70);
}

void fan_mid() {
  L1 = 0;
  L2 = 0;
  IN3 = 1;IN4 = 0;
  delay(50);
  IN3 = 0;IN4 = 0;
  delay(50);
}

void fan_high() {
  L1 = 0;
  L2 = 0;
  L3 = 0;
  IN3 = 1;IN4 = 0;
  delay(90);
  IN3 = 0;IN4 = 0;
  delay(10);
}


#endif // FAN_INCLUDED
