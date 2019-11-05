#include <pt.h>   // include protothread library

#define LEFT_PIN 11  // LEDPIN is a constant 
#define RIGHT_PIN 12 

static struct pt pt1, pt2; // each protothread needs one of these

void setup() {
  pinMode(LEFT_PIN , OUTPUT); // LED init
  pinMode(RIGHT_PIN, OUTPUT);
  PT_INIT(&pt1);  // initialise the two
  PT_INIT(&pt2);  // protothread variables
}

void toggleLED(int pin) {
  boolean ledstate = digitalRead(pin); // get LED state
  ledstate ^= 1;   // toggle LED state using xor
  digitalWrite(pin, ledstate); // write inversed state back
}

/* This function toggles the LED after 'interval' ms passed */
static int protothread1(struct pt *pt, int interval, int pin) {
  static unsigned long timestamp = 0;
  PT_BEGIN(pt);
  while(1) { // never stop 
    /* each time the function is called the second boolean
    *  argument "millis() - timestamp > interval" is re-evaluated
    *  and if false the function exits after that. */
    PT_WAIT_UNTIL(pt, millis() - timestamp > interval );
    timestamp = millis(); // take a new timestamp
    toggleLED(pin);
  }
  PT_END(pt);
}
/* exactly the same as the protothread1 function */
static int protothread2(struct pt *pt, int interval, int pin) {
  static unsigned long timestamp = 0;
  PT_BEGIN(pt);
  while(1) {
    PT_WAIT_UNTIL(pt, millis() - timestamp > interval );
    timestamp = millis();
    toggleLED(pin);
  }
  PT_END(pt);
}

void loop() {
  protothread1(&pt1, 100, LEFT_PIN); // schedule the two protothreads
  protothread2(&pt2, 1000, RIGHT_PIN); // by calling them infinitely
}
