import itertools

# Input de tiempos de las seis personas
tiempos = [int(input("Tiempo de la persona " + str(i+1) + ": ")) for i in range(6)]

# Generación de todas las combinaciones posibles de grupos de dos
combinaciones = itertools.combinations(tiempos, 2)

# Impresión de las combinaciones
for combinacion in combinaciones:
    print(combinacion)
