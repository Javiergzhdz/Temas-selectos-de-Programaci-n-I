# ROS - Simulación, Tarea 2

| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | Tarea 2 | 
| **TSR-2022-I** | Tarea *02 ... n* |
| **Robotica-2022-I**  | Tarea *02 ... n* |
| **IT102321-C002** | Sistema Ciber-Físico - Proyecto - Módulo |

## Contenido

- [Objetivo](#objetivo)
- [Investigacion](#investigacion)
- [Desarrollo](#desarrollo)
- [Funcionamiento](#funcionamiento)
- [Conclusiones](#conclusiones)
- [Autor](#autor)

## Objetivo

Objetivo, este trabajo se compone de dos partes:

    Investigación. Investigar los diferentes sensores que componen al robot Robotis Turtlebot3 Waffle y su transmisión de datos en ROS (nodos, tópicos, servicios, simulaciones).
    Simulación: Mover al robot de su posición inicial a un punto dado de coordenadas (X, Y).

Restricciones:

    El reporte de investigación debe ser redactado en uno o varios documentos de markdown en la carpeta docs y referenciados a través del archivo README.md
    El nombre del paquete de ROS generado debe ser robot_comm, usado en la tarea anterior.
    El robot a operar debe ser TurtleBot3 Waffle.
    Para los obstáculos se puede usar la técnica vista en clase o algún mundo de su preferencia.
    El sentido de giro para evitar el obstáculo puede ser arbitrario: siempre horario, siempre anti-horario o algún otro parámetro que deseen emplear para la decisión del robot.
    Se pueden usar Publicadores, Subscriptores y Servicios.

Entrega:
Se deberá adjuntar a éste trabajo el vínculo con la dirección del repositorio personal de GitHub con las especificaciones (vínculo adjunto a este mensaje) acordadas en clase.

## Investigacion
TurtleBot3 es una nueva generacion de robot mobil modular, compacto y adaptable. Es pequeño, economico, programable, usado para educacion, investigacion, hobbies y prototipado. 
TurtleBot3 puede ser personalizado en varias maneras dependiendo en como se reconstruyan sus partes mecanicas y se usan sus partes opcionales como la computadora y el sensor.
TurtleBot puede correr SLAM (simultaneos localization and mapping), algoritmos que construyen un mapa. Puede ser controlado por laptop, joypad o un smart phone basado en Android. TurtleBot3 puede ser usado como un manipulador mobil, capaz de manipular un objeto  con OpenMANIPULATOR. 

### Sensores
#### LDS-01
-El Laser Distance Sensor (LDS) es un scanner laser capas de sensar 360 grados, que recolecta un conjunto de informacion alrededor del robot, esto para ser usado en SLAM y Navegacion
- Soporta interface USB y es facil de instalar en una computadora. 
- Puede soportar UART
- 5V DC ±5%
- Distancia de deteccion 120mm ~ 3,500mm
- Sampling Rate 1.8kHz

Distance Accuracy (120mm ~ 499mm) 	±15mm
Distance Accuracy(500mm ~ 3,500mm) 	±5.0%
Distance Precision(120mm ~ 499mm) 	±10mm
Distance Precision(500mm ~ 3,500mm) 	±3.5%
Rango angular  	360°
Resolucion angular 	1°

#### Raspberry Pi Camera Module 2
La camara puede ser usada para videos de alta definicion asi como parafotografias. Soporta 1080p30, 720p60 y VGA90 modulos de videojuegos.


## Desarrollo
El programa consta de dos programas.
## [tarea2.py](https://github.com/Javiergzhdz/Temas-selectos-de-Programaci-n-I/blob/main/src/tarea2.py)
es el programa el cual ayuda al robot a llegar al distino. Basicamente hace que el robot gire de tal forma que al momento de avanzar en linea recta, vaya en direccion a el objetivo. Si por alguna razon el robot no va en linea recta y se desvia, el robot girara para corregir el rumbo
## [move_to_destiny.py](https://github.com/Javiergzhdz/Temas-selectos-de-Programaci-n-I/blob/main/src/move_to_destiny.py)
Le indica al robot, que si el sensor LDS encuentra un obstaculo, el robot lo debe evadir. En su caso el robot lo puede evadir ya sea girando a la izquierda o la derecha. una vez que lo evade continua moviendose en direccion al objetivo

## Funcionamiento
Primero ejecutar

```
~/rosdev/catkin_ws/src/robot_comm$ roslaunch turtlebot3_gazebo turtlebot3_any_world.launch
```
Despues ejecutar
```
~/rosdev/catkin_ws/src/robot_comm$ rosrun robot_comm tarea2.py
```

En otra pestaña ejecutar
```
~/rosdev/catkin_ws/src/robot_comm$ rosrun robot_comm move_to_destiny.py
```
En comando meter la cadena avanza, detente o gira
en valor para los comandos 'avanza' y 'gira' se especifica un valor

## Conclusiones
Con las herramientas que nos proporciona ROS, podemos automatizar a los robots. 
Haciendo uso de los sensores con los que los robots cuentan, se pueden realizar distintos procesos. Por ejemplo en el caso de esta actividad se puede programar para que el robot llegue a cierta posicion aunque haya obstaculos en el camino. Pues con la informacion que capta el robot, se pueden programar rutinas que, en este caso, indiquen que debe de evitar un obstaculo.
Cabe mencionar que debido a una circunstancia que desconosco, en la simulacion el robot no evita el obstaculo, choca contra el y da una vuelta de casi 360 grados en sentido antihorario, avanza, vuelve a chocar y repite el proceso. Pero si no se cuenta con ningun obstaculo, el robot llega a el punto meta indicado.

## Autor

***Javier Guzman Hernandez***

**Autor** Javiergzhdz [GitHub profile](https://github.com/Javiergzhdz)