#!/usr/bin/env python
#importando cosas
import rospy
from robot_comm.msg import Comunication
from geometry_msgs.msg import Twist

#la clase
class Robot_command(object):
    #definiendo el constructor
    def __init__(self):
        #definiento a _sentcommand como el archivo que esta dentro de msg
        self._sentcommand = Comunication()
        #definiendo el publicador
        self._cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        #definiendo el subscriptor
        self.distance_moved_sub = rospy.Subscriber('/cmd_robot', Comunication, self._action_with_command)
    #lo que va a hacer con el comando
    def _action_with_command(self, data):
        #el argumento data, va a ser el comando que se envio
        self._sentcommand = data
        #El estado del robot esta determinado por Twist()
        robot_state = Twist()
        #si el comando que se envio no es nulo
        if not self._sentcommand is None:
            #si el comando en minuscula es forward
            if self._sentcommand.comando.lower() == 'avanza':
                #el estado de la velocidad lineal en x es igual al argumento "valor" del mensaje
                robot_state.linear.x = self._sentcommand.valor
                #la velocidad angular del robot es 0 por lo tanto no gira
                robot_state.angular.z = 0.0
                #Se publica el estadodel robot
                self._cmd_vel_pub.publish(robot_state)
                #se indica que se recibio
                rospy.loginfo('Recibi el comando: ({}, {}), enviado.'.format(self._sentcommand.comando, self._sentcommand.valor))
            #si el comando es turn
            elif self._sentcommand.comando.lower() == 'gira':
                #la velocidad lineal es cero
                robot_state.linear.x = 0.0 
                #la velocidad angular es el valor especificado
                robot_state.angular.z = self._sentcommand.valor
                #se publica 
                self._cmd_vel_pub.publish(robot_state)
                #sale mensaje del comando que se recibio junto con su valor
                rospy.loginfo('Recibi el comando: ({},{}), enviado'.format(self._sentcommand.comando, self._sentcommand.valor))
            #si el comando es stop
            elif self._sentcommand.comando.lower() == 'detente':
                #la velocidad lineal de el robot es 0
                robot_state.linear.x = 0.0
                #la velocidad angular del robot es 0
                robot_state.angular.z =0.0
                # se publica el estado del robot
                self._cmd_vel_pub.publish(robot_state)
                #se manda el mensaje de que es lo que se recibio
                rospy.loginfo('Recibi el comando: ({},{}), enviado'.format(self._sentcommand.comando, self._sentcommand.valor))
            #cualquier otra opcion
            else:
                #se manda un mensaje de error
                print('El comando esta mal. Me mandaste: ({},{}), enviado'.format(self._sentcommand.comando, self._icommand.valor))
    #para que se mantenga corriendo
    def keep_running(self):
        #para que se corra muchas veces el programa
        rospy.spin()
    
#definimos la funcion principal            
def main():
    #para los posibles 
    try:
        #inicia el nodo aunque para este programa no se necesita
        rospy.init_node('move_please')
        #se inicia la clase
        cmd_listener = Robot_command()
        #la parte del problema para que siga corriendo
        cmd_listener.keep_running()
    #si se interrumpe por alguna exception entonces se imprimer el error
    except rospy.ROSInterruptException as e:
        #imprime el error
        print(str(e))
    
#pa que se haga la funcion main
if __name__ == '__main__':
    main()

#De aqui para abajo es un programa fallido que ya no funciono 

"""
import rospy
from robot_comm.msg import Comunication
from geometry_msgs.msg import Twist


class CommandListener(object):
    def __init__(self):
        self._icommand = Comunication()
        self._cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.distance_moved_sub = rospy.Subscriber('/cmd_robot', Comunication, self._on_robot_comand)

    def _on_robot_comand(self, data):
        self._icommand = data
        robot_state = Twist()
        if not self._icommand is None:
            if self._icommand.comando.lower() == 'avanza':
                robot_state.linear.x = self._icommand.valor
                robot_state.angular.z = 0.0
                self._cmd_vel_pub.publish(robot_state)
                rospy.loginfo('Recibi el comando: ({}, {}), enviado.'.format(self._icommand.comando, self._icommand.valor))
            elif self._icommand.comando.lower() == 'gira':
                robot_state.linear.x = 0.0
                robot_state.angular.z = self._icommand.valor
                self._cmd_vel_pub.publish(robot_state)
                rospy.loginfo('Recibi el comando: ({}, {}), enviado.'.format(self._icommand.comando, self._icommand.valor))
            elif self._icommand.comando.lower() == 'detente':
                robot_state.linear.x = 0.0
                robot_state.angular.z = 0.0
                self._cmd_vel_pub.publish(robot_state)
                rospy.loginfo('Recibi el comando: ({}, {}), enviado'.format(self._icommand.comando, self._icommand.valor))
            else:
                print('Recibi el comando: ({}, {}), descartado.'.format(self._icommand.comando, self._icommand.valor))

    def loop(self):
        rospy.spin()    

def main():
    try:
        rospy.init_node('asgmnt01')
        cmd_listener = CommandListener()
        cmd_listener.loop()
    except rospy.ROSInterruptException as e:
        print(str(e))

if __name__ == '__main__':
    main()
"""