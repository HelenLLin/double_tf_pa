#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # spawns turtle2
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtle_name = rospy.get_param('turtle', 'turtle2')
    spawner(4, 2, 0, turtle_name)

    # spawns turtle3
    rospy.wait_for_service('spawn')
    spawner2 = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    turtle_name2 = rospy.get_param('turtle', 'turtle3')
    spawner(4, 4, 0, turtle_name2)

    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
    turtle_vel2 = rospy.Publisher('%s/cmd_vel' % turtle_name2, geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(turtle_name, 'turtle1', rospy.Time())
            trans2 = tfBuffer.lookup_transform(turtle_name2, 'turtle2', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.Twist()
        msg2 = geometry_msgs.msg.Twist()

        msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)
        msg2.angular.z = 4 * math.atan2(trans2.transform.translation.y, trans2.transform.translation.x)
        msg2.linear.x = 0.5 * math.sqrt(trans2.transform.translation.x ** 2 + trans2.transform.translation.y ** 2)

        turtle_vel.publish(msg)
        turtle_vel2.publish(msg2)

        rate.sleep()