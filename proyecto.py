#Encabezado --------------------------------------------------------------------
"""
Este proyecto esta echo por José Alberto Juárez Palazuelos
Este Programa es para calcular el desempeño de un jugador de baloncesto
O hasta el desempeño de todo un equipo de 5 personas
"""

#1. Importaciones ---------------------------------------------------------------

print("Bienvenido al programa para calcular el desempeño de tu equipo de basquetbol de hasta 5 personas")

#2. Variables globales y Constantes ---------------------------------------------

#Constantes para calcular el desempeño del jugador
Valor_Punto = 1
Valor_Asistencias = 0.8
Valor_Rebotes = 0.5
Valor_Robos = 1.5
Valor_Pase_Fallido = -2
Valor_Triple = 3
Valor_Perdidas = -1.5
Valor_Tapones = 2
Valor_Faltas = -3

nombres_estadisticas = ["Puntos", "Asistencias", "Rebotes", "Robos",
    "Pases fallidos", "Puntos de 3", "Perdidas", "Tapones", "Faltas"]

#3. Funciones ---------------------------------------------------------------------

#Función para pedir y validar datos de los jugadores

def pedir_dato(mensaje):
    """Pide un dato al usuario y valida que no sea un numero entero negativo"""
    while True:
        try:
            dato = int(input(mensaje))
            if dato >= 0:
                return dato
            print("Dato invalido. Por favor, ingresa un numero positivo.")

        except ValueError:
            print("El valor debe ser un numero entero positivo. Intente de nuevo.")

#Función para obtener estadísticas de cada jugador

def obtener_estadisticas():
    """Solicita estadisticas a evaluar de cada jugador"""
    puntos = pedir_dato("Puntos: ")
    asistencias = pedir_dato("Asistencias: ")
    rebotes = pedir_dato("Rebotes: ")
    robos = pedir_dato("Robos: ")
    pase_fallido = pedir_dato("Pases fallidos: ")
    puntos_tres = pedir_dato("Puntos de 3: ")
    perdidas = pedir_dato("Perdidas de balon: ")
    tapones = pedir_dato("Tiros bloqueados: ")
    faltas = pedir_dato("Faltas cometidas: ")

    return [puntos, asistencias, rebotes, 
            robos, pase_fallido, puntos_tres, 
            perdidas, tapones, faltas]

#Función para calcular el desempeño de cada jugador

def calcular_desempeno(puntos, asistencias, rebotes, 
                    robos, pase_fallido, puntos_tres, 
                    perdidas, tapones, faltas):

    """Calculo de la puntuacion de desempeño del jugador"""

    puntuacion = (puntos * Valor_Punto 
                    + asistencias * Valor_Asistencias 
                    + rebotes * Valor_Rebotes 
                    + robos * Valor_Robos 
                    + puntos_tres * Valor_Triple 
                    + pase_fallido * Valor_Pase_Fallido
                    + perdidas * Valor_Perdidas 
                    + tapones * Valor_Tapones 
                    + faltas * Valor_Faltas)

    return puntuacion

#Función para obtener calificación de cada jugador

def obtener_calificacion(puntuacion):
    """Convierte la calificacion en una puntuacion del 1 al 10"""

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

#Función para mostrar el resultado de cada jugador

def mostrar_resultado(nombre, puntuacion, calificacion):
    """Muestra el resultado y calificacion del jugador"""

    print()
    print("Jugador:", nombre)
    print("Puntuacion:", puntuacion)
    print("Calificacion:", calificacion, "/ 10")


#Funciones para calcular el promedio del equipo
def calcular_promedio_equipo (puntuaciones):
    """Calcular el promedio del desempeño de todos los jugadores"""
    suma_puntuaciones = 0
    for puntuacion in puntuaciones:
        suma_puntuaciones = suma_puntuaciones + puntuacion
    promedio = suma_puntuaciones /len (puntuaciones)
    return promedio

#Funciones para calcular los puntos totales del equipo
#usando la lista anidada de estadísticas
def calcular_puntos_totales(estadisticas_jugadores):
    """Calcular los puntos anotados por los jugadores"""
    total = 0
    for jugador in estadisticas_jugadores:
        total = total + jugador [0]
    return total

