#Description: Separar un archivo CSV en varios archivos CSV, uno por cada tipo de prueba
#Es el inverso de la operacion de unircsv.py
#Si se comentan la linea de .drop(columns=["Prueba"]) se obtiene un archivo CSV con una columna extra con el tipo de prueba

import os
import pandas as pd
import sys

# Nombre del archivo CSV a leer
csv_file = sys.argv[1]

# Nombre del directorio a crear
directory_name = os.path.splitext(csv_file)[0] + "_sep"

# Crear el directorio si no existe
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# Leer el archivo CSV
df = pd.read_csv(csv_file)

# Obtener la lista de tipos de prueba
prueba_tipos = df["Prueba"].unique()

# Crear un archivo separado para cada tipo de prueba
for tipo in prueba_tipos:
    # Obtener las filas correspondientes a este tipo de prueba
    prueba_df = df[df["Prueba"] == tipo]
    # Eliminar la columna de "Prueba" del DataFrame
    #prueba_df = prueba_df.drop(columns=["Prueba"])
    # Crear el nombre del archivo separado
    file_name = os.path.join(directory_name, tipo + ".csv")
    # Guardar el DataFrame en un archivo separado
    prueba_df.to_csv(file_name, index=False)
