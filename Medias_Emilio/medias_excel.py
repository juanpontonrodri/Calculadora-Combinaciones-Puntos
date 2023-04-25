#En medias_fem o _masc se almacena los documentos de resultados de medias
#En liga test1 se almacenan los documetnos fruto de separar las pagainas del excel por pruebas

#instalar pandas y openpyxl
import itertools
import csv
import os
import pandas as pd
import sys
#la primera es del ejectautuable la segunda de donde se ejecuta el script
#ruta_ejecucion = os.path.dirname(sys.executable)
ruta_ejecucion=os.path.abspath(os.getcwd())
ruta_medias_masc=ruta_ejecucion + "/medias_masc"
ruta_medias_fem=ruta_ejecucion + "/medias_fem"

print("Ruta de ejecución: " + ruta_ejecucion)
#CODIGO PARA SEPARAR LOS ARCHIVOS DE EXCEL EN CSV
# Nombre del archivo XLSX a leer
xlsx_file = "Liga_test_1.xlsx"

ruta_archivo = ruta_ejecucion + "/medias_masc/medias_masc.csv"

# Comprobar si el archivo existe
if os.path.exists(ruta_archivo):
    # Si el archivo existe, eliminarlo
    os.remove(ruta_archivo)

ruta_archivo = ruta_ejecucion + "/medias_fem/medias_fem.csv"

# Comprobar si el archivo existe
if os.path.exists(ruta_archivo):
    # Si el archivo existe, eliminarlo
    os.remove(ruta_archivo)


# Nombre del directorio a crear para los datos masculinos
directory_name_masc = ruta_ejecucion+"/"+ xlsx_file[:-5] + "_masc"
print(directory_name_masc)
# Crear el directorio si no existe
if not os.path.exists(directory_name_masc):
    os.makedirs(directory_name_masc)

# Nombre del directorio a crear para los datos femeninos
directory_name_fem = ruta_ejecucion+"/"+ xlsx_file[:-5] + "_fem"
print(directory_name_fem)
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
  
  
#CODIGO PARA CALCULAR LAS MEDIAS DE LOS ARCHIVOS CSV MASCULINO


# Create a list to store the output file paths
output_files = []

if not os.path.exists(ruta_medias_masc):
    os.makedirs(ruta_medias_masc)

