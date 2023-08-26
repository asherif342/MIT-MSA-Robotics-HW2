#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Pose
from std_msgs.msg import float32
import numpy as np
import math
from random import random

submarine_x_position = random()*200 - 100   # possible positions are restricted between
submarine_y_position = random()*200 - 100   # -100 and +100 meters for both x and y coordinates
                                            # submarine position is randomly determined ONCE
                                            # in this code, but the Locator instance operates
                                            # repeatedly
class Locator:
    '''
    there is a circle of radius 8 meters defining a 2D safe zone for a submarine. The safe 
    zone's center is being
    broadcast by an external node not initiated within this file. The purpose of this locator class is
    to instantiate node(s) that subscribe to the circle information and use that information
    to determine whether the submarine is within it or not, and how far it is from the center 
    of the safe zone. These 2 results should be published to 2 different topics.
    
    '''

    def __init__(self):
        '''
        when an instance of a class is created, the __init__ method always runs before all else
        so we can write all the code we want to be executed within this function for the purposes
        of this node example
        '''
        def safezone_callback(safezone_data):
            """
            This callback function is run everytime the SCAN_TOPIC topic is updated. The sole
            argument of this function is the updated value from the topic. Everytime the 
            safezone data being published is updated (the center of the circle) we want to 
            update our understanding of our submarine's location relative to the circle
            """
            #TODO extract the x and y position data from the message that is being passed
            # through this callback function
           
            #x_center =
            #y_center =

            #TODO calculate the distance between the submarine's position and the center of the
            # circle defining the safezone (hint: use math.sqrt())
            
            #distance = 
            
            if distance <= 8:
                in_zone = 1
            else:
                in_zone = 0
            
            #publish the results now that they have been updated
            float32_message_1 = Float32(in_zone)
            Inside_Safezone_Result.publish(float32_message_1)
        
            float32_message_2 = Float32(distance)
            Distance_From_Center = rospy.Publisher(float32_message_2)
            
        rate = rospy.Rate(10)
        
        #TODO: Initialize the subscriber which will monitor the topic containing the circle's
        # center information, specifying the topic, ROS message type for that topic, and the
        # callback function:
        
        #Safezone_Data = 

        #Initialize publishers which will publish the 2 pieces of data derived from the 
        # previously subscribed-to topic so that they are published to 2 new topics (inside_topic,
        # distance_topic). These should specify the message type being used (float32):
        
        #Inside_Safezone_Result = 
        #Distance_From_Center = 

if __name__ == "__main__":
    #### TODO ####
    # initialize a ROS node named  "locator_node" on the line below
    #node = 
    
    Locator()
    rospy.spin()
