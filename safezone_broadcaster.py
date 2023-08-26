#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Pose
from random import random

center_publisher = rospy.Publisher("center_info_topic", Pose, queue_size=10)

def main():
    msg = Pose()
    msg.position.x = 20
    msg.position.y = -10
    center_publisher.publish(msg)

if __name__ == "__main__":
    rospy.init_node("broadcaster")
    main()
    rospy.spin()
