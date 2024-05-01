import sys
import os
from PyPDF2 import PdfReader
import re
import tabula

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            page_text = re.sub(r'Page \d+ of \d+', '', page_text)  # Cleans footer/header
            text.append(page_text)
    return '\n'.join(text)

def extract_tables_to_csv(pdf_path, csv_path):
    tabula.convert_into(pdf_path, csv_path, output_format="csv", pages="all")

def save_text_to_file(text, text_path):
    with open(text_path, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <PDF file path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    base_name = os.path.splitext(pdf_path)[0]
    text_output_path = base_name + '.txt'
    csv_output_path = base_name + '.csv'

    text = extract_text_from_pdf(pdf_path)
    save_text_to_file(text, text_output_path)
    extract_tables_to_csv(pdf_path, csv_output_path)

if __name__ == "__main__":
    main()
