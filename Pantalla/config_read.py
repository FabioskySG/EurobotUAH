#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json                                # Agrego biblioteca

f = open("config.json", "r")               # Abro fichero (modo lectura)
content = f.read()                         # Leo fichero sobre variable content
jsondecoded = json.loads(content)        

robot_name = jsondecoded["robot_name"]
pose = jsondecoded["pose"]
side = jsondecoded["side"]
mode = jsondecoded["mode"]
routines = jsondecoded["routines"]

print("Robot = " + robot_name)
print(robot_name + " está en " + pose)
print("Comenzamos en el lado " + side)
print("Activamos la rutina del modo " + mode)
print(routines)
