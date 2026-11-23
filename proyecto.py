#Encabezado ------------------------------------------------------------------

"""
Proyecto elaborado por José Alberto Juárez Palazuelos.

Este programa permite calcular y evaluar el desempeño de jugadores de baloncesto
a partir de diferentes estadísticas individuales.

Permite registrar de 1 hasta 5 jugadores, ingresar sus estadísticas
y calcular una calificación de acuerdo con su rendimiento.

También permite analizar el desempeño individual de cada jugador
y obtener estadísticas generales del equipo.
"""

#1. Importaciones ------------------------------------------------------------

# Ninguna librería externa es necesaria para este proyecto
# Pero se deja el encabezado para futuras importaciones si se requieren

#2. Variables globales y Constantes ------------------------------------------

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

NOMBRES_ESTADISTICAS = ["Puntos", "Asistencias", "Rebotes", "Robos",
    "Pases fallidos", "Puntos de 3", "Perdidas", "Tapones", "Faltas"]

#3. Funciones ----------------------------------------------------------------


# Función para pedir y validar datos de los jugadores

def pedir_dato(mensaje):
    """Solicita un nombre al usuario, lo normaliza y valida su formato."""
    while True:
        try:
            entrada = input(mensaje).strip()

            dato = int(entrada)

            if dato < 0 or dato > 99:
                print("Error: el valor debe estar entre 0 y 99.")

            else:
                return dato

        except ValueError:
            print("Error: debes ingresar un numero valido.")


# Funciones para manipular cadenas de texto

def normalizar_nombre(nombre):
    """Limpia los espacios y organiza las mayúsculas del nombre."""

    # strip() elimina los espacios al inicio y al final del texto.
    # split() divide el texto en palabras, permite eliminar espacios extra
    nombre = nombre.strip()
    nombre = " ".join(nombre.split())
    nombre = nombre.title()

    return nombre


def validar_nombre(nombre):
    """Verifica que el nombre no esté vacío, no supere 30 caracteres
    y contenga únicamente letras y espacios."""

    if len(nombre) == 0 or len(nombre) > 30:
        return False
    # Verifica que cada carácter sea una letra o un espacio en blanco.
    # isalpha() comprueba si el carácter es una letra.
    # isspace() comprueba si el carácter es un espacio en blanco.
    if not all(letra.isalpha() or letra.isspace()
            for letra in nombre):
        return False

    return True


# Función para solicitar y validar el nombre del jugador.

def pedir_nombre():
    """Solicita un nombre de máximo 30 caracteres y valida
    que solo tenga letras y espacios."""

    while True:
        nombre = normalizar_nombre(
            input("Nombre del jugador: ")
        )

        if validar_nombre(nombre):
            return nombre

        print("Error: nombre inválido.")


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


# Función para leer los jugadores desde un archivo externo

def leer_jugadores_archivo(nombre_archivo):
    """Lee, normaliza y valida los nombres y estadísticas
    de los jugadores desde un archivo."""
    
    # Crear listas vacías para almacenar los datos de los jugadores
    nombres = []
    estadisticas_jugadores = []
    puntuaciones = []
    calificaciones = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                ## Ignorar las líneas que estén vacías
                if linea.strip() == "":
                    continue

                ## Eliminar espacios y separar los datos mediante comas
                datos = linea.strip().split(",")

                if len(datos) != 10:
                    print("Error: cada jugador debe tener 10 datos.")
                    return None

                nombre = normalizar_nombre(datos[0])
                # Validar que el nombre no esté vacío
                if not validar_nombre(nombre):
                    print("Error: nombre inválido en el archivo.")
                    return None

                try:
                    estadisticas = []

                    # Convertir cada estadística de texto a entero
                    for dato in datos[1:]:
                        valor = int(dato.strip())

                        if valor < 0 or valor > 99:
                            print("Error: estadística fuera del rango.")
                            return None

                        estadisticas.append(valor)

                except ValueError:
                    print("Error: hay una estadística que no es entera.")
                    return None

                ## Guardar el nombre y las estadísticas del jugador
                nombres.append(nombre)
                estadisticas_jugadores.append(estadisticas)

                # Calcular y guardar la puntuación de desempeño
                puntuacion = calcular_desempeno(*estadisticas)
                puntuaciones.append(puntuacion)

                # Obtener y guardar la calificación del jugador
                calificacion = obtener_calificacion(puntuacion)
                calificaciones.append(calificacion)

                # Verificar que el archivo no contenga más de 5 jugadores
                if len(nombres) > 5:
                    print("El archivo no puede tener más de 5 jugadores.")
                    return None

        # Verificar que el archivo contenga al menos un jugador
        if len(nombres) == 0:
            print("Error: el archivo no contiene jugadores.")
            return None

        return nombres, estadisticas_jugadores, puntuaciones, calificaciones

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")
        return None


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
        nombre = normalizar_nombre(nombre)

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
            NOMBRES_ESTADISTICAS[i] + ":",
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


# Función para guardar los resultados en un archivo de texto

