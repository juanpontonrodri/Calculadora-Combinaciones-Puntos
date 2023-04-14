import itertools
import pandas as pd

# Lee el archivo CSV
filename1 = "series/50_esp_masc_tiempos.csv"
nombre_prueba1 = filename1.split("/")[-1].split("_tiempos")[0]
data1 = pd.read_csv(filename1)

# Lee el archivo CSV
filename2 = "series/100_esp_masc_tiempos.csv"
nombre_prueba2 = filename2.split("/")[-1].split("_tiempos")[0]
data2 = pd.read_csv(filename2)

# Definir los equipos y las pruebas
equipos = ["MOLEMOS", "BOIRO", "RIAS"]
pruebas = {nombre_prueba1: ["50m espalda"], nombre_prueba2: ["100m espalda"]}

# Inicializar el diccionario de resultados
diccionario = {}

# Para cada equipo y cada prueba, crear una entrada en el diccionario de diccionario
for equipo in equipos:
    diccionario[equipo] = {}
    for prueba in pruebas:
        diccionario[equipo][prueba] = {}

# Llenar el diccionario de diccionario con los tiempos de cada nadador
for index, row in data1.iterrows():
    equipo = row["Equipo"]
    tiempo = row["Tiempo"]
    nombre = row["Nombre"]
    for prueba in pruebas[nombre_prueba1]:
        if prueba not in diccionario[equipo]:
            diccionario[equipo][prueba] = {}
        if nombre not in diccionario[equipo][prueba]:
            diccionario[equipo][prueba][nombre] = []
        diccionario[equipo][prueba][nombre].append(tiempo)

for index, row in data2.iterrows():
    equipo = row["Equipo"]
    tiempo = row["Tiempo"]
    nombre = row["Nombre"]
    for prueba in pruebas[nombre_prueba2]:
        if prueba not in diccionario[equipo]:
            diccionario[equipo][prueba] = {}
        if nombre not in diccionario[equipo][prueba]:
            diccionario[equipo][prueba][nombre] = []
        diccionario[equipo][prueba][nombre].append(tiempo)

# Bucle para recorrer los equipos
for equipo in diccionario:
    print("Equipo:", equipo)
    # Bucle para recorrer las pruebas de cada equipo
    for prueba in diccionario[equipo]:
        print("Prueba:", prueba)
        # Bucle para recorrer los nadadores de cada prueba
        for nadador in diccionario[equipo][prueba]:
            print("Nadador:", nadador)
            # Imprime los tiempos de cada nadador en la prueba correspondiente
            print("Tiempos:", diccionario[equipo][prueba][nadador])

# Define los equipos y las pruebas
equipos = ["MOLEMOS", "BOIRO", "RIAS"]
pruebas = {"50m espalda": [], "100m espalda": []}

# Obtén los nadadores inscritos por club en cada prueba
for equipo in equipos:
    for prueba in pruebas:
        for nadador in diccionario[equipo][prueba]:
            pruebas[prueba].append((equipo, nadador))

# Inicializa el diccionario para el registro de los nadadores usados
nadadores_usados = {}
for equipo in equipos:
    nadadores_usados[equipo] = set()

# Inicializa las variables para guardar la combinación con más puntos y su puntuación
mejor_combinacion = []
mejor_puntuacion = 0

# Recorre todas las combinaciones de nadadores
for combinacion in itertools.product(pruebas["50m espalda"], pruebas["100m espalda"]):
    # Verifica que la combinación cumpla con las restricciones
    nadadores_utilizados = set()
    puntuacion = 0
    for prueba, nadador in combinacion:
        equipo, nombre = nadador
        if len(diccionario[equipo][prueba][nombre]) != 1:
            # Si el nadador ha participado en otra prueba, saltar a la siguiente combinación
            break
        if equipo in nadadores_usados and nombre in nadadores_usados[equipo]:
            # Si el nadador ya ha sido utilizado en otra prueba, saltar a la siguiente combinación
            break
        if len(nadadores_utilizados) == 6:
            # Si ya hay 6 nadadores utilizados en la combinación, saltar a la siguiente combinación
            break
        # Añadir el nadador a los registros de nadadores usados
        if equipo not in nadadores_usados:
            nadadores_usados[equipo] = set()
        nadadores_usados[equipo].add(nombre)
        nadadores_utilizados.add(nadador)
        # Calcular la puntuación de la prueba para el equipo
        posicion = sorted(diccionario[equipo][prueba][nombre])[0:2].index(diccionario[equipo][prueba][nombre][0])
        puntuacion += 7 - posicion
    else:
        # La combinación cumple con las restricciones, actualizar la mejor combinación y puntuación
        if puntuacion > mejor_puntuacion:
            mejor_combinacion = combinacion
            mejor_puntuacion = puntuacion

print("Mejor combinación:", mejor_combinacion)
print("Puntuación:", mejor_puntuacion)
