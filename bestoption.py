import csv

# Lee los datos del archivo CSV
with open('medias.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    equipos = {}
    for row in reader:
        if row[0] == "Combinación":
            equipo = row[1]
            equipos[equipo] = []
        else:
            combinacion = row[0]
            puntuacion = float(row[2])
            equipos[equipo].append((combinacion, puntuacion))

# Calcula la media de las puntuaciones medias de las combinaciones del equipo 2 y 3
media_equipo2 = sum([p[1] for p in equipos["Equipo 2"]]) / len(equipos["Equipo 2"])
media_equipo3 = sum([p[1] for p in equipos["Equipo 3"]]) / len(equipos["Equipo 3"])

# Encuentra la mejor combinación para el equipo 1 que sea superior a la media del equipo 2
mejor_combinacion2 = None
mejor_puntuacion2 = 0
for combinacion, puntuacion in equipos["Equipo 1"]:
    if puntuacion >= media_equipo2 and (mejor_combinacion2 is None or puntuacion < mejor_puntuacion2):
        mejor_combinacion2 = combinacion
        mejor_puntuacion2 = puntuacion
    elif puntuacion < media_equipo2 and (mejor_combinacion2 is None or mejor_puntuacion2 < media_equipo2):
        mejor_combinacion2 = media_equipo2
        mejor_puntuacion2 = media_equipo2

# Encuentra la mejor combinación para el equipo 1 que sea superior a la media del equipo 3
mejor_combinacion3 = None
mejor_puntuacion3 = 0
for combinacion, puntuacion in equipos["Equipo 1"]:
    if puntuacion >= media_equipo3 and (mejor_combinacion3 is None or puntuacion < mejor_puntuacion3):
        mejor_combinacion3 = combinacion
        mejor_puntuacion3 = puntuacion
    elif puntuacion < media_equipo3 and (mejor_combinacion3 is None or mejor_puntuacion3 < media_equipo3):
        mejor_combinacion3 = media_equipo3
        mejor_puntuacion3 = media_equipo3


#with open('medias.csv', 'a',encoding='utf-8', newline='') as archivo:
#    writer = csv.writer(archivo)
#    writer.writerow(["La mejor combinacion para vencer al 2 es la número",mejor_combinacion2,"con una puntuación media de", mejor_puntuacion2])
#    writer.writerow(["La mejor combinacion para vencer al 3 es la número",mejor_combinacion3,"con una puntuación media de", mejor_puntuacion3])

# Imprime la mejor combinación encontrada
print(f"La mejor combinación para ganar al 2 es la número {mejor_combinacion2} con una puntuación media de {mejor_puntuacion2}.")
print(f"La mejor combinación para ganar al 3 es la número {mejor_combinacion3} con una puntuación media de {mejor_puntuacion3}.")

