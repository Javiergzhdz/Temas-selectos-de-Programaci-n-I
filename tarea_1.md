# ROS - Simulación

| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | Tarea 1 | 
| **TSR-2022-I** | Tarea *01 ... n* |
| **Robotica-2022-I**  | Tarea *01 ... n* |
| **IT102321-C002** | Sistema Ciber-Físico - Proyecto - Módulo |

## Contenido

- [Objetivo](#objetivo)
- [Desarrollo](#desarrollo)
- [Conclusiones](#conclusiones)
- [Autor](#autor)

## Objetivo

Hacer que un robot modifique su comportamiento a partir de los siguientes comandos de texto:
Avanza  [velocidad lineal]
Gira        [velocidad angular]
Detente

Restricciones:

El nombre del paquete de ROS generado debe ser **robot_comm**.
El robot a operar debe ser **TurtleBot3** en cualquiera de sus versiones (waffle, waffle_pi o burguer).
Sólo se pueden usar Publicadores y Subscriptores.

Entrega:
Se deberá adjuntar a éste trabajo el vínculo con la dirección del repositorio personal de GitHub con las especificaciones (vínculo adjunto a este mensaje) acordadas en clase.

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