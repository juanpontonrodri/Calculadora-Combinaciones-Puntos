# Description: Unir archivos CSV de una carpeta en un solo archivo CSV

import os
import pandas as pd
import sys

# Directorio con los archivos CSV
dir_path = sys.argv[1]

# Diccionario de orden de equipos
order_dict = {'MOLEMOS': 1, 'BOIRO': 2, 'RIAS': 3}

# Lista para guardar los DataFrames de cada archivo CSV
dfs = []

# Leer cada archivo CSV en el directorio y agregar el DataFrame resultante a la lista dfs
for file_name in os.listdir(dir_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(dir_path, file_name)
        df = pd.read_csv(file_path)
        dfs.append(df)

# Concatenar todos los DataFrames en uno solo
concatenated_df = pd.concat(dfs)

# Agregar una nueva columna con el orden de equipos
concatenated_df['Equipo_Orden'] = concatenated_df['Equipo'].map(order_dict)

# Ordenar el DataFrame concatenado
concatenated_df = concatenated_df.sort_values(by=["Equipo_Orden", "Prueba", "Tiempo", "Nombre"])

# Eliminar la columna de orden de equipos
concatenated_df = concatenated_df.drop('Equipo_Orden', axis=1)

# Escribir el DataFrame concatenado en un archivo CSV
concatenated_df.to_csv('series_fem_total.csv', index=False)
