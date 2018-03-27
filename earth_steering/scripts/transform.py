#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from four_wheel_steering_msgs.msg import FourWheelSteering




class SteeringTransform(object):


    def __init__(self):
        self.last_sec = 0
        self.last_nano = 0
        self.next_sec = None
        self.next_nano = None
        self.every_nanos = 100000000
        
        
        self.velocity_scale = 0.5
        self.crab_scale = 0.7
        self.turn_scale = 0.7
        self.velocity_boost = 3
        self.max_angle = 0.7
        self.angle_change_rate = 0.5
        self.acceleration = 0.5
        self.jerk = 0.5
        
        topic = "/four_wheel_steering_controller/cmd_four_wheel_steering"
        message_type = FourWheelSteering
        
        self.publisher = rospy.Publisher(topic, message_type, queue_size=10)
        
    def time_delta(self, sec, nano):
        sec_delta = (sec - self.last_sec) * 1000000000
        nano_delta = nano - self.last_nano
        return sec_delta + nano_delta
        
        
    def get_velocity(self, joy):
    
        velocity = -(joy.axes[13] - 1) * float(self.velocity_scale)
        if velocity == 0.5:
            velocity = 0.0
        
        if joy.axes[12] != 0 and joy.axes[12] < 1 :
            velocity = (joy.axes[12] - 1) * float(self.velocity_scale)
        rospy.loginfo("velocity: %s" % velocity)
        return velocity
    	
    
    def get_crab(self, joy):
    
        crab = joy.axes[0]/float(self.crab_scale)
        return crab
        
        
    def get_turn(self, joy):
    
        turn = joy.axes[2]/float(self.turn_scale)
        return turn
        
        
    def get_angles_scaled(self, joy, scale):
    
    	crab = self.get_crab(joy) * scale
    	turn = self.get_turn(joy) * scale
        front = turn/2.0 + crab
        back = -turn/2.0 + crab
        return front, back
    
        
    def get_angles(self, joy):
    
    	front, back = self.get_angles_scaled(joy, 1.0)
        abs_front = abs(front)
        abs_back = abs(back)
        abs_max = max(abs_front, abs_back)
        if abs_max > self.max_angle:
            front, back = self.get_angles_scaled(joy, self.max_angle/abs_max)
        	
        return front, back
        
        
    def send_message(self, velocity, front, back):
    
    	msg = FourWheelSteering(front_steering_angle=front,
    	    rear_steering_angle=back,
    	    front_steering_angle_velocity=self.angle_change_rate,
    	    rear_steering_angle_velocity=self.angle_change_rate,
    	    speed=velocity,
    	    acceleration=self.acceleration,
    	    jerk=self.jerk)
    
        self.publisher.publish(msg)
    
  
    def __call__(self, joy):

        velocity = self.get_velocity(joy)
        front, back = self.get_angles(joy)
        self.send_message(velocity, front, back)


    
def listener():

    transform = SteeringTransform()

    rospy.init_node('earth_steering', anonymous=True)
    rospy.Subscriber("joy", Joy, transform)
    rospy.spin()

if __name__ == '__main__':
    listener()