def calcular_promedios_estadisticas(matriz):
    """Calcula el promedio de cada estadistica de todos los jugadores"""

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


#Función para pedir la cantidad de jugadores

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


#Función para registrar a todos los jugadores

def registrar_jugadores(cantidad_jugadores):
    """Registra nombres, estadisticas, puntuaciones y calificaciones"""

    nombres = []
    estadisticas_jugadores = []
    puntuaciones = []
    calificaciones = []

    for i in range(cantidad_jugadores):

        print("\nJugador", i + 1)

        nombre = str(input("Nombre del jugador: "))

        estadisticas = obtener_estadisticas()

        # Guardar los datos en sus respectivas listas
        nombres.append(nombre)
        estadisticas_jugadores.append(estadisticas)

        puntuacion = calcular_desempeno(*estadisticas)
        puntuaciones.append(puntuacion)

        calificacion = obtener_calificacion(puntuacion)
        calificaciones.append(calificacion)

    return nombres, estadisticas_jugadores, puntuaciones, calificaciones


#Función para mostrar los resultados de todos los jugadores

def mostrar_resultados_jugadores(nombres, puntuaciones, calificaciones):
    """Muestra los resultados individuales de todos los jugadores"""

    print("\nResultados de los jugadores")

    for i in range(len(nombres)):

        mostrar_resultado(
            nombres[i],
            puntuaciones[i],
            calificaciones[i]
        )


#Función para encontrar al mejor jugador

def encontrar_mejor_jugador(puntuaciones):
    """Encuentra el indice del jugador con mayor puntuacion"""

    mejor_indice = 0

    for i in range(1, len(puntuaciones)):

        if puntuaciones[i] > puntuaciones[mejor_indice]:
            mejor_indice = i

    return mejor_indice


#Función para mostrar al mejor jugador

def mostrar_mejor_jugador(nombres, puntuaciones, calificaciones):
    """Muestra al jugador con el mejor desempeño"""

    mejor_indice = encontrar_mejor_jugador(puntuaciones)

    print("\nMejor desempeno")
    print("Jugador:", nombres[mejor_indice])
    print("Puntuacion:", puntuaciones[mejor_indice])
    print("Calificacion:", calificaciones[mejor_indice], "/ 10")



#Función para mostrar los promedios de las estadísticas

def mostrar_promedios_estadisticas(estadisticas_jugadores):
    """Muestra el promedio de cada estadistica del equipo"""

    promedios_estadisticas = calcular_promedios_estadisticas(
        estadisticas_jugadores
    )

    print("\nPromedios de estadisticas del equipo")

    for i in range(len(promedios_estadisticas)):
        print(
            nombres_estadisticas[i] + ":",
            round(promedios_estadisticas[i], 2)
        )


#Función para mostrar los resultados generales del equipo

def mostrar_resultados_equipo(cantidad_jugadores, puntuaciones,
                                    estadisticas_jugadores):
    """Muestra los resultados generales del equipo"""

    promedio_equipo = calcular_promedio_equipo(puntuaciones)

    puntos_totales = calcular_puntos_totales(estadisticas_jugadores)

    print("\nResultados generales del equipo")
    print("Cantidad de jugadores:", cantidad_jugadores)
    print("Puntos totales anotados:", puntos_totales)
    print("Promedio del desempeño total del equipo:", round(promedio_equipo, 2))

    mostrar_promedios_estadisticas(estadisticas_jugadores)



#Función para preguntar si se desea continuar

def preguntar_continuar():
    """Pregunta si el usuario desea realizar otra busqueda"""

    while True:

        continuar = input(
            "\n¿Deseas realizar otra busqueda? (si/no): "
        ).lower()

        if continuar == "si":
            return True

        elif continuar == "no":
            print("Calculo finalizado")
            return False

        else:
            print("Opcion invalida. Ingresa 'si' o 'no'.")


#4. Función principal del programa ---------------------------------------

while True:

    print("\nEstadisticas del equipo")

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

    # Preguntar si se desea realizar otra búsqueda
    if preguntar_continuar() == False:
        break