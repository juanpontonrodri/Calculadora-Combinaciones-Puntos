import sys
import pandas as pd
import os
from itertools import combinations,product
import time
import heapq

log_file = open("output.log", "a")
#sys.stdout = log_file


puntuacion_minima_total=14;
puntuacion_minima_media=15;

def calc_puntuacion(tiempos_MOLEMOS, tiempos_BOIRO, tiempos_RIAS):
    
    puntos_MOLEMOS_p1 = 0
    puntos_MOLEMOS_p2 = 0
    puntos_BOIRO_p1 = 0
    puntos_BOIRO_p2 = 0
    puntos_RIAS_p1 = 0
    puntos_RIAS_p2 = 0
    
    tiempos_prueba1 = [(tiempo, 'MOLEMOS') for tiempo in tiempos_MOLEMOS[0]] + [(tiempo, 'BOIRO') for tiempo in tiempos_BOIRO[0]] + [(tiempo, 'RIAS') for tiempo in tiempos_RIAS[0]]
    tiempos_prueba2 = [(tiempo, 'MOLEMOS') for tiempo in tiempos_MOLEMOS[1]] + [(tiempo, 'BOIRO') for tiempo in tiempos_BOIRO[1]] + [(tiempo, 'RIAS') for tiempo in tiempos_RIAS[1]]
    
    
    
    
    tiempos=[]
    tiempos.append(sorted(tiempos_prueba1, key=lambda x: x[0]))
    tiempos.append(sorted(tiempos_prueba2, key=lambda x: x[0]))
    
    #print(tiempos)
    
    puntos_MOLEMOS = [0] * 2
    puntos_BOIRO =[0] * 2
    puntos_RIAS = [0] * 2
    contador=0
    
    for t in tiempos:
        for i, nadador in enumerate(t):
            if i!=0:
                if nadador[1] == 'MOLEMOS':
                    puntos_MOLEMOS[contador] += 6 - i
                    #print("puntos molemos ",puntos_MOLEMOS)
                elif nadador[1] == 'BOIRO':
                    puntos_BOIRO[contador] += 6 - i
                    #print("puntos boiro ",puntos_BOIRO)
                else:
                    puntos_RIAS[contador] += 6 - i
                    #print("puntos rias ",puntos_RIAS)
            else:
                if nadador[1] == 'MOLEMOS':
                    puntos_MOLEMOS[contador] += 7
                    #print("puntos molemos ",puntos_MOLEMOS)
                elif nadador[1] == 'BOIRO':
                    puntos_BOIRO[contador] += 7
                    #print("puntos boiro ",puntos_BOIRO)
                else:
                    puntos_RIAS[contador] += 7
                    #print("puntos rias ",puntos_RIAS)
        contador=contador+1 
    #print(puntos_MOLEMOS[1] + puntos_MOLEMOS[0])      
    
    #con dos pruebas no aprecio cambios notables de rendimiento
    """tiempos_prueba1_ordenados = sorted(tiempos_prueba1, key=lambda x: x[0])
    tiempos_prueba2_ordenados = sorted(tiempos_prueba2, key=lambda x: x[0])
    for i, nadador in enumerate(tiempos_prueba1_ordenados):
        if nadador[1] == 'MOLEMOS':
            puntos_MOLEMOS[0] += 6 - i
        elif nadador[1] == 'BOIRO':
            puntos_BOIRO[0] += 6 - i
        else:
            puntos_RIAS[0] += 6 - i
            
    for i, nadador in enumerate(tiempos_prueba2_ordenados):
        if nadador[1] == 'MOLEMOS':
            puntos_MOLEMOS[1] += 6 - i
        elif nadador[1] == 'BOIRO':
            puntos_BOIRO[1] += 6 - i
        else:
            puntos_RIAS[1] += 6 - i """

    puntuacion_MOLEMOS = puntos_MOLEMOS[0] + puntos_MOLEMOS[1];
    puntuacion_BOIRO = puntos_BOIRO[0] + puntos_BOIRO[1];
    puntuacion_RIAS = puntos_RIAS[0] + puntos_RIAS[1];
    
    return puntuacion_MOLEMOS, puntuacion_BOIRO, puntuacion_RIAS


def crear_diccionario(archivo):
        
    # Leer el archivo CSV
    df = pd.read_csv(archivo)

    # Crear un diccionario para almacenar los tiempos de cada nadador
    diccionario = {}

    # Recorrer el DataFrame y agregar los tiempos a cada nadador en el diccionario
    for index, row in df.iterrows():
        equipo = row["Equipo"]
        tiempo = row["Tiempo"]
        nombre = row["Nombre"]
        prueba = row["Prueba"]
        if equipo not in diccionario:
            diccionario[equipo] = {}
        if prueba not in diccionario[equipo]:
            diccionario[equipo][prueba] = {}
        if nombre not in diccionario[equipo][prueba]:
            diccionario[equipo][prueba][nombre] = []
        diccionario[equipo][prueba][nombre].append(tiempo)

    # Obtener la lista de nombres de prueba
    nombre_prueba = sorted(list(set(df["Prueba"]))) 

    return diccionario, nombre_prueba

