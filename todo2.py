import argparse
import itertools
import csv

# Función para leer los tiempos de un archivo CSV y devolver un diccionario de equipos y tiempos
def leer_tiempos(archivo):
    equipos = {}
    with open(archivo, newline='') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            nombre = fila['Nombre']
            tiempo = float(fila['Tiempo'])
            equipo = fila['Equipo']
            if equipo not in equipos:
                equipos[equipo] = []
            equipos[equipo].append((nombre, tiempo))
    return equipos

# Función para generar todas las posibles combinaciones de nadadores, teniendo en cuenta las restricciones
def generar_combinaciones(nadadores_equipo1, nadadores_equipo2, nadadores_equipo3):
    # Generar todas las posibles combinaciones de nadadores de cada equipo
    combinaciones_equipo1 = itertools.combinations(nadadores_equipo1, 4)
    combinaciones_equipo2 = itertools.combinations(nadadores_equipo2, 2)
    combinaciones_equipo3 = itertools.combinations(nadadores_equipo3, 2)
    # Generar todas las posibles combinaciones de nadadores, teniendo en cuenta las restricciones
    combinaciones = []
    for comb1 in combinaciones_equipo1:
        for comb2 in combinaciones_equipo2:
            for comb3 in combinaciones_equipo3:
                nombres_comb = set([n for n, t in comb1 + comb2 + comb3])
                if len(nombres_comb) == 8 and all([n in nombres_comb for n, t in nadadores_equipo1]):
                    combinaciones.append((comb1,
