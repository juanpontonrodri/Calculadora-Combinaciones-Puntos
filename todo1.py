import argparse
import itertools
import csv

parser = argparse.ArgumentParser(description='Encuentra la mejor combinación de nadadores.')
parser.add_argument('archivo_entrada', type=str, help='Archivo de texto con los tiempos de los nadadores')


args = parser.parse_args()
nombre_salida="./todo/"+"todo1" + ".csv"
# Lectura de tiempos de archivo CSV
equipos = {}
with open(args.archivo_entrada, newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nombre = fila['Nombre']
        tiempo = float(fila['Tiempo'])
        equipo = fila['Equipo']
        if equipo not in equipos:
            equipos[equipo] = []
        equipos[equipo].append((nombre, tiempo))

# Generación de todas las combinaciones posibles de grupos de dos para cada equipo
combinaciones_por_equipo = []
for equipo in equipos.values():
    combinaciones = itertools.combinations(equipo, 2)
    combinaciones_por_equipo.append(list(combinaciones))


# Bucle para combinaciones
puntuaciones_medias = []
for combinacion_equipo1 in combinaciones_por_equipo[0]:
    puntuacion_total = 0
    for combinacion_equipo2 in combinaciones_por_equipo[1]:
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
            puntuaciones = [7, 5, 4, 3, 2, 1]
            puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
            puntuacion_total += puntuacion_equipo1


# Aqui escribiremos que nadadores participaran en cada prueba para alcanzar el maximo numero de puntos y los puntos sumados por cada uno de ellos en cada prueba
with open(nombre_salida, 'w',encoding='utf-8', newline='') as archivo:
    writer = csv.writer(archivo)
   
