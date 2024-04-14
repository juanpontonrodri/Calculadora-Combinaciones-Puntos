#corrige la comilla de la licenacia en la posicion 9 y ewlimina la ulitma de cada liena
import os
import csv
import sys
dir_path = sys.argv[1]

for filename in os.listdir(dir_path):
    if filename.endswith("1.csv"):  # Filtrar solo archivos que terminan en "masc_1"
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if len(line) > 10:  # Solo modifica las líneas con más de 9 caracteres
                    new_line = line[:9] + '"' + line[9:-2] + '\n'  # Agrega " después del noveno carácter y elimina el último carácter
                    file.write(new_line)
                else:
                    file.write(line[:-1] + '\n')  # Si la línea es más corta que 9 caracteres, solo elimina el último carácter
            file.truncate()