import re
import csv
import sys

def parse_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Ajustar la expresión regular para incluir una mejor captura del final del evento
    pattern = r'(\d{1,3}\s+m\s+[^\n]+?\d+)\s+FINAL\s+(?:Club Pista Nome MarcaFINAL 1\nAno Licenza\n)?(.*?)(?=(\d{1,3}\s+m\s+[^\n]+?\d+)\s+FINAL|$)'
    events = re.findall(pattern, text, re.DOTALL)

    results = []
    for match in events:
        if len(match) == 3:
            event_name, swimmers_text, _ = match
        else:
            continue  # Si no tiene los tres grupos capturados correctamente, ignorar este match
        
        event_name = event_name.strip()
        swimmers_data = []
        
        for line in swimmers_text.strip().split('\n'):
            parts = re.split(r'\s(?=\d{1,2}:\d{2}\.\d{2})', line.strip())
            if len(parts) >= 2:
                nome_club = ' '.join(parts[0].split()[:-1])  # Elimina el último elemento, típicamente un código
                marca = parts[-1]
                swimmers_data.append(f"{nome_club} {marca}")
        
        results.append((event_name, swimmers_data))

    return results

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for event_name, swimmers in data:
            writer.writerow([event_name])  # Escribir el nombre del evento
            for swimmer in swimmers:
                writer.writerow([swimmer])  # Escribir los datos de cada nadador
            writer.writerow([])  # Espacio en blanco entre eventos

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input text file path> <output CSV file path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    parsed_data = parse_text(input_file_path)
    save_to_csv(parsed_data, output_file_path)

if __name__ == "__main__":
    main()
