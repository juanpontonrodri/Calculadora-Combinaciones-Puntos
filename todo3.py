import csv

# leer el archivo CSV de la primera prueba
with open('prueba1.csv') as f:
    reader = csv.reader(f)
    next(reader) # saltar la primera fila
    equipo1_prueba1 = []
    equipo2_prueba1 = []
    equipo3_prueba1 = []
    for row in reader:
        nombre = row[0]
        tiempo = int(row[1])
        equipo = row[2]
        if equipo == 'Equipo 1':
            equipo1_prueba1.append((nombre, tiempo))
        elif equipo == 'Equipo 2':
            equipo2_prueba1.append((nombre, tiempo))
        elif equipo == 'Equipo 3':
            equipo3_prueba1.append((nombre, tiempo))

# leer el archivo CSV de la segunda prueba
with open('prueba2.csv') as f:
    reader = csv.reader(f)
    next(reader) # saltar la primera fila
    equipo1_prueba2 = []
    equipo2_prueba2 = []
    equipo3_prueba2 = []
    for row in reader:
        nombre = row[0]
        tiempo = int(row[1])
        equipo = row[2]
        if equipo == 'Equipo 1':
            equipo1_prueba2.append((nombre, tiempo))
        elif equipo == 'Equipo 2':
            equipo2_prueba2.append((nombre, tiempo))
        elif equipo == 'Equipo 3':
            equipo3_prueba2.append((nombre, tiempo))

# generar todas las combinaciones posibles de nadadores para cada equipo
combinaciones_equipo1 = []
combinaciones_equipo2 = []
combinaciones_equipo3 = []

# combinaciones para la primera prueba
for i in range(len(equipo1_prueba1)):
    for j in range(i+1, len(equipo1_prueba1)):
        combinaciones_equipo1.append([equipo1_prueba1[i], equipo1_prueba1[j]])

for i in range(len(equipo2_prueba1)):
    for j in range(i+1, len(equipo2_prueba1)):
        combinaciones_equipo2.append([equipo2_prueba1[i], equipo2_prueba1[j]])

for i in range(len(equipo3_prueba1)):
    for j in range(i+1






def calcular_puntuacion(tiempo1, tiempo2):
    puntuacion1 = 7 if tiempo1 == min(tiempo1, tiempo2) else 5
    puntuacion2 = 7 if tiempo2 == min(tiempo1, tiempo2) else 5
    return puntuacion1 + puntuacion2


mejor_combinacion = max(combinaciones, key=lambda comb: sum(calcular_puntuacion(tiempo1, tiempo2) for (nadador1, tiempo1), (nadador2, tiempo2) in comb))
with open('combinacion_optima.csv', 'w') as archivo:
    escritor = csv.writer(archivo)
    for (nadador1, _), (nadador2, _) in mejor_combinacion:
        escritor.writerow([nadador1, nadador2])
