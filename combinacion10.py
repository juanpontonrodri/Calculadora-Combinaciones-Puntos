#usadno numpy
import numpy as np
import pandas as pd
import os
from itertools import combinations,product


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

#combinaciones de nadadores de cada prueba
combinaciones_equipo_prueba = {}

for equipo, pruebas in diccionario.items():
    
    for prueba, nadadores in pruebas.items():
        combinaciones_prueba = []
        nombres_nadadores = list(nadadores.keys())
        combinaciones_nadadores = list(combinations(nombres_nadadores, 2))
        combinaciones_prueba.extend(combinaciones_nadadores)

        combinaciones_equipo_prueba[(equipo, prueba)] = combinaciones_prueba
        
print("##Combinaciones creadas##")
#cada nadador solo puede estar o en la combinacion de la preuab 1 o en la combinacino de la preuab 2

#combinacion MOLEMOS para prueba 1
    #combinacion MOLEMOS para prueba 2
    #miramos si alguno de los dos nadadores de esta combinacion esta en la combinacion de la prueba uno de MOLEMOS, si no esta continuamos
    
    #puntuacion_comb=[]
        #combinacion BOIRO para prueba 1
            #combinacion BOIRO para prueba 2
                #comprobamos si alguno de los dos nadadores de esta combinacion esta en la combinacion de la prueba uno de BOIRO, si no esta continuamos
                #combinacion RIAS para prueba 1
                    #combinacion RIAS para prueba 2
                        #comprobamos si alguno de los dos nadadores de esta combinacion esta en la combinacion de la prueba uno de RIAS, si no esta continuamos
                        #ordenamos tiempos de los 6 nadadores de la prueba 1 y calculamos puntuacion
                        #ordenamos tiempos de lso 6 nadadores de la prueba 2 y calculamos puntuacion
                        #puntuacion MOLEMOS= puntuacion nadadores MOLEMOS prueba 1 + puntuacion nadadores MOLEMOS prueba 2
                        #añadirmos a puntuacion_comb la puntuacion de MOLEMOS
    #hacemos la medai de puntuacion_comb
    #guardamos la media junto con las combinaciones de MOLEMOS para la prueba 1 y preuba 2 en un diccionario
                         
prueba_1="100_esp_masc" 
prueba_2="200_esp_masc"
   
puntuaciones = {}
for comb_MOLEMOS_p1 in combinaciones_equipo_prueba[('MOLEMOS', prueba_1)]:
    puntuaciones_MOLEMOS = []
    for comb_MOLEMOS_p2 in combinaciones_equipo_prueba[('MOLEMOS', prueba_2)]:
        print(comb_MOLEMOS_p1, comb_MOLEMOS_p2)
        puntuaciones_MOLEMOS = []
        if set(comb_MOLEMOS_p1) & set(comb_MOLEMOS_p2):
            continue
        for comb_BOIRO_p1, comb_BOIRO_p2, comb_RIAS_p1, comb_RIAS_p2 in product(combinaciones_equipo_prueba[('BOIRO', prueba_1)], combinaciones_equipo_prueba[('BOIRO', prueba_2)], combinaciones_equipo_prueba[('RIAS', prueba_1)], combinaciones_equipo_prueba[('RIAS', prueba_2)]):
            if set(comb_BOIRO_p1) & set(comb_BOIRO_p2) or set(comb_RIAS_p1) & set(comb_RIAS_p2):
                continue
            
            # Calcular puntuación
            tiempos_MOLEMOS_p1 = np.array([diccionario['MOLEMOS'][prueba_1][nadador][0] for nadador in comb_MOLEMOS_p1])
            tiempos_MOLEMOS_p2 = np.array([diccionario['MOLEMOS'][prueba_2][nadador][0] for nadador in comb_MOLEMOS_p2])
            tiempos_BOIRO_p1 = np.array([diccionario['BOIRO'][prueba_1][nadador][0] for nadador in comb_BOIRO_p1])
            tiempos_BOIRO_p2 = np.array([diccionario['BOIRO'][prueba_2][nadador][0] for nadador in comb_BOIRO_p2])
            tiempos_RIAS_p1 = np.array([diccionario['RIAS'][prueba_1][nadador][0] for nadador in comb_RIAS_p1])
            tiempos_RIAS_p2 = np.array([diccionario['RIAS'][prueba_2][nadador][0] for nadador in comb_RIAS_p2])

            tiempos_prueba1 = [(tiempo, 'MOLEMOS') for tiempo in tiempos_MOLEMOS_p1] + [(tiempo, 'BOIRO') for tiempo in tiempos_BOIRO_p1] + [(tiempo, 'RIAS') for tiempo in tiempos_RIAS_p1]
            tiempos_prueba2 = [(tiempo, 'MOLEMOS') for tiempo in tiempos_MOLEMOS_p2] + [(tiempo, 'BOIRO') for tiempo in tiempos_BOIRO_p2] + [(tiempo, 'RIAS') for tiempo in tiempos_RIAS_p2]

            tiempos_prueba1_ordenados = sorted(tiempos_prueba1, key=lambda x: x[0])
            tiempos_prueba2_ordenados = sorted(tiempos_prueba2, key=lambda x: x[0])

            puntos_MOLEMOS_p1 = 0
            puntos_MOLEMOS_p2 = 0
            puntos_BOIRO_p1 = 0
            puntos_BOIRO_p2 = 0
            puntos_RIAS_p1 = 0
            puntos_RIAS_p2 = 0

            for i, nadador in enumerate(tiempos_prueba1_ordenados):
                if nadador[1] == 'MOLEMOS':
                    puntos_MOLEMOS_p1 += 6 - i
                elif nadador[1] == 'BOIRO':
                    puntos_BOIRO_p1 += 6 - i
                else:
                    puntos_RIAS_p1 += 6 - i

            for i, nadador in enumerate(tiempos_prueba2_ordenados):
                if nadador[1] == 'MOLEMOS':
                    puntos_MOLEMOS_p2 += 6 - i
                elif nadador[1] == 'BOIRO':
                    puntos_BOIRO_p2 += 6 - i
                else:
                    puntos_RIAS_p2 += 6 - i
            puntos_MOLEMOS_p1 = np.sum(6 - np.argsort(tiempos_MOLEMOS_p1))
            puntos_MOLEMOS_p2 = np.sum(6 - np.argsort(tiempos_MOLEMOS_p2))
            puntos_BOIRO_p1 = np.sum(6 - np.argsort(tiempos_BOIRO_p1))
            puntos_BOIRO_p2 = np.sum(6 - np.argsort(tiempos_BOIRO_p2))
            puntos_RIAS_p1 = np.sum(6 - np.argsort(tiempos_RIAS_p1))
            puntos_RIAS_p2 = np.sum(6 - np.argsort(tiempos_RIAS_p2))
            puntuacion_MOLEMOS = puntos_MOLEMOS_p1 + puntos_MOLEMOS_p2
            puntuacion_BOIRO = puntos_BOIRO_p1 + puntos_BOIRO_p2
            puntuacion_RIAS = puntos_RIAS_p1 + puntos_RIAS_p2
            puntuaciones_MOLEMOS.append(puntuacion_MOLEMOS)

        puntuaciones[(comb_MOLEMOS_p1, comb_MOLEMOS_p2)] = sum(puntuaciones_MOLEMOS)/len(puntuaciones_MOLEMOS)

# Obtener las combinaciones con la puntuación más alta
mejores_combinaciones = [k for k, v in puntuaciones.items() if v == max(puntuaciones.values())]

print(mejores_combinaciones)