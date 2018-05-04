#include <ros/ros.h>

#include <sensor_msgs/BatteryState.h>

using namespace std;

#define K 0.00472199
#define CELLS 6
#define MAX_CELLS 12

double cell_const[MAX_CELLS] = {1.0000, 2.1915, 2.6970,  4.1111,
                                4.7333, 6.6000, 6.6000,  7.8293,
                                8.4667, 9.2353, 11.0000, 11.0000};

int main(int argc, char **argv) {
    printf("[TODO] BATTERY LEVELS \n");
    /*
    ros::init(argc, argv, "battery_state");

    ros::NodeHandle nh;

    sensor_msgs::BatteryState batt_state;

    ros::Publisher batteryState("battery_state", &batt_state);

    // Initialize the ROS node.
    nh.initNode();
    nh.advertise(batteryState);

    // Populate battery parameters.
    batt_state.design_capacity = 2200;      // mAh
    batt_state.power_supply_status = 2;     // discharging
    batt_state.power_supply_health = 0;     // unknown
    batt_state.power_supply_technology = 3; // LiPo
    batt_state.present = 1;                 // battery present

    batt_state.location = "Crawler";       // unit location
    batt_state.serial_number = "ABC_0001"; // unit serial number
    batt_state.cell_voltage = new float[CELLS];

    ros::Rate r(5);

    while (ros::ok()) {
        // Battery status.
        double battVoltage = 0.0;
        double prevVoltage = 0.0;

        // Update battery health.
        batt_state.voltage = (float) battVoltage;

        if (batt_state.voltage > CELLS * 4.2)
            batt_state.power_supply_health = 4; // overvoltage
        else if (batt_state.voltage < CELLS * 3.0)
            batt_state.power_supply_health = 3; // dead
        else
            batt_state.power_supply_health = 1; // good

        // Publish data to ROSSERIAL.
        batteryState.publish(&batt_state);

        ros::spinOnce();
        r.sleep();
    }
    */

    return 0;
}
