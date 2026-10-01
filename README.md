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

La escala utilizada actualizada es: 

Puntuación	   Calificación
30 o más	      10
20 a 29	      8
10 a 19	      6
0 a 9	         4
Menor que 0	   1


mostrar_resultado()

Muestra el nombre del jugador, su puntuación y calificación del desempeño del jugador

## Estructura del Repositorio

El repositorio tiene los siguientes archivos:

Archivo	           Descripción

primercodigo.py	  Contiene el código principal del proyecto, las constantes, las funciones y la lógica que se está 
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

python primercodigo.py

En algunos sistemas puede ser necesario utilizar:

python3 primercodigo.py


## Estado actual del proyecto

El proyecto se encuentra actualmente en desarrollo.

Hasta este punto se han implementado:

Las constantes correspondientes al valor de cada estadística.
Una función para solicitar y validar datos.
Una función para obtener las estadísticas de un jugador.
Una función para calcular el desempeño.
Una función para convertir el desempeño en una calificación.
Una función para mostrar los resultados.
La estructura inicial de un ciclo while para trabajar con varios jugadores.


## Próximos pasos

La siguiente etapa del proyecto consiste en completar la lógica para:

Registrar correctamente a los 5 jugadores.
Almacenar la información de cada jugador.
Mostrar los resultados de los 5 jugadores.
Comparar sus puntuaciones.
Identificar al jugador con mayor desempeño.
Permitir realizar una nueva búsqueda o finalizar el programa.


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

4. Solicitar los datos de cada jugador.

5. Validar cada dato ingresado:

Verificar que sea un número entero.
Verificar que no sea negativo.
Si el dato es incorrecto, mostrar un mensaje de error y solicitarlo nuevamente.

6. Obtener las estadísticas de cada jugador, del partido:

   * Puntos.
   * Asistencias.
   * Rebotes.
   * Robos.
   * Pases fallidos.
   * Puntos de tres.
   * Pérdidas de balón.
   * Tapones
   * Faltas


7. Calcular la puntuación de desempeño de cada jugador utilizando el valor correspondiente de cada estadística.

8. Convertir la puntuación de desempeño en una calificación del 1 al 10 mediante condiciones.

9. Mostrar el nombre, puntuación y calificación de cada jugador.

10. Repetir el proceso mediante un ciclo while hasta registrar los 5 jugadores.

11. Guardar la información de los jugadores para poder utilizarla posteriormente.

12. Comparar las puntuaciones de los 5 jugadores.

13. Identificar al jugador con la puntuación de desempeño más alta.

14. Mostrar el jugador con mayor puntuación y su calificación.

15. Preguntar al usuario si desea realizar otra búsqueda.

16. Si el usuario desea realizar otra búsqueda, regresar al proceso de registro.

17. Si el usuario no desea realizar otra búsqueda, finalizar el programa.
