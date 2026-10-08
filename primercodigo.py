#Programa para calcular el desempeño de un jugador de baloncesto

print("Bienvenido al programa para calcular el desempeño de tu equipo de basquetbol de hasta 5 personas")

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

#Funcion para pedir y validar datos de los jugadores

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

#Funcion para obtener estadisticas de cada jugador

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

    return (puntos, asistencias, rebotes, 
            robos, pase_fallido, puntos_tres, 
            perdidas, tapones, faltas)

#Funcion para calcular el desempeño de cada jugador

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

#Funcion para obtener calificacion de cada jugador

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

#Funcion para mostrar el restultado de cada jugador

def mostrar_resultado(nombre, puntuacion, calificacion):
    """Muestra el resultado y calificacion del jugador"""

    print()
    print("Jugador:", nombre)
    print("Puntuacion:", puntuacion)
    print("Calificacion:", calificacion, "/ 10")

#Lo que se espera del programa

#Aun no esta completo debido a que aun no tengo los conocimientos sorry (luego borrare esta parte no se preocupen)

while True:
    print("Estadisticas del equipo")

    # Preguntar cuantos jugadores se evaluaran
    while True:
        try:
            cantidad_jugadores = int(
                input("¿Cuantos jugadores deseas evaluar? (1-5): ")
            )

            if 1 <= cantidad_jugadores <= 5:
                break

            print("Error: debes ingresar un numero del 1 al 5.")

        except ValueError:
            print("Error: debes ingresar un numero entero.")

    jugadores = []

    contador = 1

    while contador <= cantidad_jugadores:
            
            print("Jugador", contador)

            nombre = str(input("Nombre del jugador: "))

            estadisticas = obtener_estadisticas()

            puntuacion = calcular_desempeno(*estadisticas)

            calificacion = obtener_calificacion(puntuacion)

            jugador = (nombre, puntuacion, calificacion)

            jugadores.append(jugador)

            contador += 1

#Mostrar resultados de cada jugador

            print("Resultados de los jugadores")

    for jugador in jugadores:
            mostrar_resultado(jugador[0], jugador[1], jugador[2])

#Encontrar el jugador con mejor jugador

    mejor_jugador = jugadores[0]
    contador = 1
    while contador < len(jugadores):
            if jugadores[contador][1] > mejor_jugador[1]:
                mejor_jugador = jugadores[contador]
            contador += 1

    print("Mejor desempeño")

    print("jugador:", mejor_jugador[0])
    print("Puntuación:", mejor_jugador[1])
    print("Calificación:", mejor_jugador[2], "/ 10")

#Pregunta si quiere continuar

    while True:

            continuar = input(
        "\n¿Deseas realizar otra busqueda? (si/no): "
    ).lower()

            if continuar == "si":
                break

            elif continuar == "no":
                print("Programa finalizado.")
                break
            else:
                print("Opcion invalida. Ingresa 'si' o 'no'.")
    if continuar == "no":
            break