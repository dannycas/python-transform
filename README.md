# Document & Image to Markdown Converter

Skrypt do konwersji dokumentów (PDF, DOCX) i obrazów (PNG, JPG, itd.) na pliki Markdown.

## Features

- ✅ **Konwersja PDF** - Ekstrakcja tekstu i tabel z plików PDF
- ✅ **Konwersja DOCX** - Obsługa formatowania, nagłówków, tabel
- ✅ **Konwersja obrazów** - PNG, JPG, BMP, GIF, TIFF, WebP
- ✅ **OCR dla obrazów** - Opcjonalna ekstrakcja tekstu z obrazów
- ✅ **Konwersja wsadowa** - Przetwarzanie całych katalogów
- ✅ **Rekursywna konwersja** - Obsługa podkatalogów

## Wymagania

- Python 3.8+
- Biblioteki Python (patrz `requirements.txt`)
- (Opcjonalnie) Tesseract-OCR dla funkcji OCR obrazów

## Instalacja

### 1. Klonuj repozytorium

```bash
git clone https://github.com/yourusername/python-transform.git
cd python-transform
```

### 2. Zainstaluj zależności Python

```bash
pip install -r requirements.txt
```

### 3. (Opcjonalnie) Zainstaluj Tesseract-OCR

#### Windows

Pobierz instalator z: https://github.com/UB-Mannheim/tesseract/wiki

```bash
# Po instalacji, ustaw zmienną środowiska w kodzie lub w Pythonie
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-pol  # Dla polskiego
```

#### macOS

```bash
brew install tesseract
brew install tesseract-lang  # Dla dodatkowych języków
```

## 🧪 Testy

Projekt zawiera kompleksową suite testów:

```bash
# Uruchom wszystkie testy (69 testów)
python run_tests.py

# Tylko unit testy
python run_tests.py -u

# Tylko integration testy
python run_tests.py -i

# Z pokryciem kodu
pytest --cov=converters --cov=main --cov=utils --cov-report=html
```

**Test Statistics:**
- 📊 69 testów (44 unit + 25 integration)
- 📈 ~91% pokrycie kodu
- ✅ Wszystkie formaty obsługiwane

Więcej w [TESTING.md](TESTING.md) oraz [TESTS_QUICK_REFERENCE.md](TESTS_QUICK_REFERENCE.md)

## Użycie

### Konwersja pojedynczego pliku

```bash
python main.py input.pdf
```

Plik Markdown będzie utworzony w katalogu `./output/`

### Konwersja z określeniem katalogu wyjściowego

```bash
python main.py input.pdf -o ./moje_markdown_pliki
```

### Konwersja całego katalogu

```bash
python main.py ./dokumenty -d
```

Konwertuje wszystkie obsługiwane pliki w katalogu `./dokumenty`

### Konwersja rekursywna (z podkatalogami)

```bash
python main.py ./dokumenty -d -r
```

### Konwersja z OCR dla obrazów

```bash
python main.py ./obrazy -d --ocr
```

Ekstrakcja tekstu z obrazów (wymaga Tesseract-OCR)

### Pełna pomoc

```bash
python main.py -h
```

## Obsługiwane formaty

| Format | Rozszerzenie | Obsługa |
|--------|-------------|---------|
| PDF | `.pdf` | ✅ Tekst, tabele |
| Word | `.docx`, `.doc` | ✅ Tekst, formatowanie, tabele |
| PNG | `.png` | ✅ Metadane, OCR |
| JPEG | `.jpg`, `.jpeg` | ✅ Metadane, OCR |
| BMP | `.bmp` | ✅ Metadane, OCR |
| GIF | `.gif` | ✅ Metadane, OCR |
| TIFF | `.tiff` | ✅ Metadane, OCR |
| WebP | `.webp` | ✅ Metadane, OCR |

## Przykłady

### Przykład 1: Konwersja raportu PDF

```bash
python main.py raport_2024.pdf -o ./raporty_markdown
```

Rezultat: `./raporty_markdown/raport_2024.md`

### Przykład 2: Konwersja dokumentu Word z formatowaniem

```bash
python main.py instrukcja.docx -o ./dokumentacja
```

Rezultat: Markdown z zachowanym formatowaniem (nagłówkami, tabelami, itp.)

### Przykład 3: Ekstrakcja tekstu z wielu obrazów

```bash
python main.py ./przeskanowane_dokumenty -d -r --ocr -o ./tekst_z_skanow
```

Konwertuje wszystkie obrazy w katalogu rekursywnie, ekstrakcja tekstu za pomocą OCR

### Przykład 4: Konwersja projektu ze źródłami

```bash
python main.py ./projekt -d -r -o ./markdown_wersja
```

Konwertuje wszystkie obsługiwane pliki w całym projekcie

## Struktura projektu

```
python-transform/
├── main.py                 # Główny skrypt
├── requirements.txt        # Zależności Python
├── README.md              # Dokumentacja (ten plik)
├── converters/
│   ├── __init__.py
│   ├── base_converter.py  # Klasa bazowa
│   ├── pdf_converter.py   # Konwerter PDF
│   ├── docx_converter.py  # Konwerter DOCX
│   └── image_converter.py # Konwerter obrazów
└── output/                # Domyślny katalog wyjściowy
```

## Parametry konwertowania

### Ogólne

- `input` - Plik lub katalog do konwersji (wymagane)
- `-o, --output` - Katalog wyjściowy (domyślnie: `./output`)
- `-d, --directory` - Tryb katalogowy
- `-r, --recursive` - Szukaj rekursywnie

### Specyficzne dla obrazów

- `--ocr` - Użyj OCR do ekstrakcji tekstu z obrazów

## Uwagi i tips

### OCR

- OCR wymaga dodatkowe czasu na przetwarzanie
- Dla lepszych rezultatów OCR, upewnij się, że obrazy mają dobrej jakości tekst
- Obsługiwane języki: angielski (domyślnie), polski (jeśli zainstalowany)

### Wydajność

- Konwersja dużych plików PDF może trwać dłużej
- Dla dużych zbiorów obrazów, użyj konwersji rekursywnej

### Limity

- Bardzo duże PDF (>100MB) mogą wymagać więcej pamięci RAM
- Obrazy o niskiej jakości mogą dać słabe resultat OCR

## Rozwiązywanie problemów

### Problem: "ModuleNotFoundError: No module named 'docx'"

**Rozwiązanie:**
```bash
pip install python-docx
```

### Problem: "Tesseract is not installed or it's not in your PATH"

**Rozwiązanie Windows:**
1. Pobierz i zainstaluj Tesseract z: https://github.com/UB-Mannheim/tesseract/wiki
2. Ustaw ścieżkę w kodzie:
```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Problem: "No module named 'converters'"

**Rozwiązanie:**
```bash
# Uruchom z głównego katalogu projektu
python main.py input.pdf
```

## Rozszerzanie

Aby dodać obsługę nowego formatu:

1. Utwórz nowy konwerter dziedziczący z `BaseConverter`:

```python
# converters/csv_converter.py
from .base_converter import BaseConverter

class CSVConverter(BaseConverter):
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        # Implementacja konwersji
        pass
```

2. Dodaj do `main.py`:

```python
from converters.csv_converter import CSVConverter

CONVERTERS = {
    # ...
    '.csv': CSVConverter,
}
```

## Licencja

MIT

## Autor

Python Transform Project

## Kontakt i wsparcie

Aby zgłosić błędy lub zaproponować funkcje, utwórz issue w repozytorium.
