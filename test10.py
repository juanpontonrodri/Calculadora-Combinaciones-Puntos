import argparse
import itertools
import csv

parser = argparse.ArgumentParser(description='Encuentra la mejor combinación de nadadores.')
parser.add_argument('archivo_entrada', type=str, help='Archivo de texto con los tiempos de los nadadores')
parser.add_argument('archivo_salida', type=str, help='Archivo donde se guardará la tabla con los resultados')



args = parser.parse_args()

# Lectura de tiempos de archivo de texto
equipos = []
with open(args.archivo_entrada) as archivo:
    lineas = archivo.readlines()
    i = 0
    while i < len(lineas):
        if lineas[i].startswith('Equipo'):
            equipo = []
            i += 1
            while i < len(lineas) and not lineas[i].startswith('Equipo'):
                if lineas[i].strip():  # Verificar si la línea está vacía
                    nombre, tiempo = lineas[i].split()
                    equipo.append((nombre, int(tiempo)))
                i += 1
            equipos.append(equipo)
        else:
            i += 1


# Generación de todas las combinaciones posibles de grupos de dos para cada equipo
combinaciones_por_equipo = []
for equipo in equipos:
    combinaciones = itertools.combinations(equipo, 2)
    combinaciones_por_equipo.append(list(combinaciones))

# Bucle para encontrar la(s) combinación(es) con la mayor puntuación para el primer equipo
max_puntuacion = 0
mejores_combinaciones = []
for combinacion_equipo1 in combinaciones_por_equipo[0]:
    for combinacion_equipo2 in combinaciones_por_equipo[1]:
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
            puntuaciones = [6, 5, 4, 3, 2, 1]
            puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
            if puntuacion_equipo1 > max_puntuacion:
                max_puntuacion = puntuacion_equipo1
                mejores_combinaciones = [(combinacion_equipo1, combinacion_equipo2, combinacion_equipo3)]
            elif puntuacion_equipo1 == max_puntuacion:
                mejores_combinaciones.append((combinacion_equipo1, combinacion_equipo2, combinacion_equipo3))



# Bucle para encontrar las 6 combinaciones con la mayor puntuación media para el primer equipo
puntuaciones_medias = []
for combinacion_equipo1 in combinaciones_por_equipo[0]:
    puntuacion_total = 0
    for combinacion_equipo2 in combinaciones_por_equipo[1]:
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
            puntuaciones = [6, 5, 4, 3, 2, 1]
            puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
            puntuacion_total += puntuacion_equipo1
    puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[1]) * len(combinaciones_por_equipo[2]))
    puntuaciones_medias.append((combinacion_equipo1, puntuacion_media))

# Ordenar combinaciones por puntuación media
puntuaciones_medias.sort(key=lambda x: x[1], reverse=True)

# Seleccionar las 6 combinaciones con la puntuación media más alta
mejores_combinaciones_medias = puntuaciones_medias[:6]

# Escritura de la tabla de resultados para la primera parte del problema en el archivo de salida
with open(args.archivo_salida, 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Combinación", "Equipo 1", "Equipo 2", "Equipo 3", "Puntuación"])
    for idx, mejor_combinacion in enumerate(mejores_combinaciones):
        equipo1 = ", ".join([n[0] for n in mejor_combinacion[0]])
        equipo2 = ", ".join([n[0] for n in mejor_combinacion[1]])
        equipo3 = ", ".join([n[0] for n in mejor_combinacion[2]])
        writer.writerow([idx+1, equipo1, equipo2, equipo3, max_puntuacion])

# Escritura de la tabla de resultados para la segunda parte del problema en un archivo de salida diferente
with open(args.archivo_salida, 'a', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow('\n')
    writer.writerow(["Combinación", "Equipo 1", "Puntuación media"])
    for idx, mejor_combinacion in enumerate(mejores_combinaciones_medias):
        equipo1 = ", ".join([n[0] for n in mejor_combinacion[0]])
        writer.writerow([idx+1, equipo1, mejor_combinacion[1]])
