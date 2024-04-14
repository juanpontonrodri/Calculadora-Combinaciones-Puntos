#intento de separo de diccionarios, no vale la pena
import pandas as pd
import os
from itertools import combinations,product
import time


def calc_puntuacion(diccionario):
    
    puntos_MOLEMOS_p1 = 0
    puntos_MOLEMOS_p2 = 0
    puntos_BOIRO_p1 = 0
    puntos_BOIRO_p2 = 0
    puntos_RIAS_p1 = 0
    puntos_RIAS_p2 = 0
    
#MAL A PARTIR DE AQUI
    
    for nadadores in diccionario.values():
        for tiempos in nadadores.values():
            tiempos_prueba = [(tiempo, equipo) for equipo, tiempo in tiempos.items()]
            print(tiempos_prueba)
            tiempos_prueba_ordenados = sorted(tiempos_prueba, key=lambda x: x[0])
            
            if tiempos is diccionario['MOLEMOS'][prueba_1]:
                puntos_MOLEMOS_p1 = sum([6-i for i in range(len(tiempos_prueba_ordenados)) if tiempos_prueba_ordenados[i][1] == 'MOLEMOS'])
            elif tiempos is diccionario['MOLEMOS'][prueba_2]:
                puntos_MOLEMOS_p2 = sum([6-i for i in range(len(tiempos_prueba_ordenados)) if tiempos_prueba_ordenados[i][1] == 'MOLEMOS'])
            elif tiempos is diccionario['BOIRO'][prueba_1]:
                puntos_BOIRO_p1 = sum([6-i for i in range(len(tiempos_prueba_ordenados)) if tiempos_prueba_ordenados[i][1] == 'BOIRO'])
            elif tiempos is diccionario['BOIRO'][prueba_2]:
                puntos_BOIRO_p2 = sum([6-i for i in range(len(tiempos_prueba_ordenados)) if tiempos_prueba_ordenados[i][1] == 'BOIRO'])
            elif tiempos is diccionario['RIAS'][prueba_1]:
                puntos_RIAS_p1 = sum([6-i for i in range(len(tiempos_prueba_ordenados)) if tiempos_prueba_ordenados[i][1] == 'RIAS'])
            elif tiempos is diccionario['RIAS'][prueba_2]:
                puntos_RIAS_p2 = sum([6-i for i in range(len(tiempos_prueba_ordenados)) if tiempos_prueba_ordenados[i][1] == 'RIAS'])

    puntuacion_MOLEMOS = puntos_MOLEMOS_p1 + puntos_MOLEMOS_p2;
    puntuacion_BOIRO = puntos_BOIRO_p1 + puntos_BOIRO_p2;
    puntuacion_RIAS = puntos_RIAS_p1 + puntos_RIAS_p2;
    
    return puntuacion_MOLEMOS, puntuacion_BOIRO, puntuacion_RIAS


""" def crear_diccionario(archivo):
        
    # Leer el archivo CSV
    df = pd.read_csv(archivo)

    # Crear un diccionario para almacenar los tiempos de cada nadador
    diccionario = {}

    # Recorrer el DataFrame y agregar los tiempos a cada nadador en el diccionario
    for index, row in df.iterrows():
        equipo = row["Equipo"]
        tiempo = row["Tiempo"]
        nombre = row["Nombre"]
        prueba = row["Prueba"]
        if equipo not in diccionario:
            diccionario[equipo] = {}
        if prueba not in diccionario[equipo]:
            diccionario[equipo][prueba] = {}
        if nombre not in diccionario[equipo][prueba]:
            diccionario[equipo][prueba][nombre] = []
        diccionario[equipo][prueba][nombre].append(tiempo)

    # Obtener la lista de nombres de prueba
    nombre_prueba = sorted(list(set(df["Prueba"]))) 

    return diccionario, nombre_prueba"""

def crear_diccionario(folder_path):
        
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

    return diccionario, nombre_prueba

def crear_combinaciones(diccionario):
        
    #combinaciones de nadadores de cada prueba
    combinaciones_equipo_prueba = {}

    for equipo, pruebas in diccionario.items():
        
        for prueba, nadadores in pruebas.items():
            combinaciones_prueba = []
            nombres_nadadores = list(nadadores.keys())
            combinaciones_nadadores = list(combinations(nombres_nadadores, 2))
            combinaciones_prueba.extend(combinaciones_nadadores)

            combinaciones_equipo_prueba[(equipo, prueba)] = combinaciones_prueba
    return combinaciones_equipo_prueba

def crear_diccionarios_por_club(diccionario):
    diccionarios_por_club = {}
    for club, pruebas in diccionario.items():
        if club not in diccionarios_por_club:
            diccionarios_por_club[club] = {}
        for prueba, nadadores in pruebas.items():
            if prueba not in diccionarios_por_club[club]:
                diccionarios_por_club[club][prueba] = {'nadadores': [], 'tiempos': []}

            for nadador, tiempos in nadadores.items():
                diccionarios_por_club[club][prueba]['nadadores'].append(nadador)
                diccionarios_por_club[club][prueba]['tiempos'].append(tiempos)
    return diccionarios_por_club



