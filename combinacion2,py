import itertools

# Diccionario de equipos, pruebas y nadadores
equipos = {
    "Equipo1": {
        "prueba1": ["nadador1", "nadador2", "nadador3"],
        "prueba2": ["nadador4", "nadador5", "nadador6"]
    },
    "Equipo2": {
        "prueba1": ["nadador7", "nadador8", "nadador9"],
        "prueba2": ["nadador10", "nadador11", "nadador12"]
    },
    "Equipo3": {
        "prueba1": ["nadador13", "nadador14", "nadador15"],
        "prueba2": ["nadador16", "nadador17", "nadador18"]
    }
}

# Función para generar las combinaciones posibles de nadadores para una prueba de un equipo
def generar_combinaciones_nadadores(nadadores):
    combinaciones_nadadores = list(itertools.combinations(nadadores, 2))
    return combinaciones_nadadores

# Función para generar todas las combinaciones posibles de nadadores para cada prueba y equipo
def generar_combinaciones():
    combinaciones = []
    for equipo, pruebas in equipos.items():
        combinaciones_equipo = []
        for prueba, nadadores in pruebas.items():
            combinaciones_prueba = generar_combinaciones_nadadores(nadadores)
            combinaciones_equipo.append(combinaciones_prueba)
        combinaciones.append(combinaciones_equipo)
    return combinaciones

# Función para calcular la puntuación de una combinación de nadadores
def calcular_puntuacion(nadadores):
    puntuacion = 0
    for nadador in nadadores:
        puntuacion += nadador
    return puntuacion

# Generar todas las combinaciones posibles de nadadores para cada prueba y equipo
combinaciones = generar_combinaciones()

# Loop anidado para generar todas las posibles combinaciones de nadadores para todas las pruebas y equipos
for c1 in combinaciones[0][0]:
    for c2 in combinaciones[0][1]:
        if not set(c1).intersection(set(c2)): # Comprobamos que no se use el mismo nadador en dos pruebas diferentes
            for c3 in combinaciones[1][0]:
                if not set(c1).intersection(set(c3)) and not set(c2).intersection(set(c3)):
                    for c4 in combinaciones[1][1]:
                        if not set(c1).intersection(set(c4)) and not set(c2).intersection(set(c4)) and not set(c3).intersection(set(c4)):
                            for c5 in combinaciones[2][0]:
                                if not set(c1).intersection(set(c5)) and not set(c2).intersection(set(c5)) and not set(c3).intersection(set(c5)) and not set(c4).intersection(set(c5)):
                                    for c6 in combinaciones[2][1]:
                                        if not set(c1).intersection(set(c6)) and not set(c2).intersection(set(c6)) and not set(c3).intersection(set(c6)) and not set(c4).intersection(set(c6)) and not set(c5).intersection(set(c6)):
                                            nadadores = c1 + c2 + c3 + c4 + c5 + c6
                                            puntuacion = calcular_puntuacion(nadadores)
                                            print