for filename in os.listdir(directory_name_masc):
    if filename.endswith(".csv"):
        archivo_entrada = os.path.join(directory_name_masc, filename)
        nombre_salida = os.path.join(ruta_medias_masc, os.path.splitext(filename)[0] + "_salida.csv")
        output_files.append(nombre_salida)

        # Lectura de tiempos de archivo CSV
        equipos = {}
        with open(archivo_entrada, newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre = fila['Nombre']
                tiempo = float(fila['Tiempo'])
                equipo = fila['Equipo']
                if equipo not in equipos:
                    equipos[equipo] = []
                equipos[equipo].append((nombre, tiempo))

        # Generación de todas las combinaciones posibles de grupos de dos para cada equipo
        combinaciones_por_equipo = []
        for equipo in equipos.values():
            combinaciones = itertools.combinations(equipo, 2)
            combinaciones_por_equipo.append(list(combinaciones))

        

        # Bucle para encontrar las 10 combinaciones con la mayor puntuación media para el primer equipo
        puntuaciones_medias = []
        for combinacion_equipo1 in combinaciones_por_equipo[0]:
            puntuacion_minima_conseguida=12
            combinacion_boiro_para_puntuacion_minima = []
            combinacion_rias_para_puntuacion_minima = []
            puntuacion_total = 0
            contador_victorias_al_boiro = 0
            for combinacion_equipo2 in combinaciones_por_equipo[1]:
                for combinacion_equipo3 in combinaciones_por_equipo[2]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
                    puntuacion_equipo2 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo2])
                    if puntuacion_equipo1 < puntuacion_minima_conseguida:
                        puntuacion_minima_conseguida = puntuacion_equipo1
                        combinacion_boiro_para_puntuacion_minima = combinacion_equipo2
                        combinacion_rias_para_puntuacion_minima = combinacion_equipo3
                    if puntuacion_equipo1 > puntuacion_equipo2:
                        contador_victorias_al_boiro += 1
                    puntuacion_total += puntuacion_equipo1
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[1]) * len(combinaciones_por_equipo[2]))
            porcentaje_victorias_al_boiro = contador_victorias_al_boiro / (len(combinaciones_por_equipo[1]) * len(combinaciones_por_equipo[2]))
            puntuaciones_medias.append((combinacion_equipo1, puntuacion_media, porcentaje_victorias_al_boiro, puntuacion_minima_conseguida, combinacion_boiro_para_puntuacion_minima,combinacion_rias_para_puntuacion_minima))


        # Ordenar combinaciones por puntuación media
        puntuaciones_medias.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 6 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias = puntuaciones_medias[:10]

        # Bucle para encontrar las 10 mejores puntuaciones medias para el segundo equipo
        puntuaciones_medias_equipo2 = []
        for combinacion_equipo2 in combinaciones_por_equipo[1]:
            puntuacion_total = 0
            for combinacion_equipo1 in combinaciones_por_equipo[0]:
                for combinacion_equipo3 in combinaciones_por_equipo[2]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo2 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo2])
                    puntuacion_total += puntuacion_equipo2
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[0]) * len(combinaciones_por_equipo[2]))
            puntuaciones_medias_equipo2.append((combinacion_equipo2, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias_equipo2.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 10 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias_equipo2 = puntuaciones_medias_equipo2[:10]


        # Bucle para encontrar las 10 mejores puntuaciones medias para el tercer equipo
        puntuaciones_medias_equipo3 = []
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            puntuacion_total = 0
            for combinacion_equipo1 in combinaciones_por_equipo[0]:
                for combinacion_equipo2 in combinaciones_por_equipo[1]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo3 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo3])
                    puntuacion_total += puntuacion_equipo3
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[0]) * len(combinaciones_por_equipo[1]))
            puntuaciones_medias_equipo3.append((combinacion_equipo3, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias_equipo3.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 10 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias_equipo3 = puntuaciones_medias_equipo3[:10]

        # Escritura de la tabla de resultados para la segunda parte del problema en un archivo de salida diferente
        with open(nombre_salida, 'w',encoding='utf-8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([filename[:-4]])
            writer.writerow(["Nº","Nadador 1","Tiempo1","Nadador 2","Tiempo2", "Puntuación media", "Porcentaje de victorias al BOIRO", "Puntuación mínima conseguida", "Combinación BOIRO para puntuación mínima", "Combinación RIAS para puntuación mínima"])
            for idx, mejor_combinacion in enumerate(mejores_combinaciones_medias):
                t=[str(n[1]) for n in mejor_combinacion[0]]
                nadadores=[n[0] for n in mejor_combinacion[0]]
                writer.writerow([idx+1, nadadores[0],t[0][:-2],nadadores[1],t[1][:-2], mejor_combinacion[1],mejor_combinacion[2]*100,mejor_combinacion[3],mejor_combinacion[4],mejor_combinacion[5]])
            # Escritura de la tabla de resultados para el segundo equipo
            """  writer.writerow(["Combinación", "BOIRO", "Puntuación media", "Tiempos"])
            for idx2, mejor_combinacion2 in enumerate(mejores_combinaciones_medias_equipo2):
                equipo2 = ", ".join([n[0] for n in mejor_combinacion2[0]])
                tiempos=", ".join([str(n[1]) for n in mejor_combinacion2[0]])

                writer.writerow([idx2+1, equipo2, mejor_combinacion2[1],tiempos])
                
            writer.writerow(["Combinación", "RIAS", "Puntuación media", "Tiempos"])
            for idx3, mejor_combinacion3 in enumerate(mejores_combinaciones_medias_equipo3):
                equipo3 = ", ".join([n[0] for n in mejor_combinacion3[0]])
                tiempos=", ".join([str(n[1]) for n in mejor_combinacion3[0]])

                writer.writerow([idx3+1, equipo3, mejor_combinacion3[1],tiempos]) """

# Ruta de la carpeta donde se encuentran los archivos 


# Lista para almacenar los nombres de los archivos 
archivos = []

# Obtener los nombres de los archivos 
for nombre_archivo in os.listdir(ruta_medias_masc):
    if nombre_archivo.endswith('.csv'):
        archivos.append(nombre_archivo)
    
    
archivo_junto=ruta_medias_masc+"/medias_masc.csv"
# Abrir un archivo nuevo donde se escribirán todas las líneas juntas
with open(archivo_junto, 'w') as archivo_final:
    # Recorrer cada archivo .xd y escribir sus líneas en el archivo final
    for nombre_archivo in archivos:
        with open(os.path.join(ruta_medias_masc, nombre_archivo), 'r') as archivo:
            lineas = archivo.readlines()
            archivo_final.writelines(lineas)
            
            
            
            
            
            
#################################################################################################
#################################################################################################
#################################################################################################
################################################################################################# 



#CODIGO PARA CALCULAR LAS MEDIAS DE LOS ARCHIVOS CSV FEMENINO


# Create a list to store the output file paths
output_files = []

if not os.path.exists(ruta_medias_fem):
    os.makedirs(ruta_medias_fem)

for filename in os.listdir(directory_name_fem):
    if filename.endswith(".csv"):
        archivo_entrada = os.path.join(directory_name_fem, filename)
        nombre_salida = os.path.join(ruta_medias_fem, os.path.splitext(filename)[0] + "_salida.csv")
        output_files.append(nombre_salida)

        # Lectura de tiempos de archivo CSV
        equipos = {}
        with open(archivo_entrada, newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre = fila['Nombre']
                tiempo = float(fila['Tiempo'])
                equipo = fila['Equipo']
                if equipo not in equipos:
                    equipos[equipo] = []
                equipos[equipo].append((nombre, tiempo))

        # Generación de todas las combinaciones posibles de grupos de dos para cada equipo
        combinaciones_por_equipo = []
        for equipo in equipos.values():
            combinaciones = itertools.combinations(equipo, 2)
            combinaciones_por_equipo.append(list(combinaciones))

        

        # Bucle para encontrar las 10 combinaciones con la mayor puntuación media para el primer equipo
        puntuaciones_medias = []
        for combinacion_equipo1 in combinaciones_por_equipo[0]:
            puntuacion_minima_conseguida=12
            combinacion_boiro_para_puntuacion_minima = []
            combinacion_rias_para_puntuacion_minima = []
            puntuacion_total = 0
            contador_victorias_al_boiro = 0
            for combinacion_equipo2 in combinaciones_por_equipo[1]:
                for combinacion_equipo3 in combinaciones_por_equipo[2]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo1 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo1])
                    puntuacion_equipo2 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo2])
                    if puntuacion_equipo1 < puntuacion_minima_conseguida:
                        puntuacion_minima_conseguida = puntuacion_equipo1
                        combinacion_boiro_para_puntuacion_minima = combinacion_equipo2
                        combinacion_rias_para_puntuacion_minima = combinacion_equipo3
                    if puntuacion_equipo1 > puntuacion_equipo2:
                        contador_victorias_al_boiro += 1
                    puntuacion_total += puntuacion_equipo1
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[1]) * len(combinaciones_por_equipo[2]))
            porcentaje_victorias_al_boiro = contador_victorias_al_boiro / (len(combinaciones_por_equipo[1]) * len(combinaciones_por_equipo[2]))
            puntuaciones_medias.append((combinacion_equipo1, puntuacion_media, porcentaje_victorias_al_boiro, puntuacion_minima_conseguida, combinacion_boiro_para_puntuacion_minima,combinacion_rias_para_puntuacion_minima))


        # Ordenar combinaciones por puntuación media
        puntuaciones_medias.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 6 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias = puntuaciones_medias[:10]

        # Bucle para encontrar las 10 mejores puntuaciones medias para el segundo equipo
        puntuaciones_medias_equipo2 = []
        for combinacion_equipo2 in combinaciones_por_equipo[1]:
            puntuacion_total = 0
            for combinacion_equipo1 in combinaciones_por_equipo[0]:
                for combinacion_equipo3 in combinaciones_por_equipo[2]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo2 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo2])
                    puntuacion_total += puntuacion_equipo2
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[0]) * len(combinaciones_por_equipo[2]))
            puntuaciones_medias_equipo2.append((combinacion_equipo2, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias_equipo2.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 10 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias_equipo2 = puntuaciones_medias_equipo2[:10]


        # Bucle para encontrar las 10 mejores puntuaciones medias para el tercer equipo
        puntuaciones_medias_equipo3 = []
        for combinacion_equipo3 in combinaciones_por_equipo[2]:
            puntuacion_total = 0
            for combinacion_equipo1 in combinaciones_por_equipo[0]:
                for combinacion_equipo2 in combinaciones_por_equipo[1]:
                    tiempos = sorted(list(combinacion_equipo1) + list(combinacion_equipo2) + list(combinacion_equipo3), key=lambda x: x[1])
                    puntuaciones = [7, 5, 4, 3, 2, 1]
                    puntuacion_equipo3 = sum([puntuaciones[i] for i in range(len(tiempos)) if tiempos[i] in combinacion_equipo3])
                    puntuacion_total += puntuacion_equipo3
            puntuacion_media = puntuacion_total / (len(combinaciones_por_equipo[0]) * len(combinaciones_por_equipo[1]))
            puntuaciones_medias_equipo3.append((combinacion_equipo3, puntuacion_media))

        # Ordenar combinaciones por puntuación media
        puntuaciones_medias_equipo3.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las 10 combinaciones con la puntuación media más alta
        mejores_combinaciones_medias_equipo3 = puntuaciones_medias_equipo3[:10]

        # Escritura de la tabla de resultados para la segunda parte del problema en un archivo de salida diferente
        with open(nombre_salida, 'w',encoding='utf-8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([filename[:-4]])
            writer.writerow(["Nº","Nadador 1","Tiempo1","Nadador 2","Tiempo2", "Puntuación media", "Porcentaje de victorias al BOIRO", "Puntuación mínima conseguida", "Combinación BOIRO para puntuación mínima", "Combinación RIAS para puntuación mínima"])
            for idx, mejor_combinacion in enumerate(mejores_combinaciones_medias):
                t=[str(n[1]) for n in mejor_combinacion[0]]
                nadadores=[n[0] for n in mejor_combinacion[0]]
                writer.writerow([idx+1, nadadores[0],t[0][:-2],nadadores[1],t[1][:-2], mejor_combinacion[1],mejor_combinacion[2]*100,mejor_combinacion[3],mejor_combinacion[4],mejor_combinacion[5]])
            # Escritura de la tabla de resultados para el segundo equipo
            """  writer.writerow(["Combinación", "BOIRO", "Puntuación media", "Tiempos"])
            for idx2, mejor_combinacion2 in enumerate(mejores_combinaciones_medias_equipo2):
                equipo2 = ", ".join([n[0] for n in mejor_combinacion2[0]])
                tiempos=", ".join([str(n[1]) for n in mejor_combinacion2[0]])

                writer.writerow([idx2+1, equipo2, mejor_combinacion2[1],tiempos])
                
            writer.writerow(["Combinación", "RIAS", "Puntuación media", "Tiempos"])
            for idx3, mejor_combinacion3 in enumerate(mejores_combinaciones_medias_equipo3):
                equipo3 = ", ".join([n[0] for n in mejor_combinacion3[0]])
                tiempos=", ".join([str(n[1]) for n in mejor_combinacion3[0]])

                writer.writerow([idx3+1, equipo3, mejor_combinacion3[1],tiempos]) """

# Ruta de la carpeta donde se encuentran los archivos 


# Lista para almacenar los nombres de los archivos 
archivos = []

# Obtener los nombres de los archivos 
for nombre_archivo in os.listdir(ruta_medias_fem):
    if nombre_archivo.endswith('.csv'):
        archivos.append(nombre_archivo)


archivo_junto=ruta_medias_fem+ "/medias_fem.csv"
# Abrir un archivo nuevo donde se escribirán todas las líneas juntas
with open(archivo_junto, 'w') as archivo_final:
    # Recorrer cada archivo .xd y escribir sus líneas en el archivo final
    for nombre_archivo in archivos:
        with open(os.path.join(ruta_medias_fem, nombre_archivo), 'r') as archivo:
            lineas = archivo.readlines()
            archivo_final.writelines(lineas)