def crear_combinaciones(diccionario):
        
    #combinaciones de nadadores de cada prueba
    combinaciones_equipo_prueba = {}

    for equipo, pruebas in diccionario.items():
        
        for prueba, nadadores in pruebas.items():
            combinaciones_prueba = []
            nombres_nadadores = list(nadadores.keys())
            combinaciones_nadadores = list(combinations(nombres_nadadores, 2))
            combinaciones_prueba.extend(combinaciones_nadadores)

            combinaciones_equipo_prueba[(equipo, prueba)] = combinaciones_prueba
    return combinaciones_equipo_prueba

start_time = time.time()



archivo = 'series_test.csv'

diccionario,nombres_pruebas = crear_diccionario(archivo)

print("###Diccionario creado###")

combinaciones_equipo_prueba = crear_combinaciones(diccionario)

print("###Combinaciones creadas###")
#cada nadador solo puede estar o en la combinacion de la preuab 1 o en la combinacino de la preuab 2

#combinacion MOLEMOS para prueba 1
    #combinacion MOLEMOS para prueba 2
    #miramos si alguno de los dos nadadores de esta combinacion esta en la combinacion de la prueba uno de MOLEMOS, si no esta continuamos
    
    #puntuacion_comb=[]
        #combinacion BOIRO para prueba 1
            #combinacion BOIRO para prueba 2
                #comprobamos si alguno de los dos nadadores de esta combinacion esta en la combinacion de la prueba uno de BOIRO, si no esta continuamos
                #combinacion RIAS para prueba 1
                    #combinacion RIAS para prueba 2
                        #comprobamos si alguno de los dos nadadores de esta combinacion esta en la combinacion de la prueba uno de RIAS, si no esta continuamos
                        #ordenamos tiempos de los 6 nadadores de la prueba 1 y calculamos puntuacion
                        #ordenamos tiempos de lso 6 nadadores de la prueba 2 y calculamos puntuacion
                        #puntuacion MOLEMOS= puntuacion nadadores MOLEMOS prueba 1 + puntuacion nadadores MOLEMOS prueba 2
                        #añadirmos a puntuacion_comb la puntuacion de MOLEMOS
    #hacemos la medai de puntuacion_comb
    #guardamos la media junto con las combinaciones de MOLEMOS para la prueba 1 y preuba 2 en un diccionario
                         
prueba_1=nombres_pruebas[0]
prueba_2=nombres_pruebas[1]

flag_save=1
flag1=0
flag2=0
         
#variuable para debug
num_comb_guardad=[]
         
c=0
numero_combinaciones_MOLEMOS = 1
numero_combinaciones_MOLEMOS_duplicadas=0
numero_combinaciones_totales=1


for prueba in nombres_pruebas:
    numero_combinaciones_MOLEMOS=numero_combinaciones_MOLEMOS*len(combinaciones_equipo_prueba[('MOLEMOS', prueba)])
    numero_combinaciones_totales=numero_combinaciones_MOLEMOS*len(combinaciones_equipo_prueba[('BOIRO', prueba)])*len(combinaciones_equipo_prueba[('RIAS', prueba)])

