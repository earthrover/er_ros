#include <Servo.h>
#include <stdio.h>
#include <stdlib.h>
#include <SoftwareSerial.h>

#define BACK_LEFT   0
#define BACK_RIGHT  1
#define FRONT_LEFT  2
#define FRONT_RIGHT 3

//#define TESTING

Servo Servos[4];
int index = 0;

// Reset the buffer when we have 4 ceros.

int reset = 0;
int head = 0;
uint8_t buffer[16];
uint8_t angle_[4];

static const uint8_t setTargetCommand = 0xC0;
//static const uint8_t setTargetCommand = 0x00;
static const uint8_t getTargetCommand = 0xA3;

#define WRITE7BITDATA(byte) ((byte)&0x7F)

// {0xC0 + (target & 0x1F), (target << 5) & 0x7F}

uint16_t read(uint8_t lower, uint8_t upper) {
    uint8_t cmd = lower & 0x1f;
    uint8_t lowerByte = (lower & 0x1f);
    uint16_t upperByte = (upper & 0x7F) << 5;

    uint16_t value = lowerByte + upperByte;

#ifdef TESTING
    Serial.print(">> cmd: ");
    Serial.println(cmd, HEX);
    Serial.print(">> lower: ");
    Serial.println(lowerByte, HEX);

    Serial.print(">> upper: ");
    Serial.println(upperByte, HEX);
    
    Serial.print(">> value: ");    
    Serial.println(value, DEC);
#endif
    return value;
}

void testing(int target) {
    // split target bytes
    uint8_t lowerByte = target & 0x1F;
    uint8_t upperByte = (target >> 5) & 0x7F;

    Serial.println("--------------------------------");
    Serial.print(">> setTarget: ");
    Serial.println(target, HEX);

    Serial.print(">> lower: ");
    Serial.println(setTargetCommand + lowerByte, HEX);

    Serial.print(">> upper: ");
    Serial.println(WRITE7BITDATA(upperByte), HEX);

    uint32_t value = read(lowerByte, upperByte);

    Serial.print(">> position scaled: ");
    uint8_t pos = (value * 180) / 4095;
    Serial.println(pos, DEC);
}

void setup() {

  //#define BACK_LEFT   0
  //#define BACK_RIGHT  1
  //#define FRONT_LEFT  2
  //#define FRONT_RIGHT 3
  
    Servos[BACK_LEFT].attach(12, 1000, 2000); //out 1
    Servos[BACK_LEFT].write(90);
    angle_[BACK_LEFT] = 160;

    Servos[BACK_RIGHT].attach(11, 1000, 2000); //out 2
    Servos[BACK_RIGHT].write(90);
    angle_[BACK_RIGHT] = 160;

    Servos[FRONT_LEFT].attach(8, 1000, 2000); //out 3
    Servos[FRONT_LEFT].write(90);
    angle_[FRONT_LEFT] = 160;

    Servos[FRONT_RIGHT].attach(7, 1000, 2000); //out 4
    Servos[FRONT_RIGHT].write(90);
    angle_[FRONT_RIGHT] = 160;

    Serial.begin(115200);

#ifdef TESTING
    while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
    }

    testing(0xF0);
    testing(0xF);

    testing(0);
    testing(255);
    testing(2047);
    testing(4095);
#endif
}

int test = 0;
int test_count = 0;

void loop() {
    if (Serial.available() > 0) {
        uint8_t val = Serial.read();

        if (val == 't')
            test_count++;
        else
            test_count = 0;

        if (val == 0)
            reset++;
        else
            reset = 0;

        if (reset == 4) {
            index = 0;
            head = 0;
        }

        buffer[head++ % 32] = val;

        //Serial.print(">> Read: ");
        //Serial.println(val,HEX);

        if (head == 8) {
            int bidx = 0;
            for (int t = 0; t < 4; t++) {
                uint8_t lower = buffer[bidx];
                uint8_t upper = buffer[bidx + 1];

                // Position value comes as [0 .. 4095]
                uint32_t value = read(lower, upper);
                uint8_t pos = (value * 160) / 4096;

                angle_[t] = pos;
                bidx += 2;
            }
            head = 0;
        }
    }

    Serial.println(">> servo Position: ");

    for (int t = 0; t < 4; t++) {
        Serial.println(angle_[t], DEC);
        Servos[t].write(angle_[t]);
    }
    delay(5);

    if (test_count > 4) {
        int pos;

        for (pos = 0; pos <= 160; pos += 1) { // goes from 0 degrees to 180 degrees
            // in steps of 1 degree
            Servos[FRONT_RIGHT].write(pos);
            Servos[FRONT_LEFT].write(pos);
            Servos[BACK_RIGHT].write(pos);
            Servos[BACK_LEFT].write(pos);
            Serial.print(">> servo Position: ");
            Serial.println(pos, DEC);

            delay(30);                       // waits 15ms for the servo to reach the position
        }

        for (pos = 160; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
            Servos[FRONT_RIGHT].write(pos);
            Servos[FRONT_LEFT].write(pos);
            Servos[BACK_RIGHT].write(pos);
            Servos[BACK_LEFT].write(pos);
            Serial.print(">> servo Position: ");
            Serial.println(pos, DEC);

            delay(30);                       // waits 15ms for the servo to reach the position
        }
    }

    /*
    test++;
    Servos[FRONT_RIGHT].write(test%180);
    Servos[FRONT_LEFT].write(test%180);
    Servos[BACK_RIGHT].write(test%180);
    Servos[BACK_LEFT].write(test%180);

    Serial.print(">> servo Position: ");
    Serial.println(test%180, DEC);
    */
    //delay(100);
}



