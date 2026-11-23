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

Este programa está desarrollado en Python y permite calcular el desempeño de entre 1 y 5 jugadores de básquetbol a partir de nueve estadísticas obtenidas durante un partido.

Al iniciar, el usuario puede elegir entre dos formas de registrar a los jugadores:

    1. Registro manual: ingresar los nombres y las estadísticas de cada jugador directamente en el programa. Al terminar la evaluación, el usuario puede guardar las estadísticas y los resultados en un archivo de texto (.txt), escribiendo el nombre que desea utilizar.</span>

    2. Registro mediante archivo: leer los nombres y las estadísticas desde un archivo de texto externo. El usuario puede escribir el nombre del archivo que desea utilizar, por lo que no es necesario que tenga un nombre específico.

El programa valida la información ingresada o leída desde el archivo. Los nombres deben contener únicamente letras y espacios, y no pueden superar los 30 caracteres. Las estadísticas deben ser números enteros entre 0 y 99.

Después de obtener los datos, el programa calcula la puntuación de desempeño de cada jugador mediante los valores asignados a las estadísticas. Posteriormente, convierte esa puntuación en una calificación del 1 al 10.

Finalmente, muestra los resultados individuales, identifica al jugador con mejor desempeño y presenta los resultados generales del equipo, incluyendo los puntos totales y el promedio de cada estadística. Cuando el registro se realiza manualmente, también permite guardar las estadísticas y los resultados en un archivo de texto (.txt) con el nombre que el usuario elija.

El proyecto tiene objetivo aplicar conocimientos básicos de programación tales como:

Variables y constantes.
Tipos de datos y operaciones aritméticas.
Funciones y modularización del código.
Paso de parámetros y retorno de valores.
Condicionales (if, elif, else).
Ciclos (while y for).
Listas y listas anidadas.
Manipulación y validación de cadenas de texto.
Validación de datos mediante try y except.
Lectura y procesamiento de archivos externos.
Uso de métodos y funciones integradas de Python.

## Estadísticas Utilizadas

Actualmente el programa tiene las siguientes estadísticas

Estadística	        Valor asignado
Punto	            1
Asistencia	        0.8
Rebote	            0.5
Robo	            1.5
Pase fallido	    -2
Triple	            3
Pérdida de balón	-1.5
Tapón	            2
Falta	            -3


Estos valores se utilizan dentro del programa como constantes, para calcular la puntuación de desempeño de cada jugador


## Funciones Actuales

El programa cuenta con las siguientes 22 funciones:

1. pedir_dato(mensaje): solicita una estadística al usuario y valida que sea un número entero entre 0 y 99. Si el dato no es válido, vuelve a solicitarlo.

2. normalizar_nombre(nombre): elimina espacios innecesarios al inicio y al final, reduce los espacios repetidos entre palabras y organiza las mayúsculas del nombre.

3. validar_nombre(nombre): verifica que el nombre no esté vacío, que no supere los 30 caracteres y que contenga únicamente letras y espacios.

4. pedir_nombre(): solicita el nombre del jugador, lo normaliza y utiliza la función validar_nombre() para comprobar que sea válido.

5. pedir_cantidad_jugadores(): Solicita la cantidad de jugadores que se van a evaluar y valida que sea entre 1 y 5.

6. obtener_estadisticas(): Solicita las nueve estadísticas de cada jugador y utiliza la función pedir_dato() para validar los datos.

7. calcular_desempeno(...): Calcula la puntuación de desempeño de cada jugador utilizando los valores establecidos para las estadísticas.

8. obtener_calificacion(puntuacion): Convierte la puntuación de desempeño en una calificación del 1 al 10.

9. leer_jugadores_archivo(nombre_archivo): abre y lee un archivo de texto externo cuyo nombre proporciona el usuario. Separa los datos de cada jugador, normaliza y valida los nombres, verifica que las estadísticas sean números enteros entre 0 y 99 y calcula las puntuaciones y calificaciones. También comprueba que el archivo tenga como máximo cinco jugadores y que contenga información válida.

10. registrar_jugadores(cantidad_jugadores): Registra los nombres y las estadísticas de los jugadores, y almacena sus puntuaciones y calificaciones.

