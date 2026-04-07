# Project Structure - python-transform

## 📁 Directory Structure

```
python-transform/
│
├── 📄 main.py                    # Main conversion script
├── 📄 config.py                  # Project configuration
├── 📄 utils.py                   # Utility functions
├── 📄 examples.py                # Usage examples
│
├── 📁 converters/                # Converters module
│   ├── __init__.py
│   ├── base_converter.py        # Base class
│   ├── pdf_converter.py         # PDF converter
│   ├── docx_converter.py        # DOCX converter
│   └── image_converter.py       # Image converter
│
├── 📁 tests/                     # Tests
│   ├── __init__.py
│   └── test_converters.py       # Converter tests
│
├── 📁 output/                    # Default output directory for markdowns (generated)
│
├── 📄 requirements.txt           # Python dependencies
├── 📄 setup.py                   # Setup for package installation
│
├── 📖 README.md                  # Main documentation
├── 📖 QUICKSTART.md             # Quick start
├── 📖 CONTRIBUTING.md           # Contributor guide
├── 📖 CHANGELOG.md              # Changelog
├── 📄 LICENSE                   # MIT License
└── 📄 .gitignore                # Git ignore rules
```

## 🚀 Quick Start (3 steps)

### 1. Installation
```bash
cd python-transform
pip install -r requirements.txt
```

### 2. Conversion
```bash
# Single file
python main.py document.pdf

# Directory
python main.py ./documents -d

# With OCR
python main.py ./images -d --ocr
```

### 3. Output
```
./output/
├── document.md
├── other_documents.md
└── ...
```

## 📋 Supported formats

| Format | Extension | Support |
|--------|------------|---------|
| PDF | .pdf | ✅ Text, tables |
| Word | .docx | ✅ Text, formatting |
| Images | .png, .jpg | ✅ + OCR optionally |

## 🔧 Command-line options

```bash
python main.py -h

Positional arguments:
  input                File or directory to convert

Optional arguments:
  -o, --output OUT     Output directory (default: ./output)
  -d, --directory      Directory mode
  -r, --recursive      Search recursively
  --ocr                Use OCR for images
```

## 📦 Key components

### main.py
Main `DocumentConverter` class handling:
- File conversion
- Directory conversion
- File type to converter mapping
- Error handling and logging

### converters/
- **base_converter.py** - Abstract base class
- **pdf_converter.py** - Text and table extraction from PDF
- **docx_converter.py** - Conversion with formatting preservation
- **image_converter.py** - Image conversion with optional OCR

### utils.py
Helper functions:
- `is_supported()` - Format support check
- `get_supported_files()` - List supported files
- `format_file_size()` - File size formatting
- `print_conversion_summary()` - Summary output

## 🎯 Usage examples

### Convert PDF report
```bash
python main.py report_Q1_2024.pdf -o ./reports_md
```
Output: `./reports_md/report_Q1_2024.md`

### Convert entire project
```bash
python main.py ./project -d -r -o ./project_markdown
```
Converts all files recursively

### Extract text from scans
```bash
python main.py ./scanned_documents -d --ocr -o ./text
```
Requires: Tesseract-OCR

## 🧪 Tests

```bash
# Run tests
python -m pytest tests/

# Other commands
python -m pytest tests/test_converters.py -v
python -m pytest tests/test_converters.py::TestPDFConverter -v
```

## 📝 Configuration (config.py)

```python
from config import get_config

# Pre-built configurations
config = get_config('default')   # Default
config = get_config('fast')      # Fast
config = get_config('full')      # Full with OCR
```

## 🔗 Dependencies

- `PyPDF2` 3.0.1 - PDF processing
- `pdfplumber` 0.9.0 - Table extraction
- `python-docx` 0.8.11 - DOCX processing
- `Pillow` 11.0.0+ - Image processing
- `pytesseract` 0.3.10 - OCR
- `markdown` 3.5.0 - Markdown support

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt --upgrade
```

### OCR not working
- Install Tesseract-OCR
- Set path in code

### Out of Memory
- Convert smaller batches
- Reduce image sizes

## 📚 Documentation

- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start
- [examples.py](examples.py) - Code examples
- [CONTRIBUTING.md](CONTRIBUTING.md) - For developers

## 🚢 Deployment

### As script
```bash
python main.py input.pdf
```

### As module
```bash
pip install -e .
python-transform input.pdf
```

### Setup.py
```bash
python setup.py install
```

## 📝 License

MIT - See [LICENSE](LICENSE)

## 🤝 Contribution

Interested in contributing? Read [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Last Updated:** 2024-04-07
**Status:** v0.1.0 (Alpha)
