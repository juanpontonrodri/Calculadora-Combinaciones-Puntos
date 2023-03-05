import csv
from itertools import combinations

# Cargar los datos de los tiempos de las pruebas desde los archivos CSV
nombres_pruebas=["series/50_esp_masc_tiempos.csv","series/100_esp_masc_tiempos.csv"]
prueba1 = []
with open(nombres_pruebas[0], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prueba1.append(row)

prueba2 = []
with open(nombres_pruebas[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prueba2.append(row)

# Definir las constantes del problema
NUM_EQUIPOS = 3
NUM_PRUEBAS = 2
NUM_NADADORES_PRUEBA = 2
PUNTUACIONES = [7, 5, 4, 3, 2, 1]

# Generar todas las posibles combinaciones de nadadores
combinaciones = []
for i in range(NUM_EQUIPOS):
    nadadores = [p for p in prueba1 if p['Equipo'] == f'Equipo {i+1}'] + \
                [p for p in prueba2 if p['Equipo'] == f'Equipo {i+1}']
    for c in combinations(nadadores, NUM_NADADORES_PRUEBA * NUM_PRUEBAS):
        combinaciones.append(list(c))

# Calcular la puntuación para cada combinación
puntuaciones = []
for c in combinaciones:
    puntuacion = 0
    for i in range(NUM_PRUEBAS):
        prueba = c[i*NUM_NADADORES_PRUEBA:(i+1)*NUM_NADADORES_PRUEBA]
        tiempos = [float(p['Tiempo']) for p in prueba]
        tiempos.sort()
        for j, tiempo in enumerate(tiempos):
            puntuacion += PUNTUACIONES[j] * (tiempos.index(tiempo) + 1)
    puntuaciones.append(puntuacion)

# Seleccionar la combinación con la puntuación máxima
indice_max = puntuaciones.index(max(puntuaciones))
combinacion_maxima = combinaciones[indice_max]

# Escribir la combinación máxima en un archivo CSV
with open('combinacion_maxima.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(NUM_PRUEBAS):
        prueba = combinacion_maxima[i*NUM_NADADORES_PRUEBA:(i+1)*NUM_NADADORES_PRUEBA]
        writer.writerow([nombres_pruebas[i][7:-12]])
        for nadador in prueba:
            writer.writerow([nadador['Nombre'], nadador['Tiempo'], nadador['Equipo']])
