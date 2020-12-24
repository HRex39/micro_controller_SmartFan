//TIMER.H
#ifndef TIMER_INCLUDED
#define TIMER_INCLUDED
#include "types.h"
#include "uart.h"

void TIMER0_Init() {
  TMOD |= 0x01;		//为什么用或 因为可以对定时器单独操作
  TH0 = 0;
  TL0 = 0;
  TR0 = 1;
}

void TIMER0_Overflow(){
  if (TF0 == 1) {
    TF0 = 0;
	TIME_COUNT ++;
	if (TIME_COUNT == 14) {	 //71ms*14 = 1s
      
	  TIME_COUNT = 0;
	  if (TIME_FLAG) {
	    if ( TIME_MIN == 0 && TIME_SEC == 0) { FAN_FLAG = 0; TIME_FLAG = 0; }
	    else if ( TIME_MIN == 0 && TIME_SEC > 0) { TIME_SEC --; }
	    else if ( TIME_MIN > 0 && TIME_SEC == 0) { TIME_SEC = 59; TIME_MIN --; }
	    else if ( TIME_MIN > 0 && TIME_SEC > 0) { TIME_SEC --; }
	  }
	  //UART_send_string(Buf);
    }
  }
}

#endif 