11. calcular_promedio_equipo(puntuaciones): Calcula el promedio de desempeño de todos los jugadores del equipo.

12. calcular_puntos_totales(estadisticas_jugadores): Calcula la cantidad total de puntos anotados por todos los jugadores.

13. calcular_promedios_estadisticas(matriz): Calcula el promedio de cada estadística utilizando los datos almacenados en una matriz o lista anidada.

14. encontrar_mejor_jugador(puntuaciones): Identifica la posición del jugador que obtuvo la puntuación más alta.

15. mostrar_resultado(nombre, puntuacion, calificacion): Muestra el nombre, la puntuación y la calificación de un jugador.

16. mostrar_resultados_jugadores(nombres, puntuaciones, calificaciones): Muestra los resultados individuales de todos los jugadores.

17. mostrar_mejor_jugador(nombres, puntuaciones, calificaciones): Muestra al jugador con el mejor desempeño y su puntuación.

18. mostrar_promedios_estadisticas(estadisticas_jugadores): Muestra el promedio de cada una de las estadísticas del equipo.

19. mostrar_resultados_equipo(cantidad_jugadores, puntuaciones, estadisticas_jugadores): Muestra los resultados generales del equipo, incluyendo la cantidad de jugadores, los puntos totales y los promedios.

20. guardar_resultados_archivo (nombres, estadisticas_jugadores, puntuaciones, calificaciones): solicita al usuario el nombre que desea asignar al documento y guarda en un archivo .txt las estadísticas de cada jugador, sus puntuaciones y calificaciones, además de los resultados generales, el mejor jugador y los promedios del equipo. Se utiliza cuando el registro se realiza manualmente.

21. preguntar_continuar(): pregunta al usuario si desea realizar otra evaluación o finalizar el programa. Valida que la respuesta sea "si" o "no".

22. pedir_modo_registro(): permite elegir entre registrar los datos manualmente o leerlos desde un archivo externo. Valida que la opción seleccionada sea 1 o 2.

23. main(): coordina la ejecución del programa. Muestra el menú, solicita el modo de registro, obtiene los datos, presenta los resultados y permite realizar otra evaluación.

# Registro mediante archivo externo

Además del registro manual, el programa permite obtener la información de los jugadores desde cualquier archivo de texto externo que cumpla con el formato establecido.

Para utilizar esta opción, el programa solicita al usuario que escriba el nombre del archivo de estadísticas que desea utilizar. Por ejemplo:

estadisticas_equipo.txt

No es obligatorio que el archivo tenga un nombre específico. El usuario puede utilizar su propio documento, siempre que esté disponible en la ubicación desde la que se ejecuta el programa y respete el formato requerido.

Cada línea del archivo debe contener el nombre del jugador y sus nueve estadísticas, separados por comas. Por lo tanto, cada línea debe tener exactamente diez datos: un nombre y nueve números.

Ejemplo del formato:

Carlos Ruiz,18,5,7,2,1,3,2,1,2
Miguel Torres,22,4,6,3,2,2,1,2,1
Daniel Herrera,15,7,8,1,0,4,3,3,2
Andres Morales,12,3,5,2,1,1,2,1,3
Luis Fernandez,20,6,4,2,0,3,1,2,1

El archivo puede tener cualquier nombre, pero debe contener la información con el orden y formato indicados.

Al leer el archivo, el programa comprueba que:

    1.Cada línea tenga diez datos separados por comas.

    2.El nombre sea válido y no supere los 30 caracteres.

    3.Las nueve estadísticas sean números enteros entre 0 y 99.

    4.El archivo no contenga más de cinco jugadores.

    5.El archivo contenga al menos un jugador.

Si el archivo no existe o contiene información inválida, el programa muestra un mensaje de error y regresa al menú para que el usuario pueda volver a elegir cómo registrar los datos.

# Archivo de ejemplo

El repositorio incluye el archivo `datos_ejemplo.txt`, que contiene estadísticas de cinco jugadores y permite probar la funcionalidad de lectura de archivos externos.

El usuario puede utilizar este archivo para comprobar el funcionamiento del programa o utilizar uno propio, siempre que respete el formato y la estructura de datos establecidos. Este archivo se utiliza para leer estadísticas; es diferente del documento .txt que el programa puede generar al guardar una evaluación manual.

