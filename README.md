# Avance_Proyecto_1_Basquetbol

# Estadísticas de jugadores de básquetbol

# Contexto

Escogí el tema del básquetbol porque es un deporte que me gusta mucho y que considero muy interesante, no solamente por jugarlo, sino también por todo lo que pasa dentro de un partido. Me gusta la emoción de los partidos, las jugadas, los tiros de tres, las asistencias y la forma en la que cada jugador puede aportar algo diferente a su equipo. Además, creo que el básquetbol es un deporte en el que las estadísticas tienen mucha importancia, ya que muchas veces sirven para saber qué tan bien jugó una persona y qué fue lo que aportó durante el partido.

Por eso, en este proyecto quise desarrollar un programa que permita registrar y calcular las estadísticas de hasta 5 jugadores de básquetbol durante un partido. Algunas de las estadísticas que se van a tomar en cuenta son los puntos, asistencias, rebotes, robos, pases fallidos, puntos de tres y pérdidas de balón. Al final, el programa utilizará estos datos para obtener una puntuación del desempeño de cada jugador del 1 al 10, siendo 10 la mejor calificación.

¿Por qué es interesante?

Elegí este tema porque el básquetbol es uno de mis deportes favoritos y me parece interesante intentar utilizar la programación para analizar algo que normalmente podemos ver durante un partido. Muchas veces cuando vemos un juego nos damos cuenta de que un jugador tuvo un buen partido porque anotó muchos puntos, pero también existen otras cosas importantes como las asistencias, los rebotes, los robos o incluso los errores que tuvo.

Además, considero interesante que el programa pueda tomar todas estas estadísticas y convertirlas en una calificación sencilla que permita comparar el desempeño de los 5 jugadores. De esta manera, no solamente se pueden ver los números de cada jugador, sino que también se puede tener una idea general de quién tuvo el mejor partido.

Este proyecto también me parece una buena forma de utilizar lo que voy aprendiendo en programación, ya que más adelante espero poder utilizar funciones, condicionales, ciclos, variables y operaciones matemáticas para hacer que el programa sea cada vez más completo.

## Descripción

Este programa consiste en desarrollar un programa en Python para calcular el desempeño de jugadores de baloncesto a partir de diferentes estadísticas obtenidas durante el partido.

El programa asigna un valor diferente a cada estadística y utiliza estos valores para calcular una puntuación de desempeño. Después de obtener las estadísticas de cada jugador, el programa calcula una puntuación de desempeño utilizando los valores asignados a cada estadística. Posteriormente, convierte esa puntuación en una calificación del 1 al 10.

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

## Funciones Actualizadas

## Funciones actuales

El programa cuenta con las siguientes funciones:

1. pedir_dato(mensaje): Solicita un dato al usuario y valida que sea un número entero no negativo.

2. pedir_cantidad_jugadores(): Solicita la cantidad de jugadores que se van a evaluar y valida que sea entre 1 y 5.

3. manipular_nombre(nombre): Realiza diferentes operaciones con el nombre del jugador, como obtener su longitud, dividirlo en partes y cambiarlo a mayúsculas o minúsculas.

4. obtener_estadisticas(): Solicita las nueve estadísticas de cada jugador y utiliza la función pedir_dato() para validar los datos.

5. calcular_desempeno(...): Calcula la puntuación de desempeño de cada jugador utilizando los valores establecidos para las estadísticas.

6. obtener_calificacion(puntuacion): Convierte la puntuación de desempeño en una calificación del 1 al 10.

7. registrar_jugadores(cantidad_jugadores): Registra los nombres y las estadísticas de los jugadores, y almacena sus puntuaciones y calificaciones.

8. calcular_promedio_equipo(puntuaciones): Calcula el promedio de desempeño de todos los jugadores del equipo.

9. calcular_puntos_totales(estadisticas_jugadores): Calcula la cantidad total de puntos anotados por todos los jugadores.

10. calcular_promedios_estadisticas(matriz): Calcula el promedio de cada estadística utilizando los datos almacenados en una matriz o lista anidada.

