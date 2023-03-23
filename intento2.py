
import pandas as pd

# Lee el archivo CSV
filename1 = "series/50_esp_masc_tiempos.csv"
nombre_prueba1= filename1.split("/")[-1].split("_tiempos")[0]
data1 = pd.read_csv(filename1)

# Lee el archivo CSV
filename2 = "series/100_esp_masc_tiempos.csv"
nombre_prueba2= filename2.split("/")[-1].split("_tiempos")[0]
data2 = pd.read_csv(filename2)

# Agrupa los nadadores por equipo y prueba
grouped1 = data1.groupby(["Equipo", "Prueba"])
grouped2 = data2.groupby(["Equipo", "Prueba"])

# Crea las estructuras de datos para cada equipo y prueba
# El resultado de este código es un diccionario llamado "equipos", 
# donde las claves son los nombres de los equipos y los valores son otros 
# diccionarios que representan las pruebas en las que participan y los nadadores
# que las compiten, con sus respectivos tiempos.
equipos = {}
for (equipo, prueba), group in grouped1:
    if equipo not in equipos:
        equipos[equipo] = {}
    if prueba not in equipos[equipo]:
        equipos[equipo][prueba] = {}
    for _, row in group.iterrows():
        tiempo = row["Tiempo"]
        nadador = row["Nombre"]
        equipos[equipo][prueba][nadador] = tiempo

for (equipo, prueba), group in grouped2:
    if equipo not in equipos:
        equipos[equipo] = {}
    if prueba not in equipos[equipo]:
        equipos[equipo][prueba] = {}
    for _, row in group.iterrows():
        tiempo = row["Tiempo"]
        nadador = row["Nombre"]
        equipos[equipo][prueba][nadador] = tiempo

# Imprime la estructura de datos
print(equipos)

