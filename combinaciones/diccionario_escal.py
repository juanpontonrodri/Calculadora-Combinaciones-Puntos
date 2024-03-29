import pandas as pd
import os

folder_path = './series/'

# Obtener los nombres de los archivos en la carpeta
file_names = os.listdir(folder_path)

# Crear un diccionario para almacenar las pruebas y sus archivos
pruebas_archivos = {}

# Agregar cada archivo al diccionario con el nombre de la prueba como clave
for name in file_names:
    # Obtener el nombre de la prueba a partir del nombre del archivo
    prueba_name = name.split('_tiempos')[0]
    # Agregar la prueba y su archivo al diccionario
    pruebas_archivos[prueba_name] = folder_path + name

# Obtener la lista de nombres de prueba
nombre_prueba = list(pruebas_archivos.keys())
# Leer los archivos CSV y guardar los tiempos de cada nadador
diccionario = {}
for prueba, archivo in pruebas_archivos.items():
    df = pd.read_csv(archivo)
    for index, row in df.iterrows():
        equipo = row["Equipo"]
        tiempo = row["Tiempo"]
        nombre = row["Nombre"]
        if row["Prueba"] != prueba:
            continue
        if equipo not in diccionario:
            diccionario[equipo] = {}
        if prueba not in diccionario[equipo]:
            diccionario[equipo][prueba] = {}
        if nombre not in diccionario[equipo][prueba]:
            diccionario[equipo][prueba][nombre] = []
        diccionario[equipo][prueba][nombre].append(tiempo)

# Imprimir los resultados
for equipo, pruebas in diccionario.items():
    for prueba, nadadores in pruebas.items():
        print(f"{prueba} ({equipo})")
        for nadador, tiempos in nadadores.items():
            print(f"{nadador}: {tiempos[0]}")
        print()

#Imprimir con indice 
# Bucle para recorrer los equipos
for equipo in diccionario:
    print("\n\n\nEquipo:", equipo)
    # Bucle para recorrer las pruebas de cada equipo
    for prueba in diccionario[equipo]:
        print("\nPrueba:", prueba)
        nadadores = list(diccionario[equipo][prueba].keys())
        nadadores.sort()
        # Bucle para recorrer los nadadores de cada prueba
        for i, nadador in enumerate(nadadores):
            tiempos = diccionario[equipo][prueba][nadador]
            print(f"{i+1}. {nadador}: {tiempos}")

#Crear array nombres nadadores  boiro 100 espalda
# imprime los nomrbes y tiempos


nadadores_100_espalda_boiro = list(diccionario["RIAS"]["200_esp_masc"].keys())
for nadador in nadadores_100_espalda_boiro:
    print(nadador, diccionario["RIAS"]["200_esp_masc"][nadador][0])
