#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from robot_comm.msg import Estatus

def process_msg_callback(msg):

    # Initilize velocities 
    msg.twist.twist.linear.x = 0
    msg.twist.twist.linear.y = 0
    msg.twist.twist.linear.z = 0
    msg.twist.twist.angular.x = 0
    msg.twist.twist.angular.y = 0



    command = str(
        raw_input('Escribir el comando'))
    if command == "Avanzar":
        forward = True
    elif command == "Gira":
        angle = int(
        raw_input('Meta la velocidad en radianes: '))
        turn = True
        angle = angle * 3.14 /180
    elif command == "Detente":
        stop = True
    else:
        pubmsg.estado = 'Error solo se admite Avanzar, Gira o Detente'

    if turn:
        msg.twist.twist.angular.z = angle
    elif forward:
        msg.twist.twist.linear.x = 1
    elif stop:
        msg.twist.twist.linear.x = 0
        msg.twist.twist.linear.y = 0
        msg.twist.twist.linear.z = 0
        msg.twist.twist.angular.x = 0
        msg.twist.twist.angular.y = 0



rospy.init_node('programa')
sub = rospy.Subscriber('odom', Odometry, process_msg_callback)
pub = rospy.Publisher('estatus',Estatus, queue_size=2)
rate = rospy.Rate(2)
pubmsg = Estatus()
rospy.spin()

"""
    dx = round(msg.twist.twist.linear.x, 2)
    # Debido a que nuestro robot es (2,0) no puede moverse sobre el eje Y
    # dy = msg.twist.twist.linear.y
    theta = round(msg.twist.twist.angular.z, 2)
    rospy.loginfo('Actualmente el robot tiene dx={:.2f} m/s, theta={:.2f} radianes'.format(dx, theta))
    if dx == 0.0 and theta == 0.0:
        pubmsg.codigo = 0
        pubmsg.estado = 'Detenido'
    elif dx != 0.0 and theta == 0.0:
        pubmsg.codigo = 100
        pubmsg.estado = 'Solo vel lineal: {} m'.format(dx)    
    elif dx == 0.0 and theta != 0.0:
        pubmsg.codigo = 200
        pubmsg.estado = 'Solo vel angular: {} rads'.format(theta)    
    elif dx != 0.0 and theta != 0.0:
        pubmsg.codigo = 300
        pubmsg.estado = 'movimiento lineal: {} m y angular: {} rads'.format(dx, theta)
    else:
        pubmsg.codigo = 1000
        pubmsg.estado = 'Error'        
    pub.publish(pubmsg)


    






rospy.init_node('robot_control_node', anonymous=True)
self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
self.cmd = Twist()
self.rate = rospy.Rate(10)


# if __name__=='__main__':
#    init_monitor()








#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time


#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from robot_comm.msg import Estatus




rospy.init_node('robot_control_node', anonymous=True)
self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
self.cmd = Twist()
self.rate = rospy.Rate(10)



def get_command(self):



    return [self.forward, self.turn, self.stop, self.angular_speed]


def execute(self, forward, turn, stop, angle):



    # Convert speed and angle to radians
    forward, turn, stop, angle = self.get_command()

    # Check the direction of the rotation




if __name__ == '__main__':
robotcontrol_object = RobotControl()
try:
    res = robotcontrol_object.execute()
except rospy.ROSInterruptException:
    pass
"""