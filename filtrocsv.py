import csv

# Lista de los nombres de los archivos de entrada y salida
input_files = ['equipo1.csv', 'equipo2.csv', 'equipo3.csv']
output_file = 'equipos.csv'

# Lista con las etiquetas de los equipos
team_labels = ['Equipo 1:', 'Equipo 2:', 'Equipo 3:']

# Abrir archivo de salida
with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    
    # Escribir encabezado
    writer.writerow(['Nombre', 'Tiempo', 'Equipo'])
    
    # Iterar sobre los archivos de entrada
    for i, input_file in enumerate(input_files):
        # Leer datos del archivo de entrada
        with open(input_file, 'r', encoding='utf-8') as f_in:
            reader = csv.reader(f_in)
            next(reader)  # saltar la primera fila
            
            
            # Escribir datos de cada fila
            for row in reader:
                writer.writerow([row[1], row[5], 'Equipo ' + str(i+1)])
                