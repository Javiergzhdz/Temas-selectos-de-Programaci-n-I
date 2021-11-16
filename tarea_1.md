#ROS - Simulación

| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | Código del Trabajo o Número de Tarea | 
| **TSR-2022-I** | Tarea *01 ... n* |
| **Robotica-2022-I**  | Tarea *01 ... n* |
| **IT102321-C002** | Sistema Ciber-Físico - Proyecto - Módulo |

## Contenido

- [Objetivo](#objetivo)
- [Introducción](#introduccion)
- [Desarrollo](#desarrollo)
- [Conclusiones](#conclusiones)
- [Autor](#autor)
- [Referencias](#referencias)

## Objetivo

Redacción del objetivo del trabajo o texto que describe a la tarea (_según sea el caso_).

## Introducción

Párrafo de introducción del trabajo o tarea (_si aplica_). 

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


## Desarrollo

Para consultar el formato a este documento, visitar [Markdown 101](https://github.com/decidim-archive/docs-template/blob/master/es/markdown-101.md).
ver en [texto plano](https://raw.githubusercontent.com/decidim-archive/docs-template/master/es/markdown-101.md)

Ejemplo de párrafo

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.


## Conclusiones

Conclusiones o cierre al trabajo realizado.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet [[3]](#3). **<- referencia insertada en el párrafo** . 

## Autor

***[Nombre del autor o listado de los integrantes del equipo]***

**Autor** Felipe Rivas Campos [GitHub profile](https://github.com/rivascf)

o en caso de tratarse de un equipo

| Iniciales  | Description |
| ----------:| ----------- |
| **RICF** | Felipe Rivas Campos [GitHub profile](https://github.com/rivascf) |
| **EPM**  | Erik Peña Medina [GitHub profile](https://github.com/ErikFiUNAM) |
| **MGR-MX** | Mechatronics Research Group, México [GitHub profile](https://github.com/mrg-mx) |

## Referencias

_Referencia simple_

<a id="1">[1]</a>  I.A. Glover and P.M. Grant, Digital Communications, 3rd ed.  Harlow: Prentice Hall, 2009. 

_Referencia con vínculo insertado en el título del libro_

<a id='2'>[2]</a>	J. B. Kuipers, [Quaternions and rotation sequences](https://amzn.to/2RY2lwI). Princeton, NJ: Princeton University Press, 2002. (Chapter 5,  Section 5.14 “Quaternions to Matrices”, pg. 125)

_Referencia con url externo visible_

<a id="3">[3]</a>  H.-L. Pham, V. Perdereau, B. Adorno, en P. Fraisse, “Position and Orientation Control of Robot Manipulators Using Dual Quaternion Feedback”, 11 2010, bll 658–663. <https://www.researchgate.net/publication/224200087_Position_and_Orientation_Control_of_Robot_Manipulators_Using_Dual_Quaternion_Feedback>

**Nota**:

> Listado de referencias documentales consultadas para realizar el trabajo:
> consultar el siguiente [vínculo](https://www.bath.ac.uk/publications/library-guides-to-citing-referencing/attachments/ieee-style-guide.pdf)
> para el formato de referencia estilo **IEEE**.
> 
> ```text
> [Num ref] Iniciales del autor. Apellido del autor, Título del libro, edicion (si no es la primera). 
> Lugar de publicación: Publicador, Año.
> ```



# Tarea 01

## Descripcion
Problema:
 Hacer que un robot modifique su comportamiento a partir de los siguientes comandos de texto:
    Avanza  [velocidad lineal]
    Gira        [velocidad angular]
    Detente

Restricciones:
    El nombre del paquete de ROS generado debe ser robot_comm.
    El robot a operar debe ser TurtleBot3 en cualquiera de sus versiones (waffle, waffle_pi o burguer).
    Sólo se pueden usar Publicadores y Subscriptores.

Entrega:
Se deberá adjuntar a éste trabajo el vínculo con la dirección del repositorio personal de GitHub con las especificaciones (vínculo adjunto a este mensaje) acordadas en clase.

# Funcionamiento
Primero ejecutar
```
~/rosdev/catkin_ws/src$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Despues ejecutar
````
~/rosdev/catkin_ws rosrun robot_comm programa.py
```

En otra pestaña ejecutar
```
~/rosdev/catkin_ws$ rostopic pub /cmd_robot robot_comm/Comunication "comando: ''
valor: "
```
En comando meter la cadena avanza, detente o gira
en valor para los comandos 'avanza' y 'gira' se especifica un valor

## Desarrollo
Se creo la carpeta msg donde se creo un archivo .msg que contenia el comando y el valor
Despues se creo la carpeta src se hizo el programa, esto a partir de clases, variables, funciones, publicadores y subscriptores.
El codigo se documento con lo que hace cada linea de codigo
Despues se probo en gazebo, y funciono de acuerdo a lo esperado.


## Conclusiones
Para usar ROS en consola, se necesita llevar un registro de los comandos utilizados. Pues de no tenerlo es sumamente complicado hacer cualquier cosa.
En cuanto a Python es importante tener el conocimiento de que es una clase y como funciona. Gran parte del codigo no lo entendia debido a que nunca me quedo claro como funcionaban la clases en python.
Subir archivos a Github es una herramienta de gran ayuda