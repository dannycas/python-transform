# Test Documentation for python-transform

## Overview

The python-transform project has a comprehensive test suite including:

- **Unit tests** (converter tests)
- **Integration tests** (system-level tests)
- **Coverage reporting** (code coverage report)

## Test structure

```
tests/
├── __init__.py
├── test_converters.py         # Unit tests
└── test_integration.py        # Integration tests
```

## Running tests

### Method 1: Using run_tests.py

```bash
# All tests
python run_tests.py

# Unit tests only
python run_tests.py -u

# Integration tests only
python run_tests.py -i

# Specific test
python run_tests.py -t tests.test_converters.TestPDFConverter

# Verbosity control
python run_tests.py -v 1  # Minimum
python run_tests.py -v 2  # Maximum
```

### Method 2: Using unittest (Python)

```bash
# All tests
python -m unittest discover -s tests -p "test_*.py"

# Specific test file
python -m unittest tests.test_converters

# Specific test class
python -m unittest tests.test_converters.TestPDFConverter

# Specific test
python -m unittest tests.test_converters.TestPDFConverter.test_converter_exists
```

### Method 3: Using pytest (if installed)

```bash
# Installation
pip install pytest pytest-cov

# All tests with report
pytest

# Tests with code coverage
pytest --cov=converters --cov=main --cov=utils --cov-report=html

# Verbose
pytest -v

# Specific file
pytest tests/test_converters.py -v

# Specific class
pytest tests/test_converters.py::TestPDFConverter -v

# Specific test
pytest tests/test_converters.py::TestPDFConverter::test_converter_exists -v
```

## Unit tests (test_converters.py)

### Test classes:

#### 1. TestBaseConverter
Tests for the `BaseConverter` class:
- `test_converter_exists` - Check converter existence
- `test_create_markdown_header_level_*` - Create MD headers
- `test_escape_markdown` - Escape special characters

#### 2. TestPDFConverter
Tests for the `PDFConverter` class:
- `test_converter_exists` - Converter exists
- `test_converter_is_base_converter` - Inheritance
- `test_table_to_markdown_*` - Table conversion
- `test_convert_nonexistent_file` - Error handling

#### 3. TestDOCXConverter
Tests for the `DOCXConverter` class:
- `test_get_header_level_*` - Header levels
- `test_format_run_*` - Text formatting (bold, italic)
- `test_table_to_markdown` - Table conversion
- `test_convert_nonexistent_file` - Error handling

#### 4. TestImageConverter
Tests for the `ImageConverter` class:
- `test_get_mime_type_*` - MIME types for formats
- `test_convert_nonexistent_image` - Error handling

#### 5. TestUtilsFunctions
Tests for functions in `utils.py`:
- `test_is_supported_*` - Format support check
- `test_is_not_supported_*` - Unsupported formats

## Integration tests (test_integration.py)

### Test classes:

#### 1. TestDocumentConverter
Tests for the main `DocumentConverter` class:
- `test_converter_initialization` - Initialization
- `test_converter_has_supported_formats` - Supported formats
- `test_pdf_in_supported_formats` - PDF supported
- `test_*_in_supported_formats` - Other formats

#### 2. TestUtilsIntegration
Integration tests for utils:
- `test_get_supported_extensions` - Extension list
- `test_is_supported_case_insensitive` - Case-insensitivity
- `test_ensure_output_dir` - Directory creation
- `test_format_file_size` - File size formatting
- `test_get_supported_files_*` - File filtering

#### 3. TestConverterIntegration
Converter integration tests:
- `test_all_converters_exist` - Import converters
- `test_converters_are_subclasses_of_base` - Inheritance
- `test_converters_have_convert_method` - Convert methods

#### 4. TestConfigurationModule
Tests for `config.py`:
- `test_config_import` - Module import
- `test_config_default/fast/full` - Different configurations

## Test cases

### PDF Converter

| Test | Purpose |
|------|---------|
| `test_converter_exists` | ✓ Converter exists |
| `test_table_to_markdown_basic` | ✓ Simple table conversion |
| `test_table_to_markdown_with_none_values` | ✓ Support None in tables |
| `test_table_to_markdown_empty_table` | ✓ Empty tables |
| `test_table_to_markdown_single_row` | ✓ Single-row table |
| `test_convert_nonexistent_file` | ✓ Nonexistent files |

### DOCX Converter

| Test | Purpose |
|------|---------|
| `test_converter_exists` | ✓ Converter exists |
| `test_get_header_level_*` | ✓ Header levels (1-6) |
| `test_format_run_*` | ✓ Formatting (bold, italic, etc.) |
| `test_table_to_markdown` | ✓ DOCX table conversion |
| `test_convert_nonexistent_file` | ✓ Error handling |

### Image Converter

| Test | Purpose |
|------|---------|
| `test_converter_exists` | ✓ Converter exists |
| `test_get_mime_type_*` | ✓ MIME types for formats |
| `test_convert_nonexistent_image` | ✓ Error handling |

## Code coverage

### Generate coverage report

```bash
# Installation (if needed)
pip install pytest-cov

# Generate HTML report
pytest --cov=converters --cov=main --cov=utils --cov-report=html

# Report will be in: htmlcov/index.html
```

### Expected coverage

- **converters/**: >90%
- **main.py**: >85%
- **utils.py**: >85%
- **config.py**: >80%

## Mocking and Fixtures

Tests use `unittest.mock` for mocking:
- `docx.text.paragraph.CT_P` objects
- Document tables and cells
- OCR configuration

## Running examples

### Quick tests

```bash
# Only critical tests
python -m unittest tests.test_converters -v
```

### Full test with report

```bash
# All tests with coverage
pytest --cov=converters --cov=main --cov=utils \
       --cov-report=html --cov-report=term -v
```

### Monitor changes

```bash
# Run tests after every change (requires pytest-watch)
pip install pytest-watch
ptw
```

## Troubleshooting

### ImportError: No module named 'converters'

**Solution:**
```bash
# Run from main directory
cd /path/to/python-transform
python run_tests.py
```

### Test timeout

**Solution:**
```bash
# Increase timeout
pytest --timeout=300
```

### pytest issues

**Solution:**
```bash
# Use unittest instead of pytest
python -m unittest discover -s tests
```

## Best Practices

1. **Test isolation** - Each test is independent
2. **Cleanup** - `tearDown()` cleans resources
3. **Descriptive names** - Names describe what test checks
4. **Docstrings** - Each test has description
5. **Mocking** - Mock external dependencies
6. **Fixtures** - Reusable test data in `setUp()`

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

## Adding new tests

### Template

```python
class TestNewFeature(unittest.TestCase):
    """Tests for new feature."""
    
    def setUp(self):
        """Preparation."""
        pass
    
    def test_basic_functionality(self):
        """Test functionality."""
        result = some_function()
        self.assertIsNotNone(result)
    
    def test_error_handling(self):
        """Test error handling."""
        with self.assertRaises(ExpectedException):
            some_function(invalid_input)
    
    def tearDown(self):
        """Cleanup."""
        pass
```

## Test statistics

```
Unit Tests:       25+
Integration Tests: 20+
Total:            45+
Functions Tested: >90%
```

---

**Last Updated:** 2024-04-07
**Status:** Complete ✓
