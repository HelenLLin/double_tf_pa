# double_tf_pa

The double_tf_pa creates 3 turtles and makes them follow each other. The first turtle is controlled by the keyboard, the second turtle follows the first turtle, and the third turtle follows the second turtle. The turtles broadcast their locations to each other through the tf_broadcaster and uses tf to update each turtle's location to be relative to each other.

# Running the project
1. In the first terminal, run $ roscore
2. In another terminal, run $ roslaunch double_tf_pa start_demo.launch
3. Click on the terminal window and use the arrow keys to move the first turtle around
4. The second and third turtle will follow
