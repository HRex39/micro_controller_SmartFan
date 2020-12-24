//SmartFan
//HRex 2020/12/23
#include <reg52.h>
#include "types.h"
#include "fan.h"
#include "led.h"
#include "key.h"
#include "timer.h"
#include "uart.h"

void main() {		
  UART_Init();
  LED_Init();
  TIMER0_Init();
  while (1) {
    key_select();
    switch(FAN_FLAG) {
	  case 0: fan_stop();break;
	  case 1: fan_low();break;
	  case 2: fan_mid();break;
	  case 3: fan_high();break;
	  default:fan_stop();break;
	}// switch
	led_out();
	TIMER0_Overflow();
  }// while
}// main

