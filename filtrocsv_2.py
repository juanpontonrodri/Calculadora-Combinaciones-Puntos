# Description: Filtrar archivos csv de la carpeta de entrada y generar un archivo csv por prueba en la carpeta de salida


import csv
import os
import re
# Carpeta con los archivos de entrada y salida
folder_path = './tiempos/'
folder_path_out = './series/'

# Obtener los nombres de los archivos en la carpeta
file_names = os.listdir(folder_path)



# Filtrar los nombres de los archivos por grupo y número de archivo
groups = {}
for name in file_names:
    parts = name.split('_')
    group_name = '_'.join(parts[:-1]) + '_tiempos.csv'
    if group_name not in groups:
        groups[group_name] = []
    
    # Verificar si el archivo cumple con las condiciones deseadas
    if re.search(r".*(_1|_2|_3).csv", name):
        groups[group_name].append(name)


# Iterar sobre cada grupo
for group_name, file_names in groups.items():
    # Abrir archivo de salida correspondiente al grupo
    with open(os.path.join(folder_path_out, group_name), 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)

        # Escribir encabezado
        writer.writerow(['Nombre', 'Tiempo', 'Equipo', 'Prueba'])

        # Iterar sobre los archivos de entrada del grupo
        for i, input_file in enumerate(sorted(file_names)):
            # Leer datos del archivo de entrada
            print(input_file)
            nombre_prueba = input_file[:-6]
            
            with open(os.path.join(folder_path, input_file), 'r', encoding='utf-8-sig') as f_in:
                reader = csv.reader(f_in)

                # Escribir datos de cada fila
                for row in reader:
                    tiempo = row[5].replace(':', '')
                    tiempo = tiempo.replace('.', '')
                    if i==0:
                        writer.writerow([row[1], tiempo, "MOLEMOS", nombre_prueba])
                    if i==1:
                        writer.writerow([row[1], tiempo, "BOIRO",nombre_prueba])
                    if i==2:
                        writer.writerow([row[1], tiempo, "RIAS",nombre_prueba])
                        
                    
