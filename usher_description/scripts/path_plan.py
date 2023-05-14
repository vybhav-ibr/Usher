#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from math import atan2, sqrt

# Set the target point here
target_point = Point()
target_point.x = 2.5
target_point.y = 3.0

# Set the distance tolerance here
distance_tolerance = 0.5

# Initialize the ROS nodewist_keyboard
rospy.init_node('path_plan')

# Initialize the current position
current_position = Point()
current_orient=Twist()
# Define the callback function for the subscriber
def callback(msg):
    global current_position,current_orient
    current_position = msg.pose.pose.position
    current_orient=msg.twist.twist
    #rospy.loginfo(current_orient.angular.z)

# Initialize the publisher and subscriber
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/odom', Odometry, callback)


# Define the main loop
rate=rospy.Rate(5)
while not rospy.is_shutdown():
    
    # Compute the distance to the target point
    distance_to_target = sqrt((target_point.x - current_position.x)**2 + (target_point.y - current_position.y)**2)
    rospy.loginfo(distance_to_target)
    rospy.loginfo(current_orient.angular.z)
    # Check if the target point has been reached
    if(distance_to_target <= distance_tolerance or 
    current_position.x-target_point.x in range(-1,1) or 
    current_position.y-target_point.y in range(-1,1)):
        rospy.loginfo("Target point reached")

        break

    # Compute the angle to the target point
    angle_to_target = atan2(target_point.y - current_position.y, target_point.x - current_position.x)

    # Compute the angular velocity to turn towards the target point
    angular_velocity = angle_to_target - current_orient.angular.z

    # Compute the linear velocity to move towards the target point
    linear_velocity = min(distance_to_target, 0.5)

    # Publish the velocity commands
    twist_msg = Twist()
    twist_msg.linear.x = linear_velocity
    twist_msg.angular.z = angular_velocity
    pub.publish(twist_msg)

    # Sleep for a short period of time
    #rospy.sleep(0.1)
    rate.sleep()

# Stop the robot
twist_msg = Twist()
twist_msg.linear.x = 0.0
twist_msg.angular.z = 0.0
pub.publish(twist_msg)
