import pandas as pd

# Lee el archivo CSV
filename = "series/50_esp_masc_tiempos.csv"
data = pd.read_csv(filename)

# Agrupa los nadadores por equipo y prueba
grouped = data.groupby(["Equipo", "Nombre"])

# Crea las estructuras de datos para cada equipo y prueba
# El resultado de este código es un diccionario llamado "equipos", 
# donde las claves son los nombres de los equipos y los valores son otros 
# diccionarios que representan las pruebas en las que participan y los nadadores
# que las compiten, con sus respectivos tiempos.

equipos = {}
for equipo, group in grouped:
    prueba = filename.split(".")[0]
    nadadores = {}
    for _, row in group.iterrows():
        tiempo = row["Tiempo"]
        nadador = row["Nombre"]
        nadadores[nadador] = tiempo
    if equipo not in equipos:
        equipos[equipo] = {}
    equipos[equipo][prueba] = nadadores

#Por ejemplo, si quieres acceder a los tiempos de los nadadores del "Equipo 1"
# en la prueba "50_esp_masc", puedes hacerlo de la siguiente manera:

nadadores = equipos["Equipo 1"]["50_esp_masc"]
for nadador, tiempo in nadadores.items():
    print(nadador, tiempo)
