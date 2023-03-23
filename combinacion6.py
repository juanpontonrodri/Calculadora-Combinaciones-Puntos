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

# Imprimir los resultados
""" for equipo, pruebas in diccionario.items():
    for prueba, nadadores in pruebas.items():
        print(f"{prueba} ({equipo})")
         nombres_nadadores = list(nadadores.keys())
        combinaciones_prueba = combinations(nombres_nadadores, 2)
        for comb in combinaciones_prueba:
            nadador1 = comb[0]
            nadador2 = comb[1]
            print(f"Comb {comb}")
            print(diccionario[equipo][prueba][comb[0]])
            print(diccionario[equipo][prueba][comb[1]])  """
            
#mismo loop pero solo para un equipo

""" for equipo, pruebas in diccionario.items():
    if equipo != "BOIRO":
        continue
    for prueba, nadadores in pruebas.items():
        print(f"{prueba} ({equipo})")
        nombres_nadadores = list(nadadores.keys())
        combinaciones_prueba = combinations(nombres_nadadores, 2)
        for comb in combinaciones_prueba:
            nadador1 = comb[0]
            nadador2 = comb[1]
            print(f"Comb {comb}",diccionario[equipo][prueba][comb[0]],diccionario[equipo][prueba][comb[1]])
 """

""" # Crear un diccionario para almacenar las combinaciones de nadadores
combinaciones_nadadores = {}

for equipo, pruebas in diccionario.items():
    for prueba, nadadores in pruebas.items():
        nombres_nadadores = list(nadadores.keys())
        combinaciones_prueba = combinations(nombres_nadadores, 2)
        combinaciones_nadadores[(prueba, equipo)] = list(combinaciones_prueba)

# Acceder a la combinación del equipo BOIRO para la prueba 50_esp_masc
prueba = "200_esp_masc"
equipo = "BOIRO"
combinaciones = combinaciones_nadadores[(prueba, equipo)]
print(f"Combinaciones para {prueba} ({equipo}): \n{combinaciones}")
print(f"Combinación 1: {combinaciones[0]}")
nadador1, nadador2 = combinaciones[0]
print(f"Tiempo de {nadador1}: {diccionario[equipo][prueba][nadador1][0]}")
print(f"Tiempo de {nadador2}: {diccionario[equipo][prueba][nadador2][0]}")

 """

# Diccionario para almacenar las combinaciones por equipo y prueba
combinaciones_equipo_prueba = {}

prueba_analizar = "200_esp_masc"


for equipo, pruebas in diccionario.items():
    
    for prueba, nadadores in pruebas.items():
        combinaciones_prueba = []
        nombres_nadadores = list(nadadores.keys())
        combinaciones_nadadores = list(combinations(nombres_nadadores, 2))
        combinaciones_prueba.extend(combinaciones_nadadores)

        combinaciones_equipo_prueba[(equipo, prueba)] = combinaciones_prueba
        #print(f"\n\nCombinaciones para {prueba} ({equipo}): \n{combinaciones_prueba}")

# Obtener las combinaciones entre combinaciones para BOIRO y RIAS
#print(combinaciones_equipo_prueba.keys())

#CON EL DICCIONARIO combinaciones_equipo_prueba puedo coger las combinaciones de cada equipo para cada prueba
# y luego hacer un producto cartesiano entre las combinaciones de cada equipo para cada prueba
# y así obtener todas las combinaciones posibles entre los equipos

#Esto se puede escalar metiendo en un bucle que recorra todas las pruebas y que vaya guardando las combinaciones
# de cada prueba en un diccionario, y luego hacer el producto cartesiano entre los diccionarios de cada prueba
# y asi obtener todas las combinaciones de la competicion


combinaciones_MOLEMOS = combinaciones_equipo_prueba[("MOLEMOS", prueba_analizar)]
combinaciones_BOIRO = combinaciones_equipo_prueba[("BOIRO", prueba_analizar)]
combinaciones_RIAS = combinaciones_equipo_prueba[("RIAS", prueba_analizar)]

#para coger solo dos combinaciones de cada equipo:
#combinaciones_totales = list(product(combinaciones_BOIRO[:2], combinaciones_RIAS[:2]))
combinaciones_totales = list(product(combinaciones_BOIRO, combinaciones_RIAS))
# Imprimir las combinaciones totales
    

for i, comb in enumerate(combinaciones_totales):
    
    puntos_boiro = 0
    puntos_rias = 0
    nadador0 = comb[0][0]
    nadador1 = comb[0][1]
    nadador2 = comb[1][0]
    nadador3 = comb[1][1]
    
    #print(f"Combinación {i + 1}: {comb}")
    
    tiempo0=diccionario['BOIRO'][prueba_analizar][nadador0][0]
    #print(f"Tiempo de {nadador1}: {diccionario['BOIRO']['50_esp_masc'][nadador1][0]}")
    tiempo1=diccionario['BOIRO'][prueba_analizar][nadador1][0]
    #print(f"Tiempo de {nadador2}: {diccionario['RIAS']['50_esp_masc'][nadador2][0]}")
    tiempo2=diccionario['RIAS'][prueba_analizar][nadador2][0]
    #print(f"Tiempo de {nadador3}: {diccionario['RIAS']['50_esp_masc'][nadador3][0]}")
    tiempo3=diccionario['RIAS'][prueba_analizar][nadador3][0]
    
    tiempos = [tiempo0, tiempo1, tiempo2, tiempo3]
    tiempos_ordenados = sorted(tiempos)
    puntos = {}
    for j in range(len(tiempos_ordenados)):
        if(j == 0):
            puntos[tiempos_ordenados[j]] = len(tiempos)+1
        puntos[tiempos_ordenados[j]] = len(tiempos) - j

    puntos0 = puntos[tiempo0]
    puntos1 = puntos[tiempo1]
    puntos2 = puntos[tiempo2]
    puntos3 = puntos[tiempo3]
    puntos_boiro=puntos0+puntos1

    puntos_rias=puntos2+puntos3
    if(puntos_boiro>=7) & (puntos_rias>=3):
        

        print(f"Combinación {i + 1}: {comb} Puntos BOIRO: {puntos_boiro} Puntos RIAS: {puntos_rias}")


    