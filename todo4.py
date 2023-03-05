import itertools
import csv

def generate_combinations():
    # Obtener los tiempos de los nadadores del CSV de la primera prueba
    times_1 = {}
    with open('prueba_1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Nombre']
            time = int(row['Tiempo'])
            team = row['Equipo']
            if team not in times_1:
                times_1[team] = []
            times_1[team].append((name, time))

    # Obtener los tiempos de los nadadores del CSV de la segunda prueba
    times_2 = {}
    with open('prueba_2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Nombre']
            time = int(row['Tiempo'])
            team = row['Equipo']
            if team not in times_2:
                times_2[team] = []
            times_2[team].append((name, time))

    # Generar todas las posibles combinaciones de nadadores
    combinations = []
    for team in times_1:
        # Generar todas las posibles parejas de nadadores del equipo para la primera prueba
        pairs_1 = list(itertools.combinations(times_1[team], 2))
        # Generar todas las posibles parejas de nadadores del equipo para la segunda prueba
        pairs_2 = list(itertools.combinations(times_2[team], 2))
        # Generar todas las posibles combinaciones de parejas de nadadores (una por prueba)
        for pair_1 in pairs_1:
            for pair_2 in pairs_2:
                # Verificar que los nadadores no se repitan en las dos pruebas
                if set(pair_1 + pair_2) == set(pair_1) | set(pair_2):
                    combinations.append((pair_1, pair_2, team))

    return combinations

def calculate_score(pair_1, pair_2):
    # Calcular la puntuación de una combinación de parejas de nadadores
    scores_1 = [7, 5, 4, 3, 2, 1]
    times_1 = sorted([time for name, time in pair_1])
    score_1 = sum([scores_1[i] for i in range(len(times_1))])  # puntuación de la primera prueba

    scores_2 = [7, 5, 4, 3, 2, 1]
    times_2 = sorted([time for name, time in pair_2])
    score_2 = sum([scores_2[i] for i in range(len(times_2))])  # puntuación de la segunda prueba

    return score_1 + score_2

def get_best_combination():
    combinations = generate_combinations()
    best_score = 0
    best_combination = None
    for combination in combinations:
        score = calculate_score(combination[0], combination[1])
        if score > best_score:
            best_score = score
            best_combination = combination
    return best_combination