11. encontrar_mejor_jugador(puntuaciones): Identifica la posición del jugador que obtuvo la puntuación más alta.

12. mostrar_resultado(nombre, puntuacion, calificacion): Muestra el nombre, la puntuación y la calificación de un jugador.

13. mostrar_resultados_jugadores(nombres, puntuaciones, calificaciones): Muestra los resultados individuales de todos los jugadores.

14. mostrar_mejor_jugador(nombres, puntuaciones, calificaciones): Muestra al jugador con el mejor desempeño y su puntuación.

15. mostrar_promedios_estadisticas(estadisticas_jugadores): Muestra el promedio de cada una de las estadísticas del equipo.

16. mostrar_resultados_equipo(cantidad_jugadores, puntuaciones, estadisticas_jugadores): Muestra los resultados generales del equipo, incluyendo la cantidad de jugadores, los puntos totales y los promedios.

17. preguntar_continuar(): Pregunta al usuario si desea realizar otra evaluación o finalizar el programa.

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
Una función para solicitar y validar datos ingresados por el usuario.
La posibilidad de seleccionar la cantidad de jugadores que se van a evaluar, siendo el mínimo 1 y el máximo 5.
Una función para manipular y mostrar diferentes partes del nombre de cada jugador.
Una función para obtener las nueve estadísticas de cada jugador.
El almacenamiento de los nombres de los jugadores.
El almacenamiento de las estadísticas mediante listas anidadas.
El cálculo de la puntuación de desempeño de cada jugador.
La conversión de la puntuación en una calificación del 1 al 10.
El almacenamiento de las puntuaciones y calificaciones de los jugadores.
El cálculo de los puntos totales anotados por los jugadores.
El cálculo del promedio de desempeño del equipo.
El cálculo del promedio de cada estadística de todos los jugadores.
La comparación de las puntuaciones para identificar al jugador con mejor desempeño.
La presentación de los resultados individuales de cada jugador.
La presentación de los resultados generales del equipo.
La opción de realizar una nueva evaluación o finalizar el programa.

## Próximos pasos

La siguiente etapa del proyecto consiste en continuar mejorando el programa para:

Mejorar la presentación visual de los resultados.
Incorporar nuevas estadísticas que permitan analizar el desempeño de los jugadores.
Ampliar las funcionalidades para realizar un análisis más completo del equipo.
Continuar desarrollando el proyecto conforme a los conocimientos adquiridos en programación


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

8. Mostrar y manipular diferentes partes del nombre del jugador, utilizando operaciones con cadenas de texto.

9. Solicitar las estadísticas de cada jugador mediante la función obtener_estadisticas().

10. Validar cada dato ingresado

Verificar que sea un número entero.
Verificar que no sea negativo.
Si el dato es incorrecto, mostrar un mensaje de error y solicitarlo nuevamente.

11. Calcular la puntuación de desempeño de cada jugador utilizando el valor correspondiente de cada estadística.

12. Convertir la puntuación de desempeño en una calificación del 1 al 10 mediante condiciones.

13. Guardar la información correspondiente de cada jugador en las listas correspondientes.

14. Mostrar el nombre, la puntuación y la calificación de cada jugador.

15. Comparar las puntuaciones de los jugadores registrados.

16. Identificar al jugador con el mejor desempeño.

17. Mostrar al jugador con mayor puntuación y su calificación.

18. Calcular el promedio de las puntuaciones de desempeño de los jugadores registrados.

19. Calcular los puntos totales anotados por todos los jugadores registrados.

20. Calcular el promedio de cada estadística de todos los jugadores utilizando una matriz o lista anidada.

21. Mostrar los promedios de cada estadística del equipo.

22. Mostrar los resultados generales del equipo, incluyendo la cantidad de jugadores, los puntos totales y el promedio de desempeño.

Al finalizar:

23. Preguntar al usuario si desea realizar otra evaluación.

24. El usuario desea realizar otra evaluación, regresar al proceso de registro de jugadores.

25. Si el usuario no desea realizar otra evaluación, finalizar el programa.