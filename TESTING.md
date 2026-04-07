# Dokumentacja Testów dla python-transform

## Przegląd

Projekt python-transform ma kompleksową suite testów obejmującą:

- **Unit testy** (testy konwerterów)
- **Testy integracyjne** (testy systemu jako całości)
- **Coverage reporting** (raport pokrycia kodu)

## Struktura testów

```
tests/
├── __init__.py
├── test_converters.py         # Unit testy
└── test_integration.py        # Testy integracyjne
```

## Uruchamianie testów

### Metoda 1: Używając run_tests.py

```bash
# Wszystkie testy
python run_tests.py

# Tylko unit testy
python run_tests.py -u

# Tylko testy integracyjne
python run_tests.py -i

# Konkretny test
python run_tests.py -t tests.test_converters.TestPDFConverter

# Kontrola verbosity
python run_tests.py -v 1  # Minimum
python run_tests.py -v 2  # Maximum
```

### Metoda 2: Używając unittest (Python)

```bash
# Wszystkie testy
python -m unittest discover -s tests -p "test_*.py"

# Konkretny plik testów
python -m unittest tests.test_converters

# Konkretna klasa testów
python -m unittest tests.test_converters.TestPDFConverter

# Konkretny test
python -m unittest tests.test_converters.TestPDFConverter.test_converter_exists
```

### Metoda 3: Używając pytest (jeśli zainstalowany)

```bash
# Instalacja
pip install pytest pytest-cov

# Wszystkie testy z raportem
pytest

# Testy z pokryciem kodu
pytest --cov=converters --cov=main --cov=utils --cov-report=html

# Verbose
pytest -v

# Konkretny plik
pytest tests/test_converters.py -v

# Konkretna klasa
pytest tests/test_converters.py::TestPDFConverter -v

# Konkretny test
pytest tests/test_converters.py::TestPDFConverter::test_converter_exists -v
```

## Unit testy (test_converters.py)

### Klasy testowe:

#### 1. TestBaseConverter
Testy dla klasy bazowej `BaseConverter`:
- `test_converter_exists` - Sprawdzenie istnienia konwertera
- `test_create_markdown_header_level_*` - Tworzenie nagłówków MD
- `test_escape_markdown` - Escapeowanie znaków specjalnych

#### 2. TestPDFConverter
Testy dla klasy `PDFConverter`:
- `test_converter_exists` - Konwerter istnieje
- `test_converter_is_base_converter` - Dziedziczenie
- `test_table_to_markdown_*` - Konwersja tabel
- `test_convert_nonexistent_file` - Obsługa błędów

#### 3. TestDOCXConverter
Testy dla klasy `DOCXConverter`:
- `test_get_header_level_*` - Poziomy nagłówków
- `test_format_run_*` - Formatowanie tekstu (bold, italic)
- `test_table_to_markdown` - Konwersja tabel
- `test_convert_nonexistent_file` - Obsługa błędów

#### 4. TestImageConverter
Testy dla klasy `ImageConverter`:
- `test_get_mime_type_*` - MIME types dla formatów
- `test_convert_nonexistent_image` - Obsługa błędów

#### 5. TestUtilsFunctions
Testy dla funkcji z `utils.py`:
- `test_is_supported_*` - Sprawdzanie obsługiwaności formatów
- `test_is_not_supported_*` - Nieobsługiwane formaty

## Testy integracyjne (test_integration.py)

### Klasy testowe:

#### 1. TestDocumentConverter
Testy dla głównej klasy `DocumentConverter`:
- `test_converter_initialization` - Inicjalizacja
- `test_converter_has_supported_formats` - Formaty obsługiwane
- `test_pdf_in_supported_formats` - PDF obsługiwany
- `test_*_in_supported_formats` - Inne formaty

#### 2. TestUtilsIntegration
Testy integracyjne dla utils:
- `test_get_supported_extensions` - Lista rozszerzeń
- `test_is_supported_case_insensitive` - Case-insensitivity
- `test_ensure_output_dir` - Tworzenie katalogów
- `test_format_file_size` - Formatowanie rozmiaru
- `test_get_supported_files_*` - Filtrowanie plików

#### 3. TestConverterIntegration
Testy integracyjne konwerterów:
- `test_all_converters_exist` - Import konwerterów
- `test_converters_are_subclasses_of_base` - Dziedziczenie
- `test_converters_have_convert_method` - Metody konwersji

