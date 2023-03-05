import itertools
import csv

nombre_entrada=["series/50_esp_masc_tiempos.csv","series/100_esp_masc_tiempos.csv"]
nombre_salida="./todo/"+args.archivo_entrada[7:-12] + ".csv"
# Lectura de tiempos de archivo CSV
equipos = {}
with open(nombre_entrada[0], newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nombre = fila['Nombre']
        tiempo = float(fila['Tiempo'])
        equipo = fila['Equipo']
        if equipo not in equipos:
            equipos[equipo] = []
        equipos[equipo].append((nombre, tiempo,nombre_entrada[0]))

with open(nombre_entrada[1], newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nombre = fila['Nombre']
        tiempo = float(fila['Tiempo'])
        equipo = fila['Equipo']
        if equipo not in equipos:
            equipos[equipo] = []
        equipos[equipo].append((nombre, tiempo,nombre_entrada[1]))
        
# Generación de todas las combinaciones posibles de grupos de dos para cada equipo
combinaciones_por_equipo = []
for equipo in equipos.values():
    combinaciones = itertools.combinations(equipo, 2)
    combinaciones_por_equipo.append(list(combinaciones))


# Bucle para encontrar las 6 combinaciones con la mayor puntuación media para el primer equipo
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


# Escritura de la tabla de resultados para la segunda parte del problema en un archivo de salida diferente
with open(nombre_salida, 'w',encoding='utf-8', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Combinación", "Equipo 1", "Puntuación media"])
    for idx, mejor_combinacion in enumerate(mejores_combinaciones_medias):
        equipo1 = ", ".join([n[0] for n in mejor_combinacion[0]])
        writer.writerow([idx+1, equipo1, mejor_combinacion[1]])
    # Escritura de la tabla de resultados para el segundo equipo
    writer.writerow(["Combinación", "Equipo 2", "Puntuación media"])
    for idx2, mejor_combinacion2 in enumerate(mejores_combinaciones_medias_equipo2):
        equipo2 = ", ".join([n[0] for n in mejor_combinacion2[0]])
        writer.writerow([idx2+1, equipo2, mejor_combinacion2[1]])
        
    writer.writerow(["Combinación", "Equipo 3", "Puntuación media"])
    for idx3, mejor_combinacion3 in enumerate(mejores_combinaciones_medias_equipo3):
        equipo3 = ", ".join([n[0] for n in mejor_combinacion3[0]])
        writer.writerow([idx3+1, equipo3, mejor_combinacion3[1]])
