# Szybki Start

Przewodnik do szybkiego rozpoczęcia pracy z python-transform.

## 1. Instalacja (2 minuty)

### Wymagania systemowe
- Python 3.8 lub nowszy
- pip (menedżer pakietów Python)

### Procedura instalacji

```bash
# Klonuj repozytorium
git clone https://github.com/yourusername/python-transform.git
cd python-transform

# Zainstaluj zależności
pip install -r requirements.txt
```

## 2. Podstawowe użycie (1 minuta)

### Konwersja pojedynczego PDF

```bash
python main.py moj_dokument.pdf
```

Plik będzie skonwertowany do `./output/moj_dokument.md`

### Konwersja całego katalogu

```bash
python main.py ./moje_dokumenty -d
```

## 3. Przykłady (5 minut)

### Przykład 1: PDF

```bash
# Konwertuj plik PDF
python main.py raport.pdf -o ./markdown_output
```

**Output: `./markdown_output/raport.md`**

```markdown
# PDF Document
**Liczba stron:** 3

## Strona 1

Zawartość tekstu ze strony 1...

### Tabela 1
| Kolumna 1 | Kolumna 2 |
|-----------|-----------|
| Dane 1    | Dane 2    |
```

### Przykład 2: Word dokument

```bash
python main.py instrukcja.docx -o ./docs
```

**Output: `./docs/instrukcja.md`**

```markdown
# Instrukcja

## Rozdziału 1

Zawartość z formatowaniem...

**Tekst pogrubiony** i *kursywa*
```

### Przykład 3: Obrazy

```bash
# Konwertuj wszystkie obrazy z metadanymi
python main.py ./zdjecia -d -o ./obrazy_md
```

### Przykład 4: Obrazy z wyciągnięciem tekstu (OCR)

```bash
# Wymaga Tesseract-OCR
python main.py ./przeskanowane -d --ocr -o ./tekst
```

## 4. Obsługiwane formaty

| Format | Rozszerzenie |
|--------|------------|
| PDF | `.pdf` |
| Word | `.docx` |
| Obrazy | `.png`, `.jpg`, `.bmp`, `.gif` |

## 5. Ustaw Tesseract OCR (Opcjonalnie)

### Windows

1. Pobierz z: https://github.com/UB-Mannheim/tesseract/wiki
2. Zainstaluj
3. W Python:

```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Linux

```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-pol
```

### macOS

```bash
brew install tesseract
```

## 6. Zaawansowane użycie

### Konwersja rekursywna

```bash
python main.py ./projekt -d -r -o ./projekt_markdown
```

Konwertuje wszystkie obsługiwane pliki rekursywnie ze wszystkich podkatalogów.

### Niestandardowy katalog wyjściowy

```bash
python main.py dokument.pdf -o /moja/sciezka/output
```

### Kombinacja opcji

```bash
# Katalog, rekursywnie, z OCR, do niestandardowego outputu
python main.py ./dokumenty -d -r --ocr -o ./wynik
```

## 7. Rozwiązywanie problemów

### Problem: "No module named 'docx'"

```bash
pip install python-docx
```

### Problem: Tesseract not found

Windows:
- Pobierz i zainstaluj z: https://github.com/UB-Mannheim/tesseract/wiki
- Ustaw ścieżkę w kodzie

Linux/Mac:
```bash
# Linux
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract
```

## 8. Dalsze kroki

- 📖 Przeczytaj [README.md](README.md) aby poznać wszystkie opcje
- 🔧 Sprawdź [examples.py](examples.py) dla więcej przykładów
- 🐛 Zgłoś błędy na [GitHub Issues](https://github.com/yourusername/python-transform/issues)
- 🤝 Weź udział w [CONTRIBUTING.md](CONTRIBUTING.md)

## 9. Pomoc

```bash
# Pełna dokumentacja opcji
python main.py -h

# Czy masz pytania? Otwórz issue!
```

---

Powodzenia z python-transform! 🚀
