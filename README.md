# Document & Image to Markdown Converter

Script for converting documents (PDF, DOCX) and images (PNG, JPG, etc.) to Markdown files.

## Features

- ✅ **PDF Conversion** - Extract text and tables from PDF files
- ✅ **DOCX Conversion** - Support for formatting, headers, tables
- ✅ **Image Conversion** - PNG, JPG, BMP, GIF, TIFF, WebP
- ✅ **OCR for images** - Optional text extraction from images
- ✅ **Batch Conversion** - Process entire directories
- ✅ **Recursive Conversion** - Support for subdirectories

## Requirements

- Python 3.8+
- Python Libraries (see `requirements.txt`)
- (Optional) Tesseract-OCR for image OCR functionality

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/python-transform.git
cd python-transform
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Install Tesseract-OCR

#### Windows

Download installer from: https://github.com/UB-Mannheim/tesseract/wiki

```bash
# After installation, set environment variable in code or Python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-pol  # For Polish
```

#### macOS

```bash
brew install tesseract
brew install tesseract-lang  # For additional languages
```

## 🧪 Tests

The project contains a comprehensive test suite:

```bash
# Run all tests (69 tests)
python run_tests.py

# Unit tests only
python run_tests.py -u

# Integration tests only
python run_tests.py -i

# With code coverage
pytest --cov=converters --cov=main --cov=utils --cov-report=html
```

**Test Statistics:**
- 📊 69 tests (44 unit + 25 integration)
- 📈 ~91% code coverage
- ✅ All formats supported

More in [TESTING.md](TESTING.md) and [TESTS_QUICK_REFERENCE.md](TESTS_QUICK_REFERENCE.md)

## Usage

### Convert a single file

```bash
python main.py input.pdf
```

Markdown file will be created in the `./output/` directory

### Convert with specific output directory

```bash
python main.py input.pdf -o ./moje_markdown_pliki
```

### Convert entire directory

```bash
python main.py ./documents -d
```

Convert all supported files in the directory `./documents`

### Recursive conversion (with subdirectories)

```bash
python main.py ./documents -d -r
```

### Conversion with OCR for images

```bash
python main.py ./images -d --ocr
```

Extract text from images (requires Tesseract-OCR)

### Full help

```bash
python main.py -h
```

## Supported formats

| Format | Extension | Support |
|--------|-------------|---------|
| PDF | `.pdf` | ✅ Text, tables |
| Word | `.docx`, `.doc` | ✅ Text, formatting, tables |
| PNG | `.png` | ✅ Metadata, OCR |
| JPEG | `.jpg`, `.jpeg` | ✅ Metadata, OCR |
| BMP | `.bmp` | ✅ Metadata, OCR |
| GIF | `.gif` | ✅ Metadata, OCR |
| TIFF | `.tiff` | ✅ Metadata, OCR |
| WebP | `.webp` | ✅ Metadata, OCR |

## Examples

### Example 1: Convert PDF report

```bash
python main.py report_2024.pdf -o ./reports_markdown
```

Result: `./reports_markdown/report_2024.md`

### Example 2: Convert Word document with formatting

```bash
python main.py instructions.docx -o ./docs
```

Result: Markdown with preserved formatting (headers, tables, etc.)

### Example 3: Extract text from multiple images

```bash
python main.py ./scanned_documents -d -r --ocr -o ./text_from_scans
```

Converts all images in directory recursively, extract text via OCR

### Example 4: Convert entire project

```bash
python main.py ./project -d -r -o ./project_markdown
```

Converts all supported files in entire project

## Project structure

```
python-transform/
├── main.py                 # Main script
├── requirements.txt        # Python dependencies
├── README.md              # Documentation (this file)
├── converters/
│   ├── __init__.py
│   ├── base_converter.py  # Base class
│   ├── pdf_converter.py   # PDF converter
│   ├── docx_converter.py  # DOCX converter
│   └── image_converter.py # Image converter
└── output/                # Default output directory
```

## Converter parameters

### General

- `input` - File or directory to convert (required)
- `-o, --output` - Output directory (default: `./output`)
- `-d, --directory` - Directory mode
- `-r, --recursive` - Search recursively

### Specific for images

- `--ocr` - Use OCR to extract text from images

## Notes and tips

### OCR

- OCR requires additional processing time
- For better OCR results, ensure images have good quality text
- Supported languages: English (default), Polish (if installed)

### Performance

- Converting large PDF files may take longer
- For large image collections, use recursive conversion

### Limits

- Very large PDFs (>100MB) may require more RAM
- Low quality images may give poor OCR results

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'docx'"

**Solution:**
```bash
pip install python-docx
```

### Problem: "Tesseract is not installed or it's not in your PATH"

**Solution for Windows:**
1. Download and install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
2. Set the path in the code:
```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Problem: "No module named 'converters'"

**Solution:**
```bash
# Run from the main project directory
python main.py input.pdf
```

## Extending

To add support for a new format:

1. Create a new converter inheriting from `BaseConverter`:

```python
# converters/csv_converter.py
from .base_converter import BaseConverter

class CSVConverter(BaseConverter):
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        # Conversion implementation
        pass
```

2. Add to `main.py`:

```python
from converters.csv_converter import CSVConverter

CONVERTERS = {
    # ...
    '.csv': CSVConverter,
}
```

## License

MIT

## Author

Python Transform Project

## Contact and Support

To report bugs or suggest features, create an issue in the repository.
