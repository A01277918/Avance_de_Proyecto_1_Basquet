# Avance\_Proyecto\_1\_Basquetbol


# Estadísticas de jugadores de básquetbol

## Contexto

Escogí el tema del básquetbol porque es un deporte que me gusta mucho y que considero muy interesante, no solamente por jugarlo, sino también por todo lo que pasa dentro de un partido. Me gusta la emoción de los partidos, las jugadas, los tiros de tres, las asistencias y la forma en la que cada jugador puede aportar algo diferente a su equipo. Además, creo que el básquetbol es un deporte en el que las estadísticas tienen mucha importancia, ya que muchas veces sirven para saber qué tan bien jugó una persona y qué fue lo que aportó durante el partido.

Por eso, en este proyecto quise desarrollar un programa que permita registrar y calcular las estadísticas de 5 jugadores de básquetbol durante un partido. Algunas de las estadísticas que se van a tomar en cuenta son los puntos, asistencias, rebotes, robos, pases fallidos, puntos de tres y pérdidas de balón. Al final, el programa utilizará estos datos para obtener una puntuación del desempeño de cada jugador del 1 al 10, siendo 10 la mejor calificación.

¿Por qué es interesante?

Elegí este tema porque el básquetbol es uno de mis deportes favoritos y me parece interesante intentar utilizar la programación para analizar algo que normalmente podemos ver durante un partido. Muchas veces cuando vemos un juego nos damos cuenta de que un jugador tuvo un buen partido porque anotó muchos puntos, pero también existen otras cosas importantes como las asistencias, los rebotes, los robos o incluso los errores que tuvo.

Además, considero interesante que el programa pueda tomar todas estas estadísticas y convertirlas en una calificación sencilla que permita comparar el desempeño de los 5 jugadores. De esta manera, no solamente se pueden ver los números de cada jugador, sino que también se puede tener una idea general de quién tuvo el mejor partido.

Este proyecto también me parece una buena forma de utilizar lo que voy aprendiendo en programación, ya que más adelante espero poder utilizar funciones, condicionales, ciclos, variables y operaciones matemáticas para hacer que el programa sea cada vez más completo.

## Descripción

Este programa consiste en desarrollar un programa en Python para calcular el desempeño de jugadores de baloncesto a partir de diferentes estadísticas obtenidas durante el partido.

El programa asigna un valor diferente a cada estadística y utiliza estos valores para calcular una puntuación de desempeño. Después de obtener la estadísticas de cada uno de los parámetros se convierten en un puntuación del 1 al 10.

El proyecto tiene objetivo aplicar conocimientos básicos de programación tales como:

Variables y constantes.
Funciones.
Parámetros.
Condicionales.
Ciclos while.
Validación de datos.
Operaciones matemáticas.
Programación modular.
Listas para almacenar la información de varios jugadores.
Ciclos for para recorrer las estadísticas de los jugadores.
Comparación de resultados.
Cálculo de promedios y sumas.

## Estadísticas Utilizadas

Actualmente el programa tiene las siguientes estadísticas

Estadística	        Valor asignado
Punto	              1
Asistencia	        0.8
Rebote	           0.5
Robo	              1.5
Pase fallido	     -2
Triple	           3
Pérdida de balón	  -1.5
Tapón	              2
Falta	              -3


Estos valores se utilizan dentro del programa como constantes, para calcular la puntuación de desempeño de cada jugador

## Función Actual

El programa tiene varias funciones para hacer pequeñas tareas especificas

pedir_dato()

Solicita un dato al usuario y verifica que sea un numero entero no negativo

Si el usuario introduce un numero incorrecto, el programa muestra un mensaje de error y vuelve a solicitar un dato hasta recibir un dato válido.

obtener_estadisticas()

solicita las estadísticas del jugador utilizando la función pedir_dato

Actualmente solicita:

Puntos.
Asistencias.
Rebotes.
Robos.
Pases fallidos.
Puntos de 3.
Pérdidas de balón.
Tiros bloqueados.
Faltas cometidas.


calcular desempeño()

Utiliza las estadísticas y los valores asignados a cada una para obtener la puntuación de desempeño del jugador

Las estadísticas positivas ayudan a obtener una mejor puntuación y las negativas lo contrario

obtener_calificacion()

Convierte la puntuación de desempeño del 1 al 10 mediante condiciones.

La escala utilizada es: 

Puntuación	   Calificación
30 o más	      10
20 a 29	      8
10 a 19	      6
0 a 9	         4
Menor que 0	   1


mostrar_resultado()

Muestra el nombre del jugador, su puntuación y calificación del desempeño del jugador

calcular_promedio_equipo()

Calcula el promedio de las puntuaciones de desempeño de los jugadores registrados, para llegar a eso se suma las puntuaciones de los jugadores y divide el resultado entre la cantidad de jugadores evaluados.

calcular_puntos_totales()

Calcula el total de puntos anotados por los jugadores registrados, para llegar a eso recorre las estadísticas almacenadas de cada jugador y suma los puntos anotados.

