# Quick Start

Quick start guide for python-transform.

## 1. Installation (2 minutes)

### System requirements
- Python 3.8 or newer
- pip (Python package manager)

### Installation procedure

```bash
# Clone the repository
git clone https://github.com/yourusername/python-transform.git
cd python-transform

# Install dependencies
pip install -r requirements.txt
```

## 2. Basic Usage (1 minute)

### Convert a single PDF

```bash
python main.py my_document.pdf
```

File will be converted to `./output/my_document.md`

### Convert entire directory

```bash
python main.py ./my_documents -d
```

## 3. Examples (5 minutes)

### Example 1: PDF

```bash
# Convert PDF file
python main.py report.pdf -o ./markdown_output
```

**Output: `./markdown_output/report.md`**

```markdown
# PDF Document
**Number of pages:** 3

## Page 1

Text content from page 1...

### Table 1
| Column 1 | Column 2 |
|-----------|-----------|
| Data 1    | Data 2    |
```

### Example 2: Word document

```bash
python main.py instructions.docx -o ./docs
```

**Output: `./docs/instructions.md`**

```markdown
# Instructions

## Chapter 1

Content with formatting...

**Bold text** and *italics*
```

### Example 3: Images

```bash
# Convert all images with metadata
python main.py ./photos -d -o ./images_md
```

### Example 4: Images with text extraction (OCR)

```bash
# Requires Tesseract-OCR
python main.py ./scanned -d --ocr -o ./text
```

## 4. Supported formats

| Format | Extension |
|--------|------------|
| PDF | `.pdf` |
| Word | `.docx` |
| Images | `.png`, `.jpg`, `.bmp`, `.gif` |

## 5. Set up Tesseract OCR (Optional)

### Windows

1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install
3. In Python:

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

## 6. Advanced usage

### Recursive conversion

```bash
python main.py ./project -d -r -o ./project_markdown
```

Converts all supported files recursively from all subdirectories.

### Custom output directory

```bash
python main.py document.pdf -o /my/path/output
```

### Combination of options

```bash
# Directory, recursive, with OCR, to custom output
python main.py ./documents -d -r --ocr -o ./result
```

## 7. Troubleshooting

### Problem: "No module named 'docx'"

```bash
pip install python-docx
```

### Problem: Tesseract not found

Windows:
- Download and install from: https://github.com/UB-Mannheim/tesseract/wiki
- Set path in code

Linux/Mac:
```bash
# Linux
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract
```

## 8. Next steps

- 📖 Read [README.md](README.md) to learn all available options
- 🔧 Check [examples.py](examples.py) for more examples
- 🐛 Report bugs on [GitHub Issues](https://github.com/yourusername/python-transform/issues)
- 🤝 Contribute! See [CONTRIBUTING.md](CONTRIBUTING.md)

## 9. Help

```bash
# Full documentation of options
python main.py -h

# Have questions? Open an issue!
```

---

Good luck with python-transform! 🚀
