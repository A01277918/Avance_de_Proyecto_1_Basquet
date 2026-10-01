Valor_Punto = 1
Valor_Asistencias = 0.8
Valor_Rebotes = 0.5
Valor_Robos = 1.5
Valor_Pase_Fallido = -2
Valor_Triple = 3
Valor_Perdidas = -1.5
Valor_Tapones = 2
Valor_Faltas = -3

#FUNCION PARA PEDIR Y VALIDAR DATOS

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

# FUNCION PARA OBTENER ESTADISTICAS

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

# FUNCION PARA CALCULAR DESEMPENO

def calcular_desempeno(puntos, asistencias, rebotes, 
                    robos, pase_fallido, puntos_tres, 
                    perdidas, tapones, faltas):

    """Calculo de la puntuacion de desempeño del jugador"""

    puntuacion = (puntos * Valor_Punto + asistencias * Valor_Asistencias + 
                    rebotes * Valor_Rebotes + robos * Valor_Robos + 
                    puntos_tres * Valor_Triple - pase_fallido * Valor_Pase_Fallido
                    - perdidas * Valor_Perdidas - tapones * Valor_Tapones - faltas * Valor_Faltas)

    return puntuacion

# FUNCION PARA OBTENER CALIFICACION

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

# FUNCION PARA MOSTRAR RESULTADO

def mostrar_resultado(nombre, puntuacion, calificacion):
    """Muestra el resultado y calificacion del jugador"""

    print()
    print("Jugador:", nombre)
    print("Puntuacion:", puntuacion)
    print("Calificacion:", calificacion, "/ 10")

# LO QUE SE ESPERA DEL PROGRAMA

    while True:
        print("Estadisticas del jugador")

        jugadores = ()

        contador = 1

        while contador <= 5:
            print("Jugador", contador)

            nombre = str(input("Nombre del jugador: "))

            estadisticas = obtener_estadisticas()

            puntuacion = calcular_desempeno(*estadisticas)

            calificacion = obtener_calificacion(puntuacion)

            jugador = (nombre, puntuacion, calificacion)

            jugadores.append(jugador)

            contador += 1