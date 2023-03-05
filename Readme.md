Los equipos son 1: MOLEMOS, 2: Boiro, 3: Rias Baixas
Todos los arvhicos se ejecutan: pyhton3 nombre.py
Los archivos equiposx.csv son los descargados de la fegan de los 10 mejores tiempos de cada prueba
El arhivo filtrocsv.py filtra las entradas equipo{x}.csv y saca un uncio output tiempos.csv ordenados por equipo.

El archivo test13.py toma como entrada tiempos.csv y calcula las 10 mejores puntuaciones de las posibles combinaciones. El output es medias.csv
El uso es pyhton3 test13.py tiempos.csv media.csv
De esta forma se pueden cambiar los nombres de los archivos de ssalida
El archivo bestoption.py imprime por pantalla la mejor opcion para anar a cada club teniendo como input el media.csv. Tambien tiene la opcion de imprimir al fondo de media.csv las mejores opcionesss
