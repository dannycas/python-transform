"""
Przykład użycia skryptu do konwersji dokumentów.
"""

from pathlib import Path
from main import DocumentConverter


def example_1_single_file():
    """Konwersja pojedynczego pliku PDF."""
    print("=" * 50)
    print("Przykład 1: Konwersja pojedynczego PDF")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_file('example.pdf')


def example_2_single_docx():
    """Konwersja pojedynczego pliku DOCX."""
    print("=" * 50)
    print("Przykład 2: Konwersja pojedynczego DOCX")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_file('example.docx')


def example_3_directory():
    """Konwersja wszystkich plików w katalogu."""
    print("=" * 50)
    print("Przykład 3: Konwersja całego katalogu")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_directory('./documents')


def example_4_recursive():
    """Konwersja rekursywna (z podkatalogami)."""
    print("=" * 50)
    print("Przykład 4: Konwersja rekursywna")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_directory('./documents', recursive=True)


def example_5_images_with_ocr():
    """Konwersja obrazów z OCR."""
    print("=" * 50)
    print("Przykład 5: Konwersja obrazów z OCR")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_directory('./images', use_ocr=True)


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("Document & Image to Markdown Converter - Examples")
    print("=" * 50 + "\n")
    
    print("INSTRUKCJE:")
    print("-" * 50)
    print()
    print("Do uruchomienia przykładów:")
    print()
    print("1. Umieść pliki do konwersji w odpowiednich katalogach:")
    print("   - example.pdf, example.docx w głównym katalogu")
    print("   - Obrazy w ./images/")
    print("   - Dokumenty w ./documents/")
    print()
    print("2. Odkomentuj odpowiedni przykład (rozkomentuj linię z convert_)")
    print()
    print("3. Uruchom skrypt:")
    print("   python examples.py")
    print()
    print("ALTERNATYWNIE - Użyj bezpośrednio command line:")
    print("-" * 50)
    print()
    print("# Pojedynczy plik:")
    print("python main.py example.pdf")
    print()
    print("# Katalog:")
    print("python main.py ./documents -d")
    print()
    print("# Rekursywnie:")
    print("python main.py ./documents -d -r")
    print()
    print("# Z OCR:")
    print("python main.py ./images -d --ocr")
    print()
