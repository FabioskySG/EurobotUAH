#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, json, time, board, neopixel, yaml                      # Agrego biblioteca
from std_msgs.msg import Int32, String
from geometry_msgs.msg import Pose2D
from uah_msgs.msg import startup, orden
from uah_msgs.srv import startup_serv

class StartupNode():

    def __init__(self):
        rospy.init_node('startup_node')

        self.pub_posavasos = rospy.Publisher('posavasos_config', startup, queue_size=100)
        self.pub_parejitas = rospy.Publisher('parejitas_config', startup, queue_size=100)

        self.init_luces()


    def parseo_msg_json(self):
        f = open("/home/fabio/Escritorio/ros_ws/src/startup_robot/src/config.json", "r")                 # Abro fichero (modo lectura)
        content = f.read()                           # Leo fichero sobre variable content
        jsondecoded = json.loads(content)        

        robot_name = jsondecoded["robot_name"]
        pose = jsondecoded["pose"]                   #Tengo que pasar este string a datos
        side = jsondecoded["side"]
        mode = jsondecoded["mode"]
        routines = jsondecoded["routines"]           #Tengo que almacenarlo como string y int32

        pose = pose.strip("[")
        pose = pose.strip("]")

        pose = list(map(float, pose.split(',')))     # Extraigo los float del array de pose

        x = pose[0]                                  #Asocio los valores extraidos a cada atributo de Pose2D
        y = pose[1]
        theta = pose[2]

        startup_msg = startup(robot_name, Pose2D(x,y,theta), side, mode, [orden(routines,10)]) # Creo un objeto con la clase startup (mensaje)
        return(startup_msg)

    def parseo_msg_yaml(self):
        f = open("/home/fabio/Escritorio/ros_ws/src/startup_robot/src/config.yaml", "r") 
        f_parsed = yaml.load(f, Loader=yaml.FullLoader)

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
        return(startup_msg)
    
    def startup_client(self, startup_msg: object):
        servicio = rospy.ServiceProxy('servicio_startup', startup_serv)
        try:
            rospy.wait_for_service('servicio')
            resp = servicio(startup_msg)
            return resp.confirmacion
        
        except rospy.ServiceException as exc:
            print("Service call failed: " + str(exc))

    def init_luces(self):
        pixel_pin = board.D18
        num_pixels = 30
        self.pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brigthness = 0.2, auto_write = False, pixel_order = neopixel.RGB)

    def luces(self, respuesta: bool):
        
        if respuesta == True:
            self.pixels.fill((0, 255, 0))
            self.pixels.show()
            time.sleep(5)

        if respuesta == False:
            for i in range(10):
                self.pixels.fill((255, 0, 0))
                self.pixels.show()
                time.sleep(0.5)




