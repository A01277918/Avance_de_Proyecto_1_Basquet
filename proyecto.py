#Encabezado --------------------------------------------------------------------
"""
Este proyecto esta echo por Jose Alberto Juarez Palazuelos
Este Programa es para calcular el desempeño de un jugador de baloncesto
O hasta el desepeño de todo un equipo de 5 personas
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
        suma_puntuaciones += puntuacion
    promedio = suma_puntuaciones /len (puntuaciones)
    return promedio

#Funciones para calcular los puntos totales del equipo
#usando la lista anidada de estadísticas
def calcular_puntos_totales(estadisticas_jugadores):
    """Calcular los puntos anotados por los jugadores"""
    total = 0
    for jugador in estadisticas_jugadores:
        total += jugador [0]
    return total


#4. Función principal del programa ----------------------------------------

while True:
    print("Estadisticas del equipo")

    # Preguntar cuantos jugadores se evaluaran
    while True:
        try:
            cantidad_jugadores = int(
                input("¿Cuantos jugadores deseas evaluar? (1-5): ")
            )

# Verificar que la cantidad este entre 1 y 5
            if 1 <= cantidad_jugadores <= 5:
                break

            print("Error: debes ingresar un numero del 1 al 5.")

# Evitar que el programa se detenga si se ingresan letras
        except ValueError:
            print("Error: debes ingresar un numero entero.")

# Crear una lista vacia para almacenar los datos de los jugadores
    nombres = []
    estadisticas_jugadores = []
    puntuaciones = []
    calificaciones = []
    contador = 1

# Registrar las estadísticas de cada jugador
    for i in range(cantidad_jugadores):

        print("\nJugador", i + 1)

        nombre = str(input("Nombre del jugador: "))

# Guardar las estadisticas como una lista
        estadisticas = obtener_estadisticas()

# Agregar los datos a sus respectivas listas
        nombres.append(nombre)
        estadisticas_jugadores.append(estadisticas)

        puntuacion = calcular_desempeno(*estadisticas)

# Guardar la puntuacion en una lista
        puntuaciones.append(puntuacion)

# guardar la calificacion en una lista
        calificacion = obtener_calificacion(puntuacion)
        calificaciones.append(calificacion)


#Mostrar resultados de cada jugador

    print("\nResultados de los jugadores")

    for i in range(cantidad_jugadores):

        mostrar_resultado(
            nombres[i],
            puntuaciones[i],
            calificaciones[i]
        )

# Encontrar al mejor jugador usando su indice
    mejor_indice = 0

    for i in range(1, len(puntuaciones)):

        if puntuaciones[i] > puntuaciones[mejor_indice]:
            mejor_indice = i

    print("\nMejor desempeno")

# Usar el mismo indice en las listas
    print("Jugador:", nombres[mejor_indice])
    print("Puntuacion:", puntuaciones[mejor_indice])
    print("Calificacion:", calificaciones[mejor_indice], "/ 10")


#Calcular el promedio del equipo
    promedio_equipo = calcular_promedio_equipo(puntuaciones)

#Calcular los puntos totales con la matriz
    puntos_totales = calcular_puntos_totales(estadisticas_jugadores)

#Mostrar los resultados generales del equipo
    print("\nResultados generales del equipo")
    print("Cantidad de jugadores", cantidad_jugadores)
    print("Puntos totales anotados", puntos_totales)
    print("Promedio del desempeño total de equipo", round(promedio_equipo, 2))


# Preguntar si el usuario desea evaluar otro grupo de jugadores

    while True:

            continuar = input(
        "\n¿Deseas realizar otra busqueda? (si/no): "
    ).lower()

            if continuar == "si":
                break

            elif continuar == "no":
                print("Calculo finalizado ")
                break

            else:
# Volver a preguntar si la opcion ingresada no es valida
                print("Opcion invalida. Ingresa 'si' o 'no'.")

# Finalizar el ciclo principal si el usuario decide salir
    if continuar == "no":
            break