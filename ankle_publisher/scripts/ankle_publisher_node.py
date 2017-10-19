#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist



def publisher():

	pub = rospy.Publisher('ankle_mock_controller/cmd_vel', Twist, queue_size=10)
	rospy.init_node('ankle_publisher', anonymous=True)
	rate = rospy.Rate(10)

	msg = Twist()
	msg.linear.x = 0.0
	msg.linear.y = 0.0
	msg.linear.z = 0.0
	msg.angular.x = 0.0
	msg.angular.y = 0.0
	msg.angular.z = 0.0
	
	
	
	while not rospy.is_shutdown():
		
		#rospy.loginfo(pub_value)
		pub.publish(msg)
		rate.sleep()


if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
