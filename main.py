#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from startup_robot.src.startup import StartupNode

if __name__ == "__main__":

    startup = StartupNode()

    startup.init_luces()
    message = startup.parseo_msg_yaml()

    respuesta = startup.startup_client(message)
    startup.luces(respuesta)

    while not rospy.is_shutdown():
        pass



    