# Usher
A Robot which can be used in a hotel to guide guests to their rooms, carry their luggage and make deliveries directly to their door step

Instruction for use:
# 1, roslaunch usher_description gazebo.launch
    Launches the gazebo environment
    
# 2, roslaunch usher_description navigation.launch
    Starts the localisation and makes the robot ready for a goal position
    
# 3, python3 usher_description/scripts/path_plan2.py
    A controller with a GUI, when a button is clicked, the robot moves to that location
    This has a while True architecture so it the code will keep asking if you want to continue, 
    typing 'n' or 'N' will exit the loop and closes the file. 


