//KEY.H
#ifndef KEY_INCLUDED
#define KEY_INCLUDED
#include "types.h"
#include "timer.h"

//K1:STOP K2:FAN K3:TIME
void key_select() {
  if (K1 == 0) {
    delay(5);
	if (K1 == 0) { FAN_FLAG = 0; }
	while (!K1);
  }

  else if (K2 == 0) {
  	delay(15);
	if (K2 == 0) {
	  FAN_FLAG ++;
	  FAN_FLAG = FAN_FLAG % 4;
	  if (FAN_FLAG == 0) { FAN_FLAG ++; }
	}
	while (!K2);
  }
  //K3:TIME
  else if (K3 == 0) {
    delay(200);
	if (K3 == 0) {
	  //LIGHT SHINK
	  while( !K3 ) { 
	    L1 = SET_COUNT;L2=!L1;L3=!L2;
		delay(500);
		SET_COUNT = !SET_COUNT; 
	  }
	  TIME_MIN = 0; TIME_SEC = 0;
	  //SETTING TIME
	  while (K3) {
	    led_out();//TODO:FOR TESTING
	  	L1 = SET_COUNT;L2=!L1;L3=!L2;
		delay(500);
		SET_COUNT = !SET_COUNT;
		//K1: ADD ONCE
		if (K1 == 0) {
		  delay(15);
		  if (K1 == 0) {
			TIME_SEC += 30;
			if (TIME_SEC == 60) {
			  TIME_SEC = 0;
			  TIME_MIN ++;
			  if (TIME_MIN >= 60) { TIME_MIN = 0; }
			}
		  }
		}
		//K2:SUB ONCE
		if (K2 == 0) {
		  delay(15);
		  if (K2 == 0) {
			if (TIME_MIN == 0 && TIME_SEC == 0) { 
			  TIME_SEC = 30;
			  TIME_MIN = 59;
			}
			else if (TIME_SEC == 0) {
			  TIME_SEC = 30;
			  TIME_MIN --;
			}
			else { TIME_SEC -= 30; }
		  }
		}
		//K4:CONFIRM
		if (K4 == 0) { 
		  delay(20);
		  TIME_FLAG = 1;
		  break;
		}

	  }// while K3
	}// K3Ïû¶¶
  }// K3ÅÐ¶¨
}// key select

#endif // KEY_INCLUDE