puntuaciones = {}
for comb_MOLEMOS_p1 in combinaciones_equipo_prueba[('MOLEMOS', prueba_1)]:
    flag1=0
    for comb_MOLEMOS_p2 in combinaciones_equipo_prueba[('MOLEMOS', prueba_2)]:        
        c+=1
        puntuaciones_MOLEMOS = []
        if set(comb_MOLEMOS_p1) & set(comb_MOLEMOS_p2):
            numero_combinaciones_MOLEMOS_duplicadas=numero_combinaciones_MOLEMOS_duplicadas+1
            continue
        print("Combinación número %d de %d %s %s" % (c, numero_combinaciones_MOLEMOS, comb_MOLEMOS_p1, comb_MOLEMOS_p2))

        for comb_BOIRO_p1, comb_BOIRO_p2, comb_RIAS_p1, comb_RIAS_p2 in product(combinaciones_equipo_prueba[('BOIRO', prueba_1)], combinaciones_equipo_prueba[('BOIRO', prueba_2)], combinaciones_equipo_prueba[('RIAS', prueba_1)], combinaciones_equipo_prueba[('RIAS', prueba_2)]):
            if set(comb_BOIRO_p1) & set(comb_BOIRO_p2) or set(comb_RIAS_p1) & set(comb_RIAS_p2):
                continue
            
            tiempos_MOLEMOS=[]
            tiempos_BOIRO=[]
            tiempos_RIAS=[]
            
            
            #probar usando tiemposmolemos.append en vez d eponer lo sindices
            tiempos_MOLEMOS.append([diccionario['MOLEMOS'][prueba_1][nadador][0] for nadador in comb_MOLEMOS_p1])
            tiempos_MOLEMOS.append([diccionario['MOLEMOS'][prueba_2][nadador][0] for nadador in comb_MOLEMOS_p2])
            tiempos_BOIRO.append([diccionario['BOIRO'][prueba_1][nadador][0] for nadador in comb_BOIRO_p1])
            tiempos_BOIRO.append([diccionario['BOIRO'][prueba_2][nadador][0] for nadador in comb_BOIRO_p2])
            tiempos_RIAS.append([diccionario['RIAS'][prueba_1][nadador][0] for nadador in comb_RIAS_p1])
            tiempos_RIAS.append([diccionario['RIAS'][prueba_2][nadador][0] for nadador in comb_RIAS_p2])
            
            #Para dos pruebas sube el tiempo de ejecucion en un 15%
            """ contador = 1
            for prueba in nombres_pruebas:
                comb_MOLEMOS = globals()[f"comb_MOLEMOS_p{contador}"]
                tiempos_MOLEMOS.append([diccionario['MOLEMOS'][prueba][nadador][0] for nadador in comb_MOLEMOS])
                
                # Repite el mismo proceso para las otras variables de combinación
                comb_BOIRO = globals()[f"comb_BOIRO_p{contador}"]
                tiempos_BOIRO.append([diccionario['BOIRO'][prueba][nadador][0] for nadador in comb_BOIRO])
                
                comb_RIAS = globals()[f"comb_RIAS_p{contador}"]
                tiempos_RIAS.append([diccionario['RIAS'][prueba][nadador][0] for nadador in comb_RIAS])
                
                contador += 1 """

            
            puntuacion_MOLEMOS, puntuacion_BOIRO, puntuacion_RIAS= calc_puntuacion(tiempos_MOLEMOS, tiempos_BOIRO, tiempos_RIAS)
            #print("puntuacion MOLEMOS %d BOIRO %d RIAS %d" %(puntuacion_MOLEMOS,puntuacion_BOIRO, puntuacion_RIAS))
            if(puntuacion_MOLEMOS<puntuacion_minima_total):
                
                flag2=flag2+1
                print("#No llega al minimo, flag2:",flag2)
                #print(comb_BOIRO_p1,comb_BOIRO_p2,comb_RIAS_p1,comb_RIAS_p2)
                #print(tiempos_MOLEMOS,tiempos_BOIRO,tiempos_RIAS)
                #print(puntuacion_MOLEMOS,puntuacion_BOIRO,puntuacion_RIAS)
                if(flag2>1):
                    flag1=flag1+1
                    print("flag1: ",flag1)
                else:
                    flag1=0	
                print("break interno")
                flag_save=0
                break
            else:
                flag2=0
                flag_save=1
                puntuaciones_MOLEMOS.append(puntuacion_MOLEMOS)

            #descomentar para pausar en cada combinacion
            #input("Presiona una tecla para continuar...")

            
        if(flag1>1):
            print("break en p2")
            break #avanzo a la siguietne combinacion de molemos para p1
        if(len(puntuaciones_MOLEMOS)!=0):
            print("flag_save: ",flag_save)
            num_comb_guardad.append(c)
            
            puntuaciones[(comb_MOLEMOS_p1, comb_MOLEMOS_p2)] = sum(puntuaciones_MOLEMOS)/len(puntuaciones_MOLEMOS)
            print(puntuaciones[(comb_MOLEMOS_p1, comb_MOLEMOS_p2)]," ",tiempos_MOLEMOS)
        
 

# Obtener las mejores 10 combinaciones con la puntuación más alta
mejores_combinaciones = heapq.nlargest(10, puntuaciones, key=puntuaciones.get)
print("Listado de pruebas:", nombres_pruebas)
print("\nLas mejores 10 combinaciones son:")
for i, combinacion in enumerate(mejores_combinaciones):
    print(f"{i+1}. {combinacion} - Puntuación: {puntuaciones[combinacion]}")
    k=0
    for  comb in combinacion:
        print("Prueba ",nombres_pruebas[k])
        for nadador in comb:
            tiempo=(diccionario['MOLEMOS'][nombres_pruebas[k]][nadador][0])
            print(nadador,tiempo)
        if k==1:
            k=0
            break
        k=k+1    

# Obtener el número de combinaciones que superan la puntuación mínima
contador_combinaciones = 0
for puntuacion in puntuaciones.values():
    if puntuacion >= puntuacion_minima_media:
        contador_combinaciones += 1

print(f"Hay {contador_combinaciones} combinaciones que superan la puntuación mínima de {puntuacion_minima_media}")


print(num_comb_guardad)

end_time=time.time()

print()
print("Numero de combinaciones totales: ",numero_combinaciones_totales)
print("Numero de combinaciones MOLEMOS duplicadas: ",numero_combinaciones_MOLEMOS_duplicadas,"Total combinaciones MOLEMOS evaluadas: ",numero_combinaciones_MOLEMOS-numero_combinaciones_MOLEMOS_duplicadas)
print("Tiempo de ejecución: ",end_time-start_time)


log_file.close()