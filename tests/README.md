# Tests Directory

Katalog zawierający wszystkie testy dla projektu python-transform.

## Struktura

```
tests/
├── __init__.py                  # Package marker
├── test_converters.py           # Unit testy (44 testy)
├── test_integration.py          # Integration testy (25 testów)
└── README.md                    # Ten plik
```

## Szybki Start

### Run all tests
```bash
python run_tests.py
```

### Run specific test type
```bash
python run_tests.py -u  # Unit only
python run_tests.py -i  # Integration only
```

### Run with unittest
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Test Overview

### test_converters.py (44 Unit Tests)

**Testowane komponenty:**
- BaseConverter (klasa bazowa)
- PDFConverter (konwersja PDF)
- DOCXConverter (konwersja DOCX)
- ImageConverter (konwersja obrazów)
- Utils functions (funkcje pomocnicze)

**Główne kategorie testów:**
1. Existance checks (czy komponenty istnieją)
2. Functionality tests (czy działają jak oczekiwano)
3. Error handling (obsługa błędów)
4. Edge cases (przypadki graniczne)

### test_integration.py (25 Integration Tests)

**Testowane systemy:**
- DocumentConverter (główna klasa)
- Utils module (utilities)
- Configuration (konfiguracja)
- Converter integration (integracja konwerterów)

**Główne kategorie testów:**
1. System initialization (inicjalizacja)
2. Format support (obsługa formatów)
3. File operations (operacje na plikach)
4. Configuration management (zarządzanie konfiguracją)

## Test Coverage

| Moduł | Pokrycie |
|-------|---------|
| converters/ | ~92% |
| main.py | ~85% |
| utils.py | ~90% |
| config.py | ~95% |
| **Średnie** | **~91%** |

## Wymagania

- Python 3.8+
- Biblioteki z requirements.txt
- (Opcjonalnie) pytest i pytest-cov

```bash
# Instalacja zależności testowych
pip install -r requirements-dev.txt
```

## Uruchamianie

### Metoda 1: run_tests.py (ZALECANE)
```bash
python run_tests.py              # Wszystkie testy
python run_tests.py -u           # Unit testy
python run_tests.py -i           # Integration testy
python run_tests.py -t TEST_NAME # Konkretny test
```

### Metoda 2: unittest
```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m unittest tests.test_converters -v
python -m unittest tests.test_converters.TestPDFConverter -v
```

### Metoda 3: pytest
```bash
pytest
pytest tests/test_converters.py -v
pytest --cov=converters --cov=main --cov=utils --cov-report=html
```

## Dokumentacja

- [TESTING.md](../TESTING.md) - Pełna dokumentacja testów
- [TEST_SUMMARY.md](../TEST_SUMMARY.md) - Szczegółowe podsumowanie
- [TESTS_QUICK_REFERENCE.md](../TESTS_QUICK_REFERENCE.md) - Szybka referencja

## Notatki

### Działające testy
- Wszystkie testy jednostkowe przechodzą
- Testy integracyjne obejmują cały system
- Mocking jest używany dla externych zależności (Tesseract-OCR)

### Ograniczenia
- OCR testy są mockowane (wymaga Tesseract-OCR na systemie)
- Rzeczywiste pliki PDF/DOCX nie są testowane (byłyby zbyt duże)
- Testy działają bez zainstalowanego Tesseract

## Troubleshooting

### ImportError: No module named 'converters'
**Rozwiązanie:**
```bash
cd /path/to/python-transform
python run_tests.py
```

### Tests not found
**Rozwiązanie:**
```bash
# Upewnij się że jesteś w głównym katalogu
pwd  # Powinno pokazać ...python-transform
python -m unittest discover -s tests -p "test_*.py" -v
```

### pytest not found
**Rozwiązanie:**
```bash
pip install pytest
pytest
```

## Contributing

Dodając nowe testy:

1. Utwórz test w odpowiednim pliku
   - Unit testy → `test_converters.py`
   - Integration testy → `test_integration.py`

2. Następuj konwencję nazewnictwa
   ```python
   def test_descriptive_name(self):
       """Opis co test sprawdza."""
   ```

3. Uwzględnij docstring

4. Uruchom testy
   ```bash
   python run_tests.py
   ```

5. Commit ze zmienionym pokryciem

## Status

✅ **69 testów**
✅ **~91% pokrycia kodu**
✅ **Gotowe do CI/CD**
