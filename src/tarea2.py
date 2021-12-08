#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
#Inicializando variables
x = 0.0
y = 0.0 
theta = 0.0
# la clase para asignar a las variables la posicion
def newOdom(msg):
    global x
    global y
    global theta
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
rospy.init_node("speed_controller")
#inicializando el subscriptor y el publicador
sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
speed = Twist()
r = rospy.Rate(4)
goal = Point()
#Definiendo la meta
goal.x = 5
goal.y = 5
#si no esta apagado
while not rospy.is_shutdown():
    #Lo que falta para llegar a la meta
    inc_x = goal.x -x
    inc_y = goal.y -y

    angle_to_goal = atan2(inc_y, inc_x)
    #si la diferencia es mayor a 0.1 entonces corrige la direccion en la cual se mueve
    if abs(angle_to_goal - theta) > 0.1:
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    #si la diferencia es menor a 0.1 el robot sigue avanzando en linea recta
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0

    pub.publish(speed)
    r.sleep()   