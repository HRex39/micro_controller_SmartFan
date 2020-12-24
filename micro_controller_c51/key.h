//KEY.H
#ifndef KEY_INCLUDED
#define KEY_INCLUDED
#include "types.h"
#include "timer.h"

//K1:STOP K2:µ÷Õû
void key_select() {
  if (K1 == 0) {
    delay(5);
	if (K1 == 0) { FAN_FLAG = 0; }
	while (!K1);
  }
  else if (K2 == 0) {
  	delay(10);
	if (K2 == 0) {
	  FAN_FLAG ++;
	  FAN_FLAG = FAN_FLAG % 4;
	  if (FAN_FLAG == 0) { FAN_FLAG ++; }
	}
	while (!K2);
  }
  else if (K3 == 0) {
    delay(20);
	if (K3 == 0) {
	  L4 = SET_COUNT;
	
	}
  }
}



#endif // KEY_INCLUDE