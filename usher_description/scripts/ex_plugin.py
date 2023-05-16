import subprocess

def execute_gazebo_plugin():
    command = ['gazebo', '-s', 'libgazebo_ros_init.so', '-e', 'python3', 'lid_open.py']
    subprocess.call(command)

if __name__ == '__main__':
    execute_gazebo_plugin()
