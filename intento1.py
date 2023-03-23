import pandas as pd

# Lee el archivo CSV
filename1 = "series/50_esp_masc_tiempos.csv"
prueba1= filename1.split("/")[-1].split("_tiempos")[0]
data1 = pd.read_csv(filename1)

# Lee el archivo CSV
filename2 = "series/100_esp_masc_tiempos.csv"
prueba2= filename2.split("/")[-1].split("_tiempos")[0]
data2 = pd.read_csv(filename2)

# Agrupa los nadadores por equipo y prueba
grouped1 = data1.groupby(["Equipo"])
grouped2 = data2.groupby(["Equipo"])

# Crea las estructuras de datos para cada equipo y prueba
# El resultado de este código es un diccionario llamado "equipos", 
# donde las claves son los nombres de los equipos y los valores son otros 
# diccionarios que representan las pruebas en las que participan y los nadadores
# que las compiten, con sus respectivos tiempos.

equipos = {}
for equipo, group in grouped1:
    if equipo not in equipos:
        equipos[equipo] = {}
    for prueba, group2 in group.groupby("Prueba"):
        nadadores = {}
        for _, row in group2.iterrows():
            tiempo = row["Tiempo"]
            nadador = row["Nombre"]
            if prueba == prueba1:
                if "prueba1" not in equipos[equipo]:
                    equipos[equipo]["prueba1"] = {}
                equipos[equipo]["prueba1"][nadador] = tiempo
            elif prueba == prueba2:
                if "prueba2" not in equipos[equipo]:
                    equipos[equipo]["prueba2"] = {}
                equipos[equipo]["prueba2"][nadador] = tiempo

# Por ejemplo, si quieres acceder a los tiempos de los nadadores del "Equipo MOLEMOS"
# en la prueba "prueba1", puedes hacerlo de la siguiente manera:
print(equipos["MOLEMOS"]["prueba1"])

# Imprime la estructura de los equipos, pruebas y nadadores con sus tiempos
for equipo, pruebas in equipos.items():
    print(f"Equipo: {equipo}")
    for prueba, nadadores in pruebas.items():
        print(f"\tPrueba: {prueba}")
        for nadador, tiempo in nadadores.items():
            print(f"\t\tNadador: {nadador}: {tiempo}")
