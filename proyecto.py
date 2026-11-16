#Encabezado --------------------------------------------------------------------

"""
Este proyecto esta echo por José Alberto Juárez Palazuelos
Este Programa es para calcular el desempeño de un jugador de baloncesto
O hasta el desempeño de todo un equipo de 5 personas
"""

#1. Importaciones ---------------------------------------------------------------


#2. Variables globales y Constantes ---------------------------------------------

#Constantes para calcular el desempeño del jugador
VALOR_PUNTO = 1
VALOR_ASISTENCIAS = 0.8
VALOR_REBOTES = 0.5
VALOR_ROBOS = 1.5
VALOR_PASE_FALLIDO = -2
VALOR_TRIPLE = 3
VALOR_PERDIDAS = -1.5
VALOR_TAPONES = 2
VALOR_FALTAS = -3

nombres_estadisticas = ["Puntos", "Asistencias", "Rebotes", "Robos",
    "Pases fallidos", "Puntos de 3", "Perdidas", "Tapones", "Faltas"]

#3. Funciones ---------------------------------------------------------------------


# Función para pedir y validar datos de los jugadores

def pedir_dato(mensaje):
    """Pide un dato al usuario y valida que no sea un numero entero negativo"""
    while True:
        try:
            entrada = input(mensaje).strip()

            dato = int(entrada)

            if dato < 0 or dato > 99:
                print("Error: el valor debe estar entre 0 y 99.")

            elif entrada.count(".") > 1:
                print("Error: formato numérico invalido.")

            else:
                return dato

        except ValueError:
            print("Error: debes ingresar un numero valido.")


# Función para solicitar y validar el nombre del jugador.

def pedir_nombre():
    """Solicita un nombre de máximo 30 caracteres y valida que solo tenga letras y espacios."""

    while True:
        nombre = input("Nombre del jugador: ").strip()

        if len(nombre) == 0:
            print("Error: el nombre no puede estar vacío.")

        elif len(nombre) > 30:
            print("Error: el nombre no puede superar los 30 caracteres.")

        #isalpha() Comprueba que cada carácter sea una letra, incluyendo letras con acentos.
        #isspace() Permite utilizar espacios.
        elif not all(letra.isalpha() or letra.isspace()
                    for letra in nombre):
            print("Error: el nombre solo puede contener letras y espacios.")

        else:
            return nombre


# Función para pedir la cantidad de jugadores

def pedir_cantidad_jugadores():
    """Solicita y valida la cantidad de jugadores a evaluar"""

    while True:
        try:
            cantidad = int(
                input("¿Cuantos jugadores deseas evaluar? (1-5): ")
            )

            if 1 <= cantidad <= 5:
                return cantidad

            print("Error: debes ingresar un numero del 1 al 5.")

        except ValueError:
            print("Error: debes ingresar un numero entero.")


# Función para manipular cadenas de texto

def manipular_nombre(nombre):
    """Muestra y manipula diferentes partes del nombre del jugador."""

    print("\n--- Información del nombre del jugador ---")

    # Muestra el nombre y sus caracteres
    print("Nombre:", nombre)
    print("Primer carácter:", nombre[0])
    print("Tamaño del nombre:", len(nombre))

    # Muestra una parte del nombre
    print("Primeras 5 letras:", nombre[0:5])

    # Convierte el nombre a mayúsculas y minúsculas
    print("Nombre en mayúsculas:", nombre.upper())
    print("Nombre en minúsculas:", nombre.lower())

    # Separa el nombre y los apellidos
    palabras = nombre.split()
    print("Nombre separado:", palabras)


# Función para obtener estadísticas de cada jugador

