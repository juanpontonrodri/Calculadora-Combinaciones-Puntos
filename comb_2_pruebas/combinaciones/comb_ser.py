import pandas as pd
import os
from itertools import combinations

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
        nombres_nadadores = list(nadadores.keys())
        combinaciones_prueba = combinations(nombres_nadadores, 2)
        for comb in combinaciones_prueba:
            nadador1 = comb[0]
            nadador2 = comb[1]
            print(f"Comb {comb}")
            print(diccionario[equipo][prueba][comb[0]])
            print(diccionario[equipo][prueba][comb[1]])

            
