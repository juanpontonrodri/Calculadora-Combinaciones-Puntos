import os
import pandas as pd
import sys

# Nombre del archivo XLSX a leer
xlsx_file = sys.argv[1]

# Nombre del directorio a crear para los datos masculinos
directory_name_masc = os.path.splitext(xlsx_file)[0] + "_masc"
# Crear el directorio si no existe
if not os.path.exists(directory_name_masc):
    os.makedirs(directory_name_masc)

# Nombre del directorio a crear para los datos femeninos
directory_name_fem = os.path.splitext(xlsx_file)[0] + "_fem"
# Crear el directorio si no existe
if not os.path.exists(directory_name_fem):
    os.makedirs(directory_name_fem)

# Leer el archivo XLSX y guardar los datos masculinos en un archivo CSV separado para cada tipo de prueba
df_masc = pd.read_excel(xlsx_file, sheet_name="series_masc")
prueba_tipos_masc = df_masc["Prueba"].unique()
for tipo in prueba_tipos_masc:
    prueba_df = df_masc[df_masc["Prueba"] == tipo]
    file_name = os.path.join(directory_name_masc, tipo + ".csv")
    prueba_df.to_csv(file_name, index=False)

# Leer el archivo XLSX y guardar los datos femeninos en un archivo CSV separado para cada tipo de prueba
df_fem = pd.read_excel(xlsx_file, sheet_name="series_fem")
prueba_tipos_fem = df_fem["Prueba"].unique()
for tipo in prueba_tipos_fem:
    prueba_df = df_fem[df_fem["Prueba"] == tipo]
    file_name = os.path.join(directory_name_fem, tipo + ".csv")
    prueba_df.to_csv(file_name, index=False)
