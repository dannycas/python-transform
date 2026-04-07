# Tests Directory

Directory containing all tests for the python-transform project.

## Structure

```
tests/
├── __init__.py                  # Package marker
├── test_converters.py           # Unit tests (44 tests)
├── test_integration.py          # Integration tests (25 tests)
└── README.md                    # This file
```

## Quick Start

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

**Tested components:**
- BaseConverter (base class)
- PDFConverter (PDF conversion)
- DOCXConverter (DOCX conversion)
- ImageConverter (image conversion)
- Utils functions (helper functions)

**Main test categories:**
1. Existence checks (whether components exist)
2. Functionality tests (whether they work as expected)
3. Error handling (error handling)
4. Edge cases (boundary conditions)

### test_integration.py (25 Integration Tests)

**Tested systems:**
- DocumentConverter (main class)
- Utils module (utilities)
- Configuration (configuration)
- Converter integration (converter integration)

**Main test categories:**
1. System initialization (initialization)
2. Format support (format support)
3. File operations (file operations)
4. Configuration management (configuration management)

## Test Coverage

| Module | Coverage |
|--------|----------|
| converters/ | ~92% |
| main.py | ~85% |
| utils.py | ~90% |
| config.py | ~95% |
| **Average** | **~91%** |

## Requirements

- Python 3.8+
- Libraries from requirements.txt
- (Optional) pytest and pytest-cov

```bash
# Install test dependencies
pip install -r requirements-dev.txt
```

## Running

### Method 1: run_tests.py (RECOMMENDED)
```bash
python run_tests.py              # All tests
python run_tests.py -u           # Unit tests
python run_tests.py -i           # Integration tests
python run_tests.py -t TEST_NAME # Specific test
```

### Method 2: unittest
```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m unittest tests.test_converters -v
python -m unittest tests.test_converters.TestPDFConverter -v
```

### Method 3: pytest
```bash
pytest
pytest tests/test_converters.py -v
pytest --cov=converters --cov=main --cov=utils --cov-report=html
```

## Documentation

- [TESTING.md](../TESTING.md) - Full test documentation
- [TEST_SUMMARY.md](../TEST_SUMMARY.md) - Detailed summary
- [TESTS_QUICK_REFERENCE.md](../TESTS_QUICK_REFERENCE.md) - Quick reference

## Notes

### Working tests
- All unit tests pass
- Integration tests cover the entire system
- Mocking is used for external dependencies (Tesseract-OCR)

### Limitations
- OCR tests are mocked (requires Tesseract-OCR on system)
- Actual PDF/DOCX files are not tested (would be too large)
- Tests work without Tesseract installed

## Troubleshooting

### ImportError: No module named 'converters'
**Solution:**
```bash
cd /path/to/python-transform
python run_tests.py
```

### Tests not found
**Solution:**
```bash
# Make sure you're in the main directory
pwd  # Should show ...python-transform
python -m unittest discover -s tests -p "test_*.py" -v
```

### pytest not found
**Solution:**
```bash
pip install pytest
pytest
```

## Contributing

Adding new tests:

1. Create test in appropriate file
   - Unit tests → `test_converters.py`
   - Integration tests → `test_integration.py`

2. Follow naming convention
   ```python
   def test_descriptive_name(self):
       """Description of what test checks."""
   ```

3. Include docstring

4. Run tests
   ```bash
   python run_tests.py
   ```

5. Commit with changed coverage

## Status

✅ **69 tests**
✅ **~91% code coverage**
✅ **Ready for CI/CD**
