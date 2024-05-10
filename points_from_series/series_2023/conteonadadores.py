import pandas as pd

# Función para contar el número de nadadores por prueba y por club y guardar el resultado en un archivo CSV
def count_swimmers_by_event_and_club(input_file_path, output_file_path):
    # Leer el archivo CSV usando pandas
    data = pd.read_csv(input_file_path, sep=';')
    
    # Agrupar por las columnas 'Prueba' y 'Club' y contar el número de nadadores
    swimmers_count = data.groupby(['Prueba', 'Club']).size().reset_index(name='Número de Nadadores')
    
    # Guardar los resultados en un archivo CSV
    swimmers_count.to_csv(output_file_path, index=False)

# La llamada a la función está comentada para evitar su ejecución accidental
# count_swimmers_by_event_and_club("path_to_your_input_file.csv", "path_to_your_output_file.csv")

# La llamada a la función está comentada para evitar su ejecución accidental
count_result = count_swimmers_by_event_and_club("series_segundos.csv", "conteo_nadadores.csv")
print(count_result)