Para probarlo:

1. Descarga el archivo `datos_ejemplo.txt` del repositorio.
2. Ejecuta el programa.
3. Selecciona la opción de leer los datos desde un archivo.
4. Ingresa `datos_ejemplo.txt` cuando el programa solicite el nombre del archivo.
5. El programa procesará la información y mostrará los resultados.

## Resultados que muestra el programa

Después de registrar o leer los datos, el programa presenta:

    1.Los nombres, puntuaciones y calificaciones individuales de los jugadores.

    2.El jugador que obtuvo la puntuación de desempeño más alta.

    3.La cantidad de jugadores registrados.

    4.Los puntos totales anotados por el equipo.

    5.El promedio de desempeño del equipo.

    6.El promedio de cada una de las nueve estadísticas

Cuando los datos se ingresan manualmente, el programa también permite guardar las estadísticas y los resultados de la evaluación en un archivo .txt con el nombre que proporcione el usuario.

### Estructura del Repositorio

El repositorio tiene los siguientes archivos:

Archivo	           Descripción

proyecto.py	        Contiene el código principal del proyecto, las constantes, las funciones y la lógica que se está 
                    desarrollando para calcular el desempeño de los jugadores.

README.md	        Contiene la descripción del proyecto, su funcionamiento, estructura, estadísticas utilizadas e
                    e instrucciones para ejecutarlo.

LICENSE	           Contiene la licencia MIT del proyecto y establece las condiciones para utilizar y distribuir el código.

.gitignore	        Indica a Git qué archivos y carpetas debe ignorar para evitar subir archivos innecesarios al repositorio.


Nota: Los archivos de estadísticas son documentos externos que proporciona el usuario. No es obligatorio incluir un archivo específico dentro del repositorio, ya que el programa permite escribir el nombre del documento que se desea utilizar. Además, cuando se realiza un registro manual, el programa puede crear un archivo .txt nuevo con las estadísticas y los resultados de esa evaluación

## ¿Qué se necesita para que funcione?

Para ejecutar el proyecto se necesita.

Python 3 instalado.
Un editor de código o terminal para ejecutar el programa.
No se requieren librerías externas.

Para utilizar la opción de registro mediante archivo también se necesita tener un archivo de texto con las estadísticas de los jugadores, siguiendo el formato indicado anteriormente.

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

3. Elegir el modo de registro

Al iniciar el programa, aparecerá un menú con dos opciones:

Ingresar los datos manualmente.

Leer los datos desde un archivo.

El usuario debe seleccionar la opción deseada. Después, el programa solicitará o leerá la información y mostrará los resultados. Si selecciona el registro manual, al finalizar podrá escribir el nombre con el que desea guardar un documento .txt con la evaluación.

Si se selecciona la segunda opción, el programa solicitará el nombre del archivo de estadísticas que se desea utilizar.

Por ejemplo:

Escribe el nombre de tu archivo de estadísticas: estadisticas_equipo.txt

El usuario puede escribir el nombre de su propio archivo, sin necesidad de cambiar el código del programa.

# Validaciones del programa

Para evitar errores durante la ejecución, el programa valida los datos de las siguientes maneras:

    1.Estadísticas: deben ser números enteros entre 0 y 99.

    2.Cantidad de jugadores: debe ser un número entero entre 1 y 5.

    3.Nombres: no pueden estar vacíos, deben tener un máximo de 30 caracteres y solo pueden contener letras y espacios.

    4.Modo de registro: únicamente se aceptan las opciones 1 y 2.

    5.Continuar o finalizar: únicamente se aceptan las respuestas "si" o "no".

    6.Archivo externo: debe existir, contener al menos un jugador y tener el formato correcto. Cada jugador debe tener un nombre y nueve estadísticas.

Cuando un dato ingresado manualmente no cumple con las condiciones, el programa muestra un mensaje de error y vuelve a solicitarlo. Si el archivo contiene información inválida, muestra el error correspondiente y permite regresar al menú.

## Estado actual del proyecto

El proyecto cuenta con las siguientes funcionalidades:

