#Description: Eliminar todas las entradas de un archivo CSV que contengan un nombre determinado

import pandas as pd
import sys

archivo_entrada = sys.argv[1]
# Leer el archivo CSV en un dataframe
df = pd.read_csv(archivo_entrada)

# Crear una lista con los nombres que se desean eliminar
nombres_a_eliminar = ["PEREZ TIERRA, ISMAEL", "VALCARCE DOMINGUEZ, PABLO", "PEREZ TIERRA, DANIEL", "MARTINEZ MARINO, ANDRES", "RODRIGUEZ SANCHEZ, MIGUEL"]
#nombre_a_eliminar = ["SENRA RODRIGUEZ, LAURA","VARELA MENDEZ, LUCIA","VARELA MENDEZ, CLARA","MENDES GONZALEZ, SOFIA","GARCIA SANCHEZ, ISABEL"]

# Filtrar las filas que contengan los nombres a eliminar
df = df[~df['Nombre'].isin(nombres_a_eliminar)]

# Guardar el dataframe resultante en un nuevo archivo CSV
df.to_csv('series_masc_total.csv', index=False)
