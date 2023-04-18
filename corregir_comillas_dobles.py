import os
import csv
import sys
dir_path = sys.argv[1]

for filename in os.listdir(dir_path):
    if filename.endswith("1.csv"):  # Filtrar solo archivos que terminan en "masc_1"
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "r+") as file:
            content = file.read()
            content = content.replace('""', '"')  # Reemplazar las dobles comillas por una sola
            file.seek(0)
            file.write(content)
            file.truncate()