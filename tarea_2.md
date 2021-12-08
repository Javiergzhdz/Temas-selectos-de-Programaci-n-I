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

https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_01/


https://www.raspberrypi.com/products/camera-module-v2/

https://emanual.robotis.com/docs/en/platform/turtlebot3/features/

https://repository.usta.edu.co/bitstream/handle/11634/18667/2019davidmartinez.pdf?sequence=1&isAllowed=y

## Desarrollo
Se creo la carpeta msg donde se creo un archivo .msg que contenia el comando y el valor
Despues se creo la carpeta src se hizo el programa, esto a partir de clases, variables, funciones, publicadores y subscriptores.
El codigo se documento con lo que hace cada linea de codigo
Despues se probo en gazebo, y funciono de acuerdo a lo esperado.

## Funcionamiento
Primero ejecutar

```
~/rosdev/catkin_ws/src$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
Despues ejecutar
```
~/rosdev/catkin_ws rosrun robot_comm programa.py
```

En otra pestaña ejecutar
```
~/rosdev/catkin_ws$ rostopic pub /cmd_robot robot_comm/Comunication "comando: ''
valor: "
```
En comando meter la cadena avanza, detente o gira
en valor para los comandos 'avanza' y 'gira' se especifica un valor

## Conclusiones
Para usar ROS en consola, se necesita llevar un registro de los comandos utilizados. Pues de no tenerlo es sumamente complicado hacer cualquier cosa.
En cuanto a Python es importante tener el conocimiento de que es una clase y como funciona. Gran parte del codigo no lo entendia debido a que nunca me quedo claro como funcionaban la clases en python.
Subir archivos a Github es una herramienta de gran ayuda

## Autor

***Javier Guzman Hernandez***

**Autor** Javiergzhdz [GitHub profile](https://github.com/Javiergzhdz)