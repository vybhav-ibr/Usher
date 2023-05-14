#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point


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


if __name__ == '__main__':
    try:
        # Initialize the ROS node
        rospy.init_node('go_to_a_specific_point')

        # Define the x and y coordinates of the goal point
        x = 1.0
        y = 2.0

        # Call the go_to_a_specific_point function with the goal coordinates
        go_to_a_specific_point(x, y)

    except rospy.ROSInterruptException:
        pass
