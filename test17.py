#se aplica a un directorio entero


import argparse
import itertools
import csv
import os
import pandas as pd

parser = argparse.ArgumentParser(description='Encuentra la mejor combinación de nadadores.')
parser.add_argument('directorio_entrada', type=str, help='Directorio que contiene los archivos de texto con los tiempos de los nadadores')

args = parser.parse_args()

# Create a list to store the output file paths
output_files = []



for filename in os.listdir(args.directorio_entrada):
    if filename.endswith(".csv"):
        archivo_entrada = os.path.join(args.directorio_entrada, filename)
        nombre_salida = os.path.join("./medias", os.path.splitext(filename)[0] + "_salida.csv")
        output_files.append(nombre_salida)

        # Lectura de tiempos de archivo CSV
        equipos = {}
        with open(archivo_entrada, newline='') as archivo:
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


        # Bucle para encontrar las 10 combinaciones con la mayor puntuación media para el primer equipo
        puntuaciones_medias = []
        for combinacion_equipo1 in combinaciones_por_equipo[0]:
            puntuacion_total = 0
            for combinacion_equipo2 in combinaciones_por_equipo[1]:
                for combinacion_equipo3 in combinaciones_por_equipo[2]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
                    puntuacion_total += puntuacion_equipo1
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[1]) * len(combinaciones_por_equipo[2]))
            puntuaciones_medias.append((combinacion_equipo1, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 6 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias = puntuaciones_medias[:10]

        # Bucle para encontrar las 10 mejores puntuaciones medias para el segundo equipo
        puntuaciones_medias_equipo2 = []
        for combinacion_equipo2 in combinaciones_por_equipo[1]:
            puntuacion_total = 0
            for combinacion_equipo1 in combinaciones_por_equipo[0]:
                for combinacion_equipo3 in combinaciones_por_equipo[2]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo2 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo2])
                    puntuacion_total += puntuacion_equipo2
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[0]) * len(combinaciones_por_equipo[2]))
            puntuaciones_medias_equipo2.append((combinacion_equipo2, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias_equipo2.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 10 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias_equipo2 = puntuaciones_medias_equipo2[:10]


        # Bucle para encontrar las 10 mejores puntuaciones medias para el tercer equipo
        puntuaciones_medias_equipo3 = []
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            puntuacion_total = 0
            for combinacion_equipo1 in combinaciones_por_equipo[0]:
                for combinacion_equipo2 in combinaciones_por_equipo[1]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo3 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo3])
                    puntuacion_total += puntuacion_equipo3
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[0]) * len(combinaciones_por_equipo[1]))
            puntuaciones_medias_equipo3.append((combinacion_equipo3, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias_equipo3.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 10 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias_equipo3 = puntuaciones_medias_equipo3[:10]

        # Escritura de la tabla de resultados para la segunda parte del problema en un archivo de salida diferente
        with open(nombre_salida, 'w',encoding='utf-8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Combinación", "MOLEMOS", "Puntuación media"])
            for idx, mejor_combinacion in enumerate(mejores_combinaciones_medias):
                equipo1 = ", ".join([n[0] for n in mejor_combinacion[0]])
                writer.writerow([idx+1, equipo1, mejor_combinacion[1]])
            # Escritura de la tabla de resultados para el segundo equipo
            writer.writerow(["Combinación", "BOIRO", "Puntuación media"])
            for idx2, mejor_combinacion2 in enumerate(mejores_combinaciones_medias_equipo2):
                equipo2 = ", ".join([n[0] for n in mejor_combinacion2[0]])
                writer.writerow([idx2+1, equipo2, mejor_combinacion2[1]])
                
            writer.writerow(["Combinación", "RIAS", "Puntuación media"])
            for idx3, mejor_combinacion3 in enumerate(mejores_combinaciones_medias_equipo3):
                equipo3 = ", ".join([n[0] for n in mejor_combinacion3[0]])
                writer.writerow([idx3+1, equipo3, mejor_combinacion3[1]])
