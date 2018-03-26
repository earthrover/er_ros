cd ~/catkin_ws/src/earth-rover-ros/pololu_test

echo FRONT LEFT

./a.out /dev/serial/by-id/usb-Pololu_Corporation_Pololu_Jrk_21v3_Motor_Controller_00203356-if00

echo BACK RIGHT
./a.out /dev/serial/by-id/usb-Pololu_Corporation_Pololu_Jrk_21v3_Motor_Controller_00104525-if00

echo BACK LEFT
./a.out /dev/serial/by-id/usb-Pololu_Corporation_Pololu_Jrk_21v3_Motor_Controller_00155898-if00

echo FRONT RIGHT
./a.out /dev/serial/by-id/usb-Pololu_Corporation_Pololu_Jrk_21v3_Motor_Controller_00140203-if00