def obtener_estadisticas():
    """Solicita estadísticas a evaluar de cada jugador"""
    puntos = pedir_dato("Puntos: ")
    asistencias = pedir_dato("Asistencias: ")
    rebotes = pedir_dato("Rebotes: ")
    robos = pedir_dato("Robos: ")
    pase_fallido = pedir_dato("Pases fallidos: ")
    puntos_tres = pedir_dato("Puntos de 3: ")
    perdidas = pedir_dato("Perdidas de balón: ")
    tapones = pedir_dato("Tiros bloqueados: ")
    faltas = pedir_dato("Faltas cometidas: ")

    return [puntos, asistencias, rebotes, 
            robos, pase_fallido, puntos_tres, 
            perdidas, tapones, faltas]


# Función para calcular el desempeño de cada jugador

def calcular_desempeno(puntos, asistencias, rebotes, 
                    robos, pase_fallido, puntos_tres, 
                    perdidas, tapones, faltas):

    """Calculo de la puntuación de desempeño del jugador"""

    puntuacion = (puntos * VALOR_PUNTO 
                    + asistencias * VALOR_ASISTENCIAS 
                    + rebotes * VALOR_REBOTES 
                    + robos * VALOR_ROBOS 
                    + puntos_tres * VALOR_TRIPLE 
                    + pase_fallido * VALOR_PASE_FALLIDO
                    + perdidas * VALOR_PERDIDAS 
                    + tapones * VALOR_TAPONES 
                    + faltas * VALOR_FALTAS)

    return puntuacion


# Función para obtener calificación de cada jugador

def obtener_calificacion(puntuacion):
    """Convierte la calificación en una puntuación del 1 al 10"""

    if puntuacion >= 30:
        calificacion = 10
    elif puntuacion >= 20:
        calificacion = 8
    elif puntuacion >= 10:
        calificacion = 6
    elif puntuacion >= 0:
        calificacion = 4
    else:
        calificacion = 1
    
    return calificacion


# Función para registrar a todos los jugadores

def registrar_jugadores(cantidad_jugadores):
    """Registra nombres, estadísticas, puntuaciones y calificaciones"""

    nombres = []
    estadisticas_jugadores = []
    puntuaciones = []
    calificaciones = []

    for i in range(cantidad_jugadores):

        print("\nJugador", i + 1)

        nombre = pedir_nombre()

        estadisticas = obtener_estadisticas()

        # Guardar los datos en sus respectivas listas
        nombres.append(nombre)
        estadisticas_jugadores.append(estadisticas)

        puntuacion = calcular_desempeno(*estadisticas)
        puntuaciones.append(puntuacion)

        calificacion = obtener_calificacion(puntuacion)
        calificaciones.append(calificacion)

    return nombres, estadisticas_jugadores, puntuaciones, calificaciones


# Funciones para calcular el promedio del equipo

def calcular_promedio_equipo(puntuaciones):
    """Calcular el promedio del desempeño de todos los jugadores"""
    suma_puntuaciones = 0
    for puntuacion in puntuaciones:
        suma_puntuaciones = suma_puntuaciones + puntuacion
    promedio = suma_puntuaciones / len(puntuaciones)
    return promedio


# Funciones para calcular los puntos totales del equipo
# usando la lista anidada de estadísticas

def calcular_puntos_totales(estadisticas_jugadores):
    """Calcular los puntos anotados por los jugadores"""
    total = 0
    for jugador in estadisticas_jugadores:
        total = total + jugador[0]
    return total


# Función para calcular el promedio de cada estadística de todos los jugadores

def calcular_promedios_estadisticas(matriz):
    """Calcula el promedio de cada estadística de todos los jugadores"""

    promedios = []

    # Recorrer las columnas de la matriz
    for columna in range(len(matriz[0])):

        suma = 0

        # Recorrer las filas de la matriz
        for fila in matriz:
            suma = suma + fila[columna]

        promedio = suma / len(matriz)
        promedios.append(promedio)

    return promedios


# Función para encontrar al mejor jugador

def encontrar_mejor_jugador(puntuaciones):
    """Encuentra el indice del jugador con mayor puntuación"""

    mejor_indice = 0

    for i in range(1, len(puntuaciones)):

        if puntuaciones[i] > puntuaciones[mejor_indice]:
            mejor_indice = i

    return mejor_indice


