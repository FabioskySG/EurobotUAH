#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print msg.data

rospy.init_node('node_suscriber')
sub = rospy.Subscriber('counter', Int32, callback)  # Callback es lo que se hace cuando el suscriptor recibe algo
rospy.spin()
