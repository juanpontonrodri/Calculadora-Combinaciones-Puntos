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
