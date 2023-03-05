"""El mejor en teoria"""

import itertools

# Lectura de tiempos de archivo de texto
equipos = []
for i in range(3):
    equipo = []
    with open("tiempos.txt") as archivo:
        lineas = archivo.readlines()[i*7:(i+1)*7]
        for linea in lineas[1:]:
            nombre, tiempo = linea.split()
            equipo.append((nombre, int(tiempo)))
    equipos.append(equipo)

# Generación de todas las combinaciones posibles de grupos de dos para cada equipo
combinaciones_por_equipo = []
for equipo in equipos:
    combinaciones = itertools.combinations(equipo, 2)
    combinaciones_por_equipo.append(list(combinaciones))

# Bucle para encontrar la combinación con la mayor puntuación para el primer equipo
max_puntuacion = 0
mejor_combinacion = None
for combinacion_equipo1 in combinaciones_por_equipo[0]:
    for combinacion_equipo2 in combinaciones_por_equipo[1]:
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            nadadores = [combinacion_equipo1[0], combinacion_equipo1[1], combinacion_equipo2[0], combinacion_equipo2[1], combinacion_equipo3[0], combinacion_equipo3[1]]
            tiempos = sorted([nadador[1] for nadador in nadadores])
            puntuaciones = [6, 5, 4, 3, 2, 1]
            puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in [nadador[1] for nadador in combinacion_equipo1]])
            if puntuacion_equipo1 > max_puntuacion:
                max_puntuacion = puntuacion_equipo1
                mejor_combinacion = [(nadador[0], nadador[1]) for nadador in combinacion_equipo1] + [(nadador[0], nadador[1]) for nadador in combinacion_equipo2] + [(nadador[0], nadador[1]) for nadador in combinacion_equipo3]

# Impresión de la combinación con la mayor puntuación para el primer equipo
print("Mejor combinación para el primer equipo:")
print("Equipo 1: ", [nadador[0] + ' ' + str(nadador[1]) for nadador in mejor_combinacion[:2]])
print("Equipo 2: ", [nadador[0] + ' ' + str(nadador[1]) for nadador in mejor_combinacion[2:4]])
print("Equipo 3: ", [nadador[0] + ' ' + str(nadador[1]) for nadador in mejor_combinacion[4:]])
print("Puntuación para el primer equipo: ", max_puntuacion)
