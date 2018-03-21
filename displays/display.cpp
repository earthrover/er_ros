//
//DislayTest.cpp
//
#include <termios.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/signal.h>
#include <sys/types.h>
#define BAUDRATE B19200
#define device "/dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0"

unsigned char ClearScreen[] = {254,88};
unsigned char WelcomeMessage[] = {'H','e','l','l','o',' ','W','o','r','l','d','!'};
int main(int argc, char *argv[])
{
 struct termios term;
 //Open the serial port
 int lcd = open(device, O_RDWR | O_NOCTTY | O_NONBLOCK);
 //handle errors
 if (lcd < 0)
 {
 printf("Error opening serial port %s\n",device);
 return -1;
 }

 //Setup the serial port 8 data bits, no parity ,1 stopbit, no flow control
 term.c_cflag = BAUDRATE | CS8 | CSTOPB | CLOCAL | CREAD;
 term.c_iflag = 0;
 term.c_oflag = 0;
 term.c_lflag = 0;
 tcflush(lcd, TCIFLUSH);
 tcsetattr(lcd,TCSANOW,&term);

 //Write Welcome Message to the display
 write(lcd,ClearScreen,sizeof(ClearScreen));
 write(lcd,WelcomeMessage,sizeof(WelcomeMessage));

 //Close the display
 close(lcd);
 return 0;
} 
