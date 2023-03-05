"""MUY PROMETEDOR"""

import itertools

# Input de tiempos para cada equipo
equipos = []
for i in range(3):
    equipo = [int(input("Tiempo del nadador " + str(j+1) + " del equipo " + str(i+1) + ": ")) for j in range(6)]
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
            tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3))
            puntuaciones = [6, 5, 4, 3, 2, 1]
            puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
            if puntuacion_equipo1 > max_puntuacion:
                max_puntuacion = puntuacion_equipo1
                mejor_combinacion = (combinacion_equipo1, combinacion_equipo2, combinacion_equipo3)

# Impresión de la combinación con la mayor puntuación para el primer equipo
print("Mejor combinación para el primer equipo:")
print("Equipo 1: ", mejor_combinacion[0])
print("Equipo 2: ", mejor_combinacion[1])
print("Equipo 3: ", mejor_combinacion[2])
print("Puntuación para el primer equipo: ", max_puntuacion)
