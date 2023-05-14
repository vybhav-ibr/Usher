#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
from box import GUI

current_position = Point()

def callback(msg):
    global current_position,current_orient
    current_position = msg.pose.pose.position
    #current_orient=msg.twist.twist
    #rospy.loginfo(current_position)
sub = rospy.Subscriber('/odom', Odometry, callback)
def go_to_a_specific_point(x, y):
    # Create a move_base client
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    # Wait for the action server to come up
    client.wait_for_server()

    # Create a move_base goal from the x and y coordinates
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position = Point(x, y, 0)
    goal.target_pose.pose.orientation.w = 1.0

    # Send the goal and wait for the result
    client.send_goal(goal)

    # Set the obstacle avoidance parameters
    client.wait_for_result(rospy.Duration.from_sec(300.0))
    state = client.get_state()
    rospy.loginfo("Current state: %s", state)

    # Check if the goal was reached
    if state == 3:
        rospy.loginfo("Goal reached successfully!")
        return True
    else:
        rospy.loginfo("Failed to reach the goal")
        return False

dim={
 "1-1": [16,14]
,"1-2": [16,9]
,"2-1": [13,14]
,"2-2": [13,9]
,"3-1": [11,14]
,"3-2": [11,9]
,"4-1": [9,14]
,"4-2": [9,9]
,"5-1": [6.5,14]
,"5-2": [6.5,9]
,"6-1": [4,14]
,"6-2": [4,9]
,"7-1": [2,14]
,"7-2": [2,9]
,"1-4": [16,-14]
,"1-3": [16,-9]
,"2-4": [13,-14]
,"2-3": [13,-9]
,"3-4": [11,-14]
,"3-3": [11,-9]
,"4-4": [9,-14]
,"4-3": [9,-9]
,"5-4": [6,-14]
,"5-3": [6,-9]
,"6-4": [4,-14]
,"6-3": [4,-9]
,"7-4": [2,-14]
,"7-3": [2,-9]
,"Reception":[0,0]
}
if __name__ == '__main__':
    try:
        rospy.init_node('go_to_a_point')
        cnt=0
        while(True):
            com=input("Would you like to continue :")
            if com=='N' or com=='n':
                break
            else:
                g=GUI()
                print("Going to room",g.s)
                coord=dim[g.s]
                x = coord[0]
                y = coord[1]
                go_to_a_specific_point(x, y)
        

    except rospy.ROSInterruptException:
        pass
