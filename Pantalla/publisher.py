#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')     # Iniciamos nodo
pub = rospy.Publisher('counter', Int32, queue_size = 100) # Publisher está en rospy - queue_size elementos en la cola esperando a ser mandados
rate = rospy.Rate(2)    # Frecuencia de envío de mensajes

count = 0
while not rospy.is_shutdown(): # Mientras que no esté apagado rospy
    pub.publish(count)
    count += 1
    rate.sleep()
