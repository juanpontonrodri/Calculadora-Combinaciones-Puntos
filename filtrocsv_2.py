import csv
import os

# Carpeta con los archivos de entrada y salida
folder_path = './tiempos/'

# Obtener los nombres de los archivos en la carpeta
file_names = os.listdir(folder_path)

# Filtrar los nombres de los archivos por grupo
groups = {}
for name in file_names:
    parts = name.split('_')
    group_name = '_'.join(parts[:-1]) + '_tiempos.csv'
    if group_name not in groups:
        groups[group_name] = []
    groups[group_name].append(name)

# Iterar sobre cada grupo
for group_name, file_names in groups.items():
    # Abrir archivo de salida correspondiente al grupo
    with open(os.path.join(folder_path, group_name), 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)

        # Escribir encabezado
        writer.writerow(['Nombre', 'Tiempo', 'Equipo'])

        # Iterar sobre los archivos de entrada del grupo
        for i, input_file in enumerate(file_names):
            # Leer datos del archivo de entrada
            with open(os.path.join(folder_path, input_file), 'r', encoding='utf-8') as f_in:
                reader = csv.reader(f_in)
                next(reader)  # saltar la primera fila

                # Escribir datos de cada fila
                for row in reader:
                    writer.writerow([row[1], row[5], 'Equipo ' + str(i+1)])