start_time = time.time()



folder_path = './series/'

diccionario,nombres_pruebas = crear_diccionario(folder_path)

print("###Diccionario creado###")

diccionario_nuevo=crear_diccionarios_por_club(diccionario)

print("###Diccionario nuevo creado###")


combinaciones_equipo_prueba = crear_combinaciones(diccionario)

print("###Combinaciones creadas###")


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
                         
prueba_1=nombres_pruebas[0]
prueba_2=nombres_pruebas[1]
                       
c=0
numero_combinaciones_MOLEMOS = 1
numero_combinaciones_totales=1

for prueba in nombres_pruebas:
    numero_combinaciones_MOLEMOS=numero_combinaciones_MOLEMOS*len(combinaciones_equipo_prueba[('MOLEMOS', prueba)])
    numero_combinaciones_totales=numero_combinaciones_MOLEMOS*len(combinaciones_equipo_prueba[('BOIRO', prueba)])*len(combinaciones_equipo_prueba[('RIAS', prueba)])

puntuaciones = {}
for comb_MOLEMOS_p1 in combinaciones_equipo_prueba[('MOLEMOS', prueba_1)]:
    for comb_MOLEMOS_p2 in combinaciones_equipo_prueba[('MOLEMOS', prueba_2)]:
        c+=1
        print("Combinación número %d de %d %s %s" % (c, numero_combinaciones_MOLEMOS, comb_MOLEMOS_p1, comb_MOLEMOS_p2))
        puntuaciones_MOLEMOS = []
        if set(comb_MOLEMOS_p1) & set(comb_MOLEMOS_p2):
            continue
        for comb_BOIRO_p1, comb_BOIRO_p2, comb_RIAS_p1, comb_RIAS_p2 in product(combinaciones_equipo_prueba[('BOIRO', prueba_1)], combinaciones_equipo_prueba[('BOIRO', prueba_2)], combinaciones_equipo_prueba[('RIAS', prueba_1)], combinaciones_equipo_prueba[('RIAS', prueba_2)]):
            if set(comb_BOIRO_p1) & set(comb_BOIRO_p2) or set(comb_RIAS_p1) & set(comb_RIAS_p2):
                continue
            
            tiempos_MOLEMOS=[]
            tiempos_BOIRO=[]
            tiempos_RIAS=[]
            
            
            #probar usando tiemposmolemos.append en vez d eponer lo sindices
            tiempos_MOLEMOS.append([diccionario['MOLEMOS'][prueba_1][nadador][0] for nadador in comb_MOLEMOS_p1])
            tiempos_MOLEMOS.append([diccionario['MOLEMOS'][prueba_2][nadador][0] for nadador in comb_MOLEMOS_p2])
            tiempos_BOIRO.append([diccionario['BOIRO'][prueba_1][nadador][0] for nadador in comb_BOIRO_p1])
            tiempos_BOIRO.append([diccionario['BOIRO'][prueba_2][nadador][0] for nadador in comb_BOIRO_p2])
            tiempos_RIAS.append([diccionario['RIAS'][prueba_1][nadador][0] for nadador in comb_RIAS_p1])
            tiempos_RIAS.append([diccionario['RIAS'][prueba_2][nadador][0] for nadador in comb_RIAS_p2])
            
            #Para dos pruebas sube el tiempo de ejecucion en un 15%
            """ contador = 1
            for prueba in nombres_pruebas:
                comb_MOLEMOS = globals()[f"comb_MOLEMOS_p{contador}"]
                tiempos_MOLEMOS.append([diccionario['MOLEMOS'][prueba][nadador][0] for nadador in comb_MOLEMOS])
                
                # Repite el mismo proceso para las otras variables de combinación
                comb_BOIRO = globals()[f"comb_BOIRO_p{contador}"]
                tiempos_BOIRO.append([diccionario['BOIRO'][prueba][nadador][0] for nadador in comb_BOIRO])
                
                comb_RIAS = globals()[f"comb_RIAS_p{contador}"]
                tiempos_RIAS.append([diccionario['RIAS'][prueba][nadador][0] for nadador in comb_RIAS])
                
                contador += 1 """

            
            puntuacion_MOLEMOS, puntuacion_BOIRO, puntuacion_RIAS= calc_puntuacion(diccionario_nuevo)
            puntuaciones_MOLEMOS.append(puntuacion_MOLEMOS)

        puntuaciones[(comb_MOLEMOS_p1, comb_MOLEMOS_p2)] = sum(puntuaciones_MOLEMOS)/len(puntuaciones_MOLEMOS)

# Obtener las combinaciones con la puntuación más alta
mejores_combinaciones = [k for k, v in puntuaciones.items() if v == max(puntuaciones.values())]

print(mejores_combinaciones)



end_time=time.time()

print()
print("Numero de combinaciones totales: ",numero_combinaciones_totales)
print("Tiempo de ejecución: ",end_time-start_time)
