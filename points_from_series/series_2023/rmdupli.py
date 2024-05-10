import pandas as pd

# Función para eliminar líneas duplicadas de un archivo CSV y guardar el resultado
def remove_duplicates_from_csv(input_file_path, output_file_path):
    # Leer el archivo CSV usando pandas
    data = pd.read_csv(input_file_path)
    
    # Eliminar duplicados
    unique_data = data.drop_duplicates()
    
    # Guardar el DataFrame sin duplicados en un nuevo archivo CSV
    unique_data.to_csv(output_file_path, index=False)

# La llamada a la función está comentada para evitar su ejecución accidental
remove_duplicates_from_csv("series.csv", "series2.csv")
