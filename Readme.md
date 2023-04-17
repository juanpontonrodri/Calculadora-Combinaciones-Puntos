Los equipos son 1: MOLEMOS, 2: Boiro, 3: Rias Baixas
Los archivos equiposx.csv son los descargados de la fegan de los 10 mejores tiempos de cada prueba
El arhivo filtrocsv.py filtra las entradas equipo{x}.csv y saca un uncio output tiempos.csv ordenados por equipo.

Para añadir a las versiones de prubeas individuales:
-Seleccionar el numero de combinacion del equipo 1 de la lista de medias y que te de el outpt de todas las combinaciones posibles con esos dos nadadores
ordenadas de menor a mayor puntuacion.

Medidas de optimización:
-Usar listas de comprension
-Modifciar las estructurasd de datos para que sean mas eficientes(usar sets en vez de listas)
-Optimizar las sumas
-Guardado y seleccion de mejores combinaciones
-Arreglar puntuaciones para 7 puntos el primero
-Separar diccionario en 3 diccionarios(uno por club) y luego crear listas para cada preuba en esos diccionarios
-Ademas al pasar los tiempos a las funcionesnde alcular, puedo pasarlos de otras formas par a no iteren tanto en la propia funcion
-Variable de puntuacion minima: si no consigues la puntuacion minima, salta a la siguiente iteraccion, es decir, si con 4 pruebas no se llega al minimo se salta a la siguiente iteracion del molemos y se activa un flag, si sigue sin llegarse y el flag esta activado se salta a la siguiente iteraccion de la prueba 3 y se incrementa el flag(o decremtna si es mas comodo por el numero de prueba), si sigue sin lelgarse se salta al siguentee de la 2 etc
-Poner q si no ganamos al boiro pase a la siguietne combinacion
-Arreglar leer de un archivo
