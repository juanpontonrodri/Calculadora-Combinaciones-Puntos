Los equipos son 1: MOLEMOS, 2: Boiro, 3: Rias Baixas
Los archivos equiposx.csv son los descargados de la fegan de los 10 mejores tiempos de cada prueba
El arhivo filtrocsv.py filtra las entradas equipo{x}.csv y saca un uncio output tiempos.csv ordenados por equipo.

Para añadir a las versiones de prubeas individuales:
-Seleccionar el numero de combinacion del equipo 1 de la lista de medias y que te de el outpt de todas las combinaciones posibles con esos dos nadadores
ordenadas de menor a mayor puntuacion.

Medidas de optimización:
X-Usar listas de comprension:Hay un ejepmlo implementado en la funcion de calcular puntuacion, pero ha aumentado en un 25% el tiempo total de ejecucion

-Modifciar las estructurasd de datos para que sean mas eficientes(usar sets en vez de listas)
-Optimizar las sumas
-Separar diccionario en 3 diccionarios(uno por club) y luego crear listas para cada preuba en esos diccionarios
-Ademas al pasar los tiempos a las funcionesnde alcular, puedo pasarlos de otras formas par a no iteren tanto en la propia funcion
-Poner q si no ganamos al boiro pase a la siguietne combinacion
O-Arreglar leer de un archivo
-Guardar los resultados en un csv y q vaya siendo con append para poder ir viendo los resultados parciales
