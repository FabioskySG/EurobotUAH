#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import RPi.GPIO as GPIO
import rospy, json, time, yaml
import os

def parseo_msg_yaml(file: str):
        f = open(os.getcwd() + "/" + file, "r") 
        f_parsed = yaml.load(f, Loader=yaml.FullLoader)

        startup_msg = str(f_parsed[0]['robot_name']).strip("['").strip("']")
        '''
        startup_msg = startup(
            String(str(f_parsed[0]['robot_name']).strip("['").strip("']")),
            Pose2D(
                float(f_parsed[1]['pose'][0][0]),
                float(f_parsed[1]['pose'][0][1]),
                float(f_parsed[1]['pose'][0][2])
            ),
            String(str(f_parsed[2]['side']).strip("['").strip("']")),
            String(str(f_parsed[3]['mode']).strip("['").strip("']")),
            orden(
                String("Avanzar"),
                Int32(100)
            )
    
        )
        '''
        return(startup_msg)
'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
'''

test_input = input()            #Lee del teclado

if test_input == "a":
#if GPIO.input(7) or test_input == "a":
    print(parseo_msg_yaml('config1.yaml'))
elif test_input == "b":
#elif GPIO.input(8) or test_input == "b":
    print(parseo_msg_yaml('config2.yaml'))

