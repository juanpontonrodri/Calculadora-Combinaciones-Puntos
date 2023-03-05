// Paso 1: Crear matriz de tiempos
tiempos = [[t_11, t_12, ..., t_1n],
           [t_21, t_22, ..., t_2n],
           ...
           [t_m1, t_m2, ..., t_mn]]

// Paso 2: Crear matriz de puntuaciones
puntuaciones = [[7, 5, 4, 3, 2, 1],
                [7, 5, 4, 3, 2, 1],
                ...
                [7, 5, 4, 3, 2, 1]]

// Paso 3: Crear matriz de equipos
equipos = [[e_11, e_12, ..., e_1n],
           [e_21, e_22, ..., e_2n],
           ...
           [e_m1, e_m2, ..., e_mn]]

// Paso 4: Crear matriz de puntos
puntos = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          ...
          [0, 0, 0]]

// Paso 5: Crear lista de combinaciones posibles de pruebas
combinaciones = []
for cada participante:
    combinaciones_participante = todas_las_combinaciones_de_4_pruebas_individuales
    combinaciones.append(combinaciones_participante)

// Paso 6: Calcular puntos para cada combinación de pruebas
puntos_maximos = 0
mejor_combinacion = []
for cada combinacion in combinaciones:
    puntos_combinacion = [0, 0, 0]
    for cada prueba in combinacion:
        for cada participante in prueba:
            puntos_combinacion[equipos[prueba][participante]] += puntuaciones[prueba][participante]
    puntos_equipo = sumar_todos_los_puntos_de_la_combinacion_para_tu_equipo(puntos_combinacion)
    if puntos_equipo > puntos_maximos:
        puntos_maximos = puntos_equipo
        mejor_combinacion = combinacion