1. Definición de constantes para asignar un valor a cada estadística.
2. Registro manual de entre 1 y 5 jugadores.
3. Registro de jugadores mediante un archivo de texto externo.
4. Posibilidad de utilizar archivos de estadísticas con nombres personalizados.
5. Solicitud y validación de nombres.
6. Normalización de nombres para eliminar espacios innecesarios y organizar las mayúsculas.
7. Solicitud y validación de las nueve estadísticas de cada jugador.
8. Validación de números enteros dentro del rango de 0 a 99.
9. Almacenamiento de nombres y estadísticas mediante listas y listas anidadas.
10. Cálculo de la puntuación de desempeño de cada jugador.
11. Conversión de la puntuación en una calificación del 1 al 10.
12. Cálculo de los puntos totales anotados por el equipo.
13. Cálculo del promedio de desempeño del equipo.
14. Cálculo del promedio de cada estadística de todos los jugadores.
15. Comparación de las puntuaciones para identificar al jugador con mejor desempeño.
16. Presentación de los resultados individuales.
17. Presentación de los resultados generales del equipo.
18. Opción para realizar una nueva evaluación o finalizar el programa.
19. Validación de la información obtenida desde el archivo externo.
20. Creación de un archivo .txt con nombre personalizado para guardar las estadísticas y los resultados cuando el registro se realiza manualmente.

# Próximos pasos

La siguiente etapa del proyecto consiste en continuar mejorando el programa para:

Mejorar la presentación visual de los resultados.
Incorporar nuevas estadísticas que permitan analizar el desempeño de los jugadores.
Ampliar las funcionalidades para realizar un análisis más completo del equipo.
Continuar desarrollando el proyecto conforme a los conocimientos adquiridos en programación


## Licencia

Este proyecto utiliza la licencia MIT. Para consultar los términos completos, revisar el archivo LICENSE.


### Algoritmo

Iniciar el programa.

1. Mostrar un mensaje de bienvenida.
2. Mostrar el menú para elegir el modo de registro:

3. Ingresar los datos manualmente.
    Leer los datos desde un archivo externo.
    Validar que la opción seleccionada sea 1 o 2. Si es incorrecta, solicitarla nuevamente.

4. Si el usuario elige el registro manual:
    Solicitar la cantidad de jugadores.
    Validar que sea un número entero entre 1 y 5.
    Solicitar el nombre de cada jugador.
    Normalizar y validar cada nombre.
    Solicitar las nueve estadísticas de cada jugador.
    Validar que cada estadística sea un número entero entre 0 y 99.
    Guardar los nombres y las estadísticas en las listas correspondientes.

6. Si el usuario elige el registro mediante archivo:
    Solicitar el nombre del archivo de estadísticas que desea utilizar.
    Abrir el archivo indicado por el usuario.
    Leer cada línea y separar sus datos mediante comas.
    Comprobar que cada jugador tenga un nombre y nueve estadísticas.
    Normalizar y validar el nombre.
    Convertir las estadísticas a números enteros y validar que estén entre 0 y 99.
    Comprobar que el archivo contenga entre 1 y 5 jugadores.
    Guardar los datos válidos en las listas correspondientes.
    Si ocurre un error, mostrar un mensaje y regresar al menú.

7. Calcular la puntuación de desempeño de cada jugador utilizando los valores asignados a las nueve estadísticas.
8. Convertir cada puntuación en una calificación del 1 al 10 mediante condiciones.
9. Mostrar el nombre, la puntuación y la calificación de cada jugador.
10. Comparar las puntuaciones e identificar al jugador con el mejor desempeño.
11. Mostrar al jugador con mayor puntuación y su calificación.
12. Calcular el promedio de desempeño de todos los jugadores.
13. Calcular los puntos totales anotados por el equipo.
14. Calcular el promedio de cada una de las nueve estadísticas utilizando la lista anidada.
15. Mostrar los resultados generales del equipo y los promedios de sus estadísticas.
16. Si el registro fue manual, solicitar al usuario un nombre para el documento y guardar en un archivo .txt las estadísticas, puntuaciones, calificaciones y resultados generales, incluyendo el mejor jugador y los promedios.
17. Preguntar al usuario si desea realizar otra evaluación.
18. Si responde "si", regresar al menú de registro.
19. Si responde "no", finalizar el programa.