def guardar_resultados_archivo(nombres, estadisticas_jugadores,
                            puntuaciones, calificaciones):
    """Guarda las estadísticas y resultados en un archivo .txt"""

    nombre_archivo = input(
        "\nIngresa el nombre para guardar el documento: "
    ).strip()

    # Agregar la extensión .txt al nombre del archivo
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo = nombre_archivo + ".txt"

    # Abrir el archivo para escribir los resultados
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:

        archivo.write("ESTADÍSTICAS DEL EQUIPO DE BALONCESTO\n")
        archivo.write("-------------------------------------\n")

        # Guardar las estadísticas de cada jugador
        for i in range(len(nombres)):

            archivo.write("\nJugador: " + nombres[i] + "\n")

            for j in range(len(estadisticas_jugadores[i])):

                archivo.write(
                    NOMBRES_ESTADISTICAS[j] + ": "
                    + str(estadisticas_jugadores[i][j]) + "\n"
                )

            archivo.write(
                "Puntuación: " + str(puntuaciones[i]) + "\n"
            )

            archivo.write(
                "Calificación: " + str(calificaciones[i]) + "/10\n"
            )

        # Guardar los resultados generales del equipo
        promedio = calcular_promedio_equipo(puntuaciones)

        puntos_totales = calcular_puntos_totales(
            estadisticas_jugadores
        )

        archivo.write("\nRESULTADOS GENERALES DEL EQUIPO\n")
        archivo.write("-------------------------------------\n")

        archivo.write(
            "Cantidad de jugadores: " + str(len(nombres)) + "\n"
        )

        archivo.write(
            "Puntos totales: " + str(puntos_totales) + "\n"
        )

        archivo.write(
            "Promedio de desempeño: " + str(round(promedio, 2)) + "\n"
        )

        # Guardar al mejor jugador
        mejor_indice = encontrar_mejor_jugador(puntuaciones)

        archivo.write("\nMEJOR JUGADOR\n")
        archivo.write("-------------------------------------\n")

        archivo.write(
            "Jugador: " + nombres[mejor_indice] + "\n"
        )

        archivo.write(
            "Puntuación: " + str(puntuaciones[mejor_indice]) + "\n"
        )

        archivo.write(
            "Calificación: "
            + str(calificaciones[mejor_indice]) + "/10\n"
        )

        # Guardar los promedios de las estadísticas
        promedios = calcular_promedios_estadisticas(
            estadisticas_jugadores
        )

        archivo.write("\nPROMEDIOS DE ESTADÍSTICAS\n")
        archivo.write("-------------------------------------\n")

        for i in range(len(promedios)):

            archivo.write(
                NOMBRES_ESTADISTICAS[i] + ": "
                + str(round(promedios[i], 2)) + "\n"
            )

    print("\nEl documento se guardó correctamente:", nombre_archivo)


# Función para preguntar si se desea continuar

def preguntar_continuar():
    """Pregunta si el usuario desea realizar otra evaluación"""

    while True:

        continuar = input(
            "\n¿Deseas realizar otra evaluación? (si/no): "
        ).strip().lower()

        if continuar == "si":
            return True

        elif continuar == "no":
            print("Calculo finalizado")
            return False

        else:
            print("Opción invalida. Ingresa 'si' o 'no'.")


# Función para elegir la forma de registrar jugadores

def pedir_modo_registro():
    """Permite elegir entre registro manual o archivo externo."""

    while True:
        print("\n¿Cómo deseas registrar a los jugadores?")
        print("1. Ingresar los datos manualmente")
        print("2. Leer los datos desde un archivo")

        ## Solicitar la opción y eliminar espacios innecesarios
        opcion = input("Selecciona una opción: ").strip()

        # Validar que la opción ingresada sea 1 o 2
        if opcion == "1" or opcion == "2":
            return opcion

        print("Opción inválida. Selecciona 1 o 2.")


#4. Función principal del programa -----------------------------------------

def main():
    """Ejecuta el programa principal de evaluación."""
    
    print("Bienvenido al programa para calcular el desempeño"
        " de tu equipo de basquetbol de hasta 5 personas")

    while True:

        print("\nEstadísticas del equipo")

        # Solicitar al usuario la forma de registrar a los jugadores
        modo = pedir_modo_registro()

        if modo == "1":

            # Solicitar la cantidad de jugadores
            cantidad_jugadores = pedir_cantidad_jugadores()

            # Registrar los jugadores y sus estadísticas
            nombres, estadisticas_jugadores, puntuaciones, calificaciones = (
            registrar_jugadores(cantidad_jugadores)
        )

        # Si selecciona la opción 2, leer los datos desde un archivo externo
        elif modo == "2":

            nombre_archivo = input(
                "Escribe el nombre de tu archivo de estadísticas: "
            )

            datos = leer_jugadores_archivo(nombre_archivo)

            # Si ocurre un error al leer el archivo, regresar al menú
            if datos is None:
                continue

            # Separar y guardar la información obtenida del archivo
            (nombres, estadisticas_jugadores, 
            puntuaciones, calificaciones) = datos

            cantidad_jugadores = len(nombres)
    
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
        
        # Guardar los resultados si el registro fue manual
        if modo == "1":

            guardar_resultados_archivo(
            nombres,
            estadisticas_jugadores,
            puntuaciones,
            calificaciones
            )
        # Preguntar si se desea realizar otra evaluación
        continuar = preguntar_continuar()

        if continuar == False:
            break

# Verifica que el archivo se esté ejecutando directamente
# Llama a la función principal del programa
if __name__ == "__main__":
    main()