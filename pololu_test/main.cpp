// Uses POSIX functions to send and receive data from a jrk.
// NOTE: The jrk's input mode must be "Serial".
// NOTE: The jrk's serial mode must be set to "USB Dual Port".
// NOTE: You must change the 'const char * device' line below.

#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#ifdef _WIN32
#define O_NOCTTY 0
#else
#include <termios.h>
#endif

// Reads a variable from the jrk.
// The 'command' argument must be one of the two-byte variable-reading
// commands documented in the "Variable Reading Commands" section of
// the jrk user's guide.
int jrkGetVariable(int fd, unsigned char command)
{
    if(write(fd, &command, 1) == -1)
    {
        perror("error writing");
        return -1;
    }

    unsigned char response[2];
    if(read(fd,response,2) != 2)
    {
        perror("error reading");
        return -1;
    }

    return response[0] + 256*response[1];
}

// Gets the value of the jrk's Feedback variable (0-4095).
int jrkGetFeedback(int fd)
{
    return jrkGetVariable(fd, 0xA5);
}

// Gets the value of the jrk's Target variable (0-4095).
int jrkGetTarget(int fd)
{
    return jrkGetVariable(fd, 0xA3);
}

// Sets the jrk's Target variable (0-4095).
int jrkSetTarget(int fd, unsigned short target)
{
    unsigned char command[] = {0xC0 + (target & 0x1F), (target >> 5) & 0x7F};
    if (write(fd, command, sizeof(command)) == -1)
    {
        perror("error writing");
        return -1;
    }
    return 0;
}

int main(int argc, const char * argv[])
{
    printf("------------ POLOLU " __TIME__ "---------------\n");

    int i;
    for(i = 0; i < argc; i++) {
       printf("Argument %i = %s\n", i, argv[i]);
    }

    // Open the Jrk's virtual COM port.
    const char * device = "\\\\.\\USBSER000";  // Windows, "\\\\.\\COM6" also works
    //const char * device = "/dev/ttyACM0";  // Linux
    //const char * device = "/dev/cu.usbmodem00000041"; // Mac OS X

    if (argc > 1) {
    	printf(" Write to [%s]\n", argv[1]);
    } else {
        printf(" Please add device address. Example: /dev/serial/by-id/usb-Pololu_your_id-if00 \n");
        return 0;
    }

    device = argv[1];

    int speed = 3000; 
    if (argc >= 2) {
	speed = atoi(argv[2]);
    }

    int fd = open(device, O_RDWR | O_NOCTTY);
    if (fd == -1)
    {
        perror(device);
        return 1;
    }

#ifndef _WIN32
    struct termios options;
    tcgetattr(fd, &options);
    options.c_lflag &= ~(ECHO | ECHONL | ICANON | ISIG | IEXTEN);
    options.c_oflag &= ~(ONLCR | OCRNL);
    tcsetattr(fd, TCSANOW, &options);
#endif

	int count = 0;
    int feedback = -1;
	while (feedback == -1 && count++ < 10) {
		feedback = jrkGetFeedback(fd);
	}
	
	printf("Current Feedback is %d.\n", feedback);

    int target = -1;

	count = 0;
	while (feedback == -1 && count++ < 10) {
		jrkGetTarget(fd);
	}

	printf("Current Target is %d.\n", target);

    int newTarget=speed; 
    printf("Setting Target to %d.\n", newTarget);
    jrkSetTarget(fd, newTarget);

    close(fd);
    return 0;
}
