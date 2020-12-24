//Fan.h
//Control Fan
//Created by HRex on 2020/12/23
#ifndef FAN_INCLUDED
#define FAN_INCLUDED
#include "types.h"

void delay(uint16 n) {
  uint16 x,y;
  for (x=n;x>0;x--)
  	for (y=114;y>0;y--);
}

void fan_stop() {
  P1 = 0x07;
  IN3 = 0;
  IN4 = 0;
  delay(100);
}

void fan_low() {
  P1 = 0x0E;
  IN3 = 1;IN4 = 0;
  delay(38);
  IN3 = 0;IN4 = 0;
  delay(70);
}

void fan_mid() {
  P1 = 0x0C;
  IN3 = 1;IN4 = 0;
  delay(50);
  IN3 = 0;IN4 = 0;
  delay(50);
}

void fan_high() {
  P1 = 0x08;
  IN3 = 1;IN4 = 0;
  delay(90);
  IN3 = 0;IN4 = 0;
  delay(10);
}


#endif // FAN_INCLUDED
