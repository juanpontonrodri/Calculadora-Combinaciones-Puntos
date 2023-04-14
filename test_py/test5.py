"""Lo mismo que el 4 pero leyendo de un archivo:
Equipo 1:
Juan 3456
JAvier 443635

Equipo 2:
Manuel 3454
"""

import itertools

# Lectura de tiempos de archivo de texto
equipos = []
for i in range(3):
    equipo = []
    with open("tiempos.txt") as archivo:
        lineas = archivo.readlines()[i*7:(i+1)*7]
        for linea in lineas[1:]:
            nombre, tiempo = linea.split()
            equipo.append(int(tiempo))
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
""" 




# Lectura de nombres de archivo de texto

nombres_por_equipo = []
for i in range(3):
    nombres = []
    with open("tiempos.txt") as archivo:
        lineas = archivo.readlines()[i*7:(i+1)*7]
        for linea in lineas[1:]:
            nombre, tiempo = linea.split()
            nombres.append(nombre)
    nombres_por_equipo.append(nombres)

# Impresión de los nombres de los nadadores de la mejor combinación para el primer equipo
print("Mejor combinación para el primer equipo:")
nombres_equipo1 = [nombres_por_equipo[0][equipos[0].index(tiempo)] for tiempo in mejor_combinacion[0]]
nombres_equipo2 = [nombres_por_equipo[1][equipos[1].index(tiempo)] for tiempo in mejor_combinacion[1]]
nombres_equipo3 = [nombres_por_equipo[2][equipos[2].index(tiempo)] for tiempo in mejor_combinacion[2]]
print("Equipo 1: ", nombres_equipo1)
print("Equipo 2: ", nombres_equipo2)
print("Equipo 3: ", nombres_equipo3)
print("Puntuación para el primer equipo: ", max_puntuacion)
 """