# Función para mostrar el resultado de cada jugador

def mostrar_resultado(nombre, puntuacion, calificacion):
    """Muestra el resultado y calificación del jugador"""

    print()
    print("Jugador:", nombre)
    print("Puntuación:", puntuacion)
    print("Calificación:", calificacion, "/ 10")


# Función para mostrar los resultados de todos los jugadores

def mostrar_resultados_jugadores(nombres, puntuaciones, calificaciones):
    """Muestra los resultados individuales de todos los jugadores"""

    print("\nResultados de los jugadores")

    for i in range(len(nombres)):

        mostrar_resultado(
            nombres[i],
            puntuaciones[i],
            calificaciones[i]
        )


# Función para mostrar al mejor jugador

def mostrar_mejor_jugador(nombres, puntuaciones, calificaciones):
    """Muestra al jugador con el mejor desempeño"""

    mejor_indice = encontrar_mejor_jugador(puntuaciones)

    print("\nMejor desempeño")
    print("Jugador:", nombres[mejor_indice])
    print("Puntuación:", puntuaciones[mejor_indice])
    print("Calificación:", calificaciones[mejor_indice], "/ 10")


# Función para mostrar los promedios de las estadísticas

def mostrar_promedios_estadisticas(estadisticas_jugadores):
    """Muestra el promedio de cada estadística del equipo"""

    promedios_estadisticas = calcular_promedios_estadisticas(
        estadisticas_jugadores
    )

    print("\nPromedios de estadísticas del equipo")

    for i in range(len(promedios_estadisticas)):
        print(
            nombres_estadisticas[i] + ":",
            round(promedios_estadisticas[i], 2)
        )


# Función para mostrar los resultados generales del equipo

def mostrar_resultados_equipo(cantidad_jugadores, puntuaciones,
                                    estadisticas_jugadores):
    """Muestra los resultados generales del equipo"""

    promedio_equipo = calcular_promedio_equipo(puntuaciones)

    puntos_totales = calcular_puntos_totales(estadisticas_jugadores)

    print("\nResultados generales del equipo")
    print("Cantidad de jugadores:", cantidad_jugadores)
    print("Puntos totales anotados:", puntos_totales)
    print("Promedio del desempeño total del equipo:",
        round(promedio_equipo, 2))

    mostrar_promedios_estadisticas(estadisticas_jugadores)


# Función para preguntar si se desea continuar

def preguntar_continuar():
    """Pregunta si el usuario desea realizar otra búsqueda"""

    while True:

        continuar = input(
            "\n¿Deseas realizar otra búsqueda? (si/no): "
        ).lower().strip()

        if continuar == "si":
            return True

        elif continuar == "no":
            print("Calculo finalizado")
            return False

        else:
            print("Opción invalida. Ingresa 'si' o 'no'.")


#4. Función principal del programa ---------------------------------------

print("Bienvenido al programa para calcular el desempeño"
        " de tu equipo de basquetbol de hasta 5 personas")

while True:

    print("\nEstadísticas del equipo")

    # Solicitar la cantidad de jugadores
    cantidad_jugadores = pedir_cantidad_jugadores()

    # Registrar los jugadores y sus estadísticas
    nombres, estadisticas_jugadores, puntuaciones, calificaciones = (
        registrar_jugadores(cantidad_jugadores)
    )

    # Mostrar resultados individuales
    mostrar_resultados_jugadores(
        nombres,
        puntuaciones,
        calificaciones
    )

    # Mostrar al mejor jugador
    mostrar_mejor_jugador(
        nombres,
        puntuaciones,
        calificaciones
    )

    # Mostrar resultados generales del equipo
    mostrar_resultados_equipo(
        cantidad_jugadores,
        puntuaciones,
        estadisticas_jugadores
    )

    # Preguntar si se desea realizar otra evaluación
    continuar = preguntar_continuar()

    if continuar == False:
        break