## Estructura del Repositorio

El repositorio tiene los siguientes archivos:

Archivo	           Descripción

proyecto.py	        Contiene el código principal del proyecto, las constantes, las funciones y la lógica que se está 
                    desarrollando para calcular el desempeño de los jugadores.

README.md	        Contiene la descripción del proyecto, su funcionamiento, estructura, estadísticas utilizadas e
                    e instrucciones para ejecutarlo.

LICENSE	           Contiene la licencia MIT del proyecto y establece las condiciones para utilizar y distribuir el código.

.gitignore	        Indica a Git qué archivos y carpetas debe ignorar para evitar subir archivos innecesarios al repositorio.


## ¿Qué se necesita para que funcione?

Para ejecutar el proyecto se necesita.

Python 3 instalado.
Un editor de código o terminal para ejecutar el programa.
No se requieren librerías externas.


## ¿Cómo ejecutar el proyecto?

1. Clonar el repositorio

Si se utiliza Git, clonar el repositorio:

git clone URL_DEL_REPOSITORIO

Después, entrar a la carpeta del proyecto:

cd NOMBRE_DEL_REPOSITORIO

2. Ejecutar el programa

Ejecutar el archivo principal:

python proyecto.py

En algunos sistemas puede ser necesario utilizar:

python3 proyecto.py


## Estado actual del proyecto

El proyecto se encuentra actualmente en desarrollo.

Hasta este punto se han implementado:

Las constantes correspondientes al valor de cada estadística.
Una función para solicitar y validar datos.
Una función para obtener las estadísticas de un jugador.
Una función para calcular el desempeño.
Una función para convertir el desempeño en una calificación.
Una función para mostrar los resultados.
La posibilidad de seleccionar la cantidad de jugadores que se van a evaluar, siendo el mínimo 1 y el máximo 5.
El almacenamiento de los nombres de los jugadores.
El almacenamiento de las estadísticas, puntuaciones y calificaciones mediante listas.
Un ciclo para solicitar y procesar la información de cada jugador.
La comparación de las puntuaciones para identificar al jugador con mejor desempeño.
El cálculo del promedio de desempeño del equipo.
El cálculo de los puntos totales anotados por los jugadores.
La opción de realizar una nueva evaluación o finalizar el programa.


## Próximos pasos

La siguiente etapa del proyecto consiste en continuar mejorando el programa para:

Mejorar la presentación de los resultados.
Agregar nuevas funcionalidades que permitan analizar el desempeño de los jugadores.
Continuar desarrollando el proyecto conforme a los conocimientos adquiridos en programación.


## Licencia

Este proyecto utiliza la licencia MIT. Para consultar los términos completos, revisar el archivo LICENSE.


## Algoritmo

1. Iniciar el programa.

2. Mostrar una bienvenida al usuario.

3. Definir los valores constantes de cada estadística

Punto = 1
Asistencia = 0.8
Rebote = 0.5
Robo = 1.5
Pase fallido = -2
Triple = 3
Pérdida de balón = -1.5
Tapón = 2
Falta = -3

4. Solicitar los datos de los jugadores que desea evaluar, con un mínimo de 1 y un máximo de 5.

5. Validar que la cantidad de jugadores ingresada se encuentre dentro del rango permitido. Si el dato es incorrecto, solicitarlo nuevamente.

6. Crear las listas para almacenar los nombres, las estadísticas, las puntuaciones y las calificaciones de los jugadores

7. Solicitar el nombre de cada jugador.

8. Solicitar las estadísticas de cada jugador mediante la función obtener_estadisticas().

9. Validar cada dato ingresado

Verificar que sea un número entero.
Verificar que no sea negativo.
Si el dato es incorrecto, mostrar un mensaje de error y solicitarlo nuevamente.

10. Calcular la puntuación de desempeño de cada jugador utilizando el valor correspondiente de cada estadística.

Valor_Punto = 1
Valor_Asistencias = 0.8
Valor_Rebotes = 0.5
Valor_Robos = 1.5
Valor_Pase_Fallido = -2
Valor_Triple = 3
Valor_Perdidas = -1.5
Valor_Tapones = 2
Valor_Faltas = -3

11. Convertir la puntuación de desempeño en una calificación del 1 al 10 mediante condiciones.

12. Guardar la información correspondiente de cada jugador en las listas correspondientes.

13. Mostrar el nombre, la puntuación y la calificación de cada jugador.

14. Comparar las puntuaciones con los jugadores registrados.

15. Identificar al jugador con el mejor desempeño.

16. Mostrar al jugador con mayor puntuación y su calificación.

17. Calcular el promedio de las puntuaciones de desempeño de los jugadores registrados.

18. Calcular los puntos totales anotados por todos los jugadores registrados.

19. Mostrar el promedio de desempeño del equipo y los puntos totales anotados.

20. Preguntar al usuario si quiere realizar otra evaluación.

21. Si el usuario desea realizar otra evaluación, regresar al proceso de registro de jugadores.

22. Si el usuario no desea realizar otra evaluación, finalizar el programa.