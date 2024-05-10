import pandas as pd

# Función para leer, filtrar y guardar el archivo CSV
def filter_and_save_csv(input_file_path, output_file_path):
    # Leer el archivo CSV usando pandas con el separador especificado
    data = pd.read_csv(input_file_path, sep=';', header=None)
    
    # Lista de palabras claves para filtrar
    keywords = ['ARZUA', 'CASINO', 'CNMOS']
    
    # Filtrar las filas que no contienen ninguna de las palabras clave en cualquiera de las columnas
    filtered_data = data[~data.apply(lambda row: row.astype(str).str.contains('|'.join(keywords)).any(), axis=1)]
    
    # Guardar los datos filtrados en un nuevo archivo CSV
    filtered_data.to_csv(output_file_path, index=False, sep=';')

# La llamada a la función está comentada para evitar su ejecución accidental
filter_and_save_csv("series2024.csv", "filtrado.csv")
