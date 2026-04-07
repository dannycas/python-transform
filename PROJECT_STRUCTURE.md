# Struktura projektu - python-transform

## 📁 Struktura katalogów

```
python-transform/
│
├── 📄 main.py                    # Główny skrypt konwersji
├── 📄 config.py                  # Konfiguracja projektu
├── 📄 utils.py                   # Utility functions
├── 📄 examples.py                # Przykłady użycia
│
├── 📁 converters/                # Moduł konwerterów
│   ├── __init__.py
│   ├── base_converter.py        # Klasa bazowa
│   ├── pdf_converter.py         # Konwerter PDF
│   ├── docx_converter.py        # Konwerter DOCX
│   └── image_converter.py       # Konwerter obrazów
│
├── 📁 tests/                     # Testy
│   ├── __init__.py
│   └── test_converters.py       # Testy konwerterów
│
├── 📁 output/                    # Domyślny katalog na markdown'y (generowany)
│
├── 📄 requirements.txt           # Zależności Python
├── 📄 setup.py                   # Setup dla instalacji pakietu
│
├── 📖 README.md                  # Główna dokumentacja
├── 📖 QUICKSTART.md             # Szybki start (ten plik)
├── 📖 CONTRIBUTING.md           # Przewodnik dla współtwórców
├── 📖 CHANGELOG.md              # Historia zmian
├── 📄 LICENSE                   # Licencja MIT
└── 📄 .gitignore                # Reguły dla git
```

## 🚀 Szybki Start (3 kroki)

### 1. Instalacja
```bash
cd python-transform
pip install -r requirements.txt
```

### 2. Konwersja
```bash
# Pojedynczy plik
python main.py dokument.pdf

# Katalog
python main.py ./dokumenty -d

# Z OCR
python main.py ./obrazy -d --ocr
```

### 3. Output
```
./output/
├── dokument.md
├── inne_dokumenty.md
└── ...
```

## 📋 Obsługiwane formaty

| Format | Rozszerzenie | Obsługa |
|--------|------------|---------|
| PDF | .pdf | ✅ Tekst, tabele |
| Word | .docx | ✅ Tekst, formatowanie |
| Obrazy | .png, .jpg | ✅ + OCR opcjonalnie |

## 🔧 Opcje wiersza poleceń

```bash
python main.py -h

Pozycyjne argumenty:
  input                Plik lub katalog do konwersji

Argumenty opcjonalne:
  -o, --output OUT     Katalog wyjściowy (domyślnie: ./output)
  -d, --directory      Tryb katalogowy
  -r, --recursive      Szukaj rekursywnie
  --ocr                Użyj OCR dla obrazów
```

## 📦 Kluczowe komponenty

### main.py
Główna klasa `DocumentConverter` obsługująca:
- Konwersję plików
- Konwersję katalogów
- Mapowanie typów plików na konwertery
- Obsługa błędów i logowanie

### converters/
- **base_converter.py** - Abstrakcyjna klasa bazowa
- **pdf_converter.py** - Ekstrakcja tekstu i tabel z PDF
- **docx_converter.py** - Konwersja z zachowaniem formatowania
- **image_converter.py** - Konwersja obrazów z opcjonalnym OCR

### utils.py
Funkcje pomocnicze:
- `is_supported()` - Sprawdzenie obsługiwaności formatu
- `get_supported_files()` - Lista obsługiwanych plików
- `format_file_size()` - Formatowanie rozmiaru
- `print_conversion_summary()` - Podsumowanie

## 🎯 Przykłady użycia

### Konwersja raportu PDF
```bash
python main.py raport_Q1_2024.pdf -o ./raporty_md
```
Output: `./raporty_md/raport_Q1_2024.md`

### Konwersja całego projektu
```bash
python main.py ./projekt -d -r -o ./projekt_markdown
```
Konwertuje wszystkie pliki rekursywnie

### Ekstrakcja tekstu z skanów
```bash
python main.py ./przeskanowane_dokumenty -d --ocr -o ./tekst
```
Wymaga: Tesseract-OCR

## 🧪 Testy

```bash
# Uruchom testy
python -m pytest tests/

# Inne polecenia
python -m pytest tests/test_converters.py -v
python -m pytest tests/test_converters.py::TestPDFConverter -v
```

## 📝 Konfig (config.py)

```python
from config import get_config

# Pre-built konfiguracje
config = get_config('default')   # Domyślna
config = get_config('fast')      # Szybka
config = get_config('full')      # Pełna z OCR
```

## 🔗 Zależności

- `PyPDF2` 3.0.1 - Przetwarzanie PDF
- `pdfplumber` 0.9.0 - Ekstrakcja tabel
- `python-docx` 0.8.11 - Przetwarzanie DOCX
- `Pillow` 10.0.0 - Przetwarzanie obrazów
- `pytesseract` 0.3.10 - OCR
- `markdown` 3.5.0 - Obsługa Markdown

## 🐛 Rozwiązywanie problemów

### Błąd: "ModuleNotFoundError"
```bash
pip install -r requirements.txt --upgrade
```

### OCR nie działa
- Zainstaluj Tesseract-OCR
- Ustaw ścieżkę w kodzie

### Out of Memory
- Konwertuj mniejsze partie
- Zmniejsz rozmiar obrazów

## 📚 Dokumentacja

- [README.md](README.md) - Pełna dokumentacja
- [QUICKSTART.md](QUICKSTART.md) - Szybki start
- [examples.py](examples.py) - Przykłady kodu
- [CONTRIBUTING.md](CONTRIBUTING.md) - Dla developerów

## 🚢 Deployment

### Jako skrypt
```bash
python main.py input.pdf
```

### Jako moduł
```bash
pip install -e .
python-transform input.pdf
```

### Setup.py
```bash
python setup.py install
```

## 📝 Licencja

MIT - Patrz [LICENSE](LICENSE)

## 🤝 Wkład

Zainteresowany w udziale? Przeczytaj [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Ostatnia aktualizacja:** 2024-04-07
**Status:** v0.1.0 (Alpha)
