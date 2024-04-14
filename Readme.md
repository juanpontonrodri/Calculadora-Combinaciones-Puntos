Los equipos son 1: MOLEMOS, 2: CIDSANTI, 3: NTNARON


## Como actualizar para nuevos equipos
- Descargar los 10 mejores tiempos de cada prueba de la fegan y meterlos en tiempos_fem y tiempos_masc con el formato existente (Distancia_Estilo_sexo_numeroequipo.csv)
- Ejecutar filtrocsv.py. Este script toma como parametros la carpeta de entrada (donde estan los tiempos separados por prueba y equipo) y la carpeta de salida (donde se guardaran todos los tiempos en un solo csv). Ejemplo de ejecucion:
```bash
 python3 filtrocsv.py tiempos_masc series_masc_1
```
- Usamos unir_csv.py para unir todos los csvs de la carpeta series_x_1 en un solo csv. Ejemplo de ejecucion:
```bash
 python3 unir_csv.py series_masc_1 series_masc.csv
```
- series_masc.csv se debe de usar para crear las hojas en el excel de medias
- Se eliminaran las hojas series_masc y series_fem del excel y se crearan de nuevo esas hojas dandole a obtener datos de csv y seleccionando los nuevos csvs
- Al importarlos se debe de seleccionar la opcion de obtener formato de las primeras lineas
- Los proximos pasos se encuentran en el readme de la carpeta software_medias


## Eliminar nombres de nadadores que se repiten y ya no estan en el club
- Seleccionar el nadador dentro del codigo de rm_names.py 
- Ejecutar el script rm_names.py. Este script toma como parametros el csv. Ejemplo de ejecucion:
```bash
 python3 rm_names.py series_masc_1.csv
```

Para añadir a las versiones de prubeas individuales:
-Seleccionar el numero de combinacion del equipo 1 de la lista de medias y que te de el outpt de todas las combinaciones posibles con esos dos nadadores
ordenadas de menor a mayor puntuacion.
