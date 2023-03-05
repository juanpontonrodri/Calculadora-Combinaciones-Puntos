Los equipos son 1: MOLEMOS, 2: Boiro, 3: Rias Baixas
Todos los arvhicos se ejecutan: pyhton3 nombre.py
Los archivos equiposx.csv son los descargados de la fegan de los 10 mejores tiempos de cada prueba
El arhivo filtrocsv.py filtra las entradas equipo{x}.csv y saca un uncio output tiempos.csv ordenados por equipo.

El archivo test13.py toma como entrada tiempos.csv y calcula las 10 mejores puntuaciones de las posibles combinaciones. El output es medias.csv
El uso es pyhton3 test13.py tiempos.csv media.csv
De esta forma se pueden cambiar los nombres de los archivos de ssalida
El archivo bestoption.py imprime por pantalla la mejor opcion para anar a cada club teniendo como input el media.csv. Tambien tiene la opcion de imprimir al fondo de media.csv las mejores opcionesss

ejecutamos filtrocsv_2 sin parametros y coge de la carpeta tiempos los tiempos de los 3 equipos. luego deja las series en la carpeta series
el test15.py se ejecuta con parametro series/la serie y crea los resultados en la carpeta medias

series/50_esp_masc_tiempos.csv
series/100_esp_masc_tiempos.csv

Para añadir a las versiones de prubeas individuales:
-Seleccionar el numero de combinacion del equipo 1 de la lista de medias y que te de el outpt de todas las combinaciones posibles con esos dos nadadores
ordenadas de menor a mayor puntuacion.
-Además, mostrar el porcentaje de veces que obtienen cada puntuacion para saber las posibilidades q tiene de ganar




Falta:
-Crear una estructura facilmente comparable para saber si un nadador ha participado en otra serie(una lista con todos los nadadores y el numero de pruebas en las q participan, este registro se reinica cada vez que se haga una nueva combinacion)
-Creamos combinaciones posibles entre los nadadores presentados a cada prueba.
-Iniciamos con la primera combinacion:  
        Segunda
            Tercera
                Aqui repetimos el procedimiento para la segunda serie
                    1eq Se busca en la lista q tenga de key el nombre de nadador el parametro de contador, si es un 1 se salta a la siguiente combinacion
                        2eq Se busca en la lista q tenga de key el nombre de nadador el parametro de contador, si es un 1 se salta a la siguiente combinacion
                            3eq Se busca en la lista q tenga de key el nombre de nadador el parametro de contador, si es un 1 se salta a la siguiente combinacion
                                Sumamos puntuacion equipo 1 y guardamos la combinacion de todos los nadadores si es la mas alta encontrada
