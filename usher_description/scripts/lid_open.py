import rospy
from gazebo_msgs.srv import ApplyJointEffort, JointRequest
from std_msgs.msg import Float64
from time import sleep

class MyGazeboPlugin:
    def __init__(self):
        # Initialize the ROS node
        #rospy.init_node('lid_open_plugin')

        # Create a service proxy for applying joint effort
        self.apply_joint_effort_proxy = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)

        # Name of the joint you want to move
        self.joint_name = 'lidj'  # Replace with the name of your joint

    def move_joint(self, effort, duration):
        # Create the request message for applying joint effort
        joint_request = JointRequest()
        joint_request.joint_name = self.joint_name
        joint_request.effort = effort
        joint_request.duration = rospy.Duration(duration)

        # Call the service to apply joint effort
        #self.apply_joint_effort_proxy.call(joint_request)
        self.apply_joint_effort_proxy(joint_name=self.joint_name, effort=effort, start_time=rospy.Time(0, 0), duration=rospy.Duration(duration))

if __name__ == '__main__':
    plugin = MyGazeboPlugin()
    sleep(5)
    plugin.move_joint(effort=1.0, duration=1.0)  # Adjust the effort and duration as needed
    sleep(5)
    plugin.move_joint(effort=-1.0, duration=1.0)  # Adjust the effort and duration as needed
    rospy.spin()