#### 4. TestConfigurationModule
Testy dla `config.py`:
- `test_config_import` - Import modułu
- `test_config_default/fast/full` - Różne konfiguracje

## Przypadki testowe (Test Cases)

### PDF Converter

| Test | Cel |
|------|-----|
| `test_converter_exists` | ✓ Konwerter istnieje |
| `test_table_to_markdown_basic` | ✓ Konwersja prostych tabel |
| `test_table_to_markdown_with_none_values` | ✓ Obsługa None w tabelach |
| `test_table_to_markdown_empty_table` | ✓ Puste tabele |
| `test_table_to_markdown_single_row` | ✓ Tabela z jednym wierszem |
| `test_convert_nonexistent_file` | ✓ Nieistniejące pliki |

### DOCX Converter

| Test | Cel |
|------|-----|
| `test_converter_exists` | ✓ Konwerter istnieje |
| `test_get_header_level_*` | ✓ Poziomy nagłówków (1-6) |
| `test_format_run_*` | ✓ Formatowanie (bold, italic itp.) |
| `test_table_to_markdown` | ✓ Konwersja tabel DOCX |
| `test_convert_nonexistent_file` | ✓ Obsługa błędów |

### Image Converter

| Test | Cel |
|------|-----|
| `test_converter_exists` | ✓ Konwerter istnieje |
| `test_get_mime_type_*` | ✓ MIME types dla formatów |
| `test_convert_nonexistent_image` | ✓ Obsługa błędów |

## Pokrycie kodu (Coverage)

### Generowanie raportu pokrycia

```bash
# Instalacja (jeśli potrzebna)
pip install pytest-cov

# Generowanie raportu HTML
pytest --cov=converters --cov=main --cov=utils --cov-report=html

# Raport będzie w: htmlcov/index.html
```

### Oczekiwane pokrycie

- **converters/**: >90%
- **main.py**: >85%
- **utils.py**: >85%
- **config.py**: >80%

## Mocking i Fixtures

Testy używają `unittest.mock` do mockowania:
- Objektów `docx.text.paragraph.CT_P`
- Tabel i komórek dokumentów
- Konfiguracji OCR

## Przykłady uruchamiania

### Szybkie testy

```bash
# Tylko krytyczne testy
python -m unittest tests.test_converters -v
```

### Pełny test z raportem

```bash
# Wszystkie testy z pokryciem
pytest --cov=converters --cov=main --cov=utils \
       --cov-report=html --cov-report=term -v
```

### Monitorowanie zmian

```bash
# Uruchamiaj testy po każdej zmianie (wymaga pytest-watch)
pip install pytest-watch
ptw
```

## Rozwiązywanie problemów

### ImportError: No module named 'converters'

**Rozwiązanie:**
```bash
# Uruchom z głównego katalogu
cd /path/to/python-transform
python run_tests.py
```

### Test timeout

**Rozwiązanie:**
```bash
# Zwiększ timeout
pytest --timeout=300
```

### Problemy z pytest

**Rozwiązanie:**
```bash
# Używaj unittest zamiast pytest
python -m unittest discover -s tests
```

## Best Practices

1. **Izolacja testów** - Każdy test jest niezależny
2. **Czyszczenie** - `tearDown()` czyści zasoby
3. **Descriptive names** - Nazwy opisują co test sprawdza
4. **Docstrings** - Każdy test ma opis
5. **Mocking** - Mockuj zewnętrzne zależności
6. **Fixtures** - Reużywalne dane testowe w `setUp()`

## CI/CD Integration

### GitHub Actions

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements-dev.txt
      - run: pytest --cov
```

## Dodawanie nowych testów

### Template

```python
class TestNewFeature(unittest.TestCase):
    """Testy dla nowej funkcji."""
    
    def setUp(self):
        """Przygotowanie."""
        pass
    
    def test_basic_functionality(self):
        """Test funkcjonalności."""
        result = some_function()
        self.assertIsNotNone(result)
    
    def test_error_handling(self):
        """Test obsługi błędów."""
        with self.assertRaises(ExpectedException):
            some_function(invalid_input)
    
    def tearDown(self):
        """Czyszczenie."""
        pass
```

## Statystyki testów

```
Unit Tests:       25+
Integration Tests: 20+
Total:            45+
Functions Tested: >90%
```

---

**Last Updated:** 2024-04-07
**Status:** Complete ✓
