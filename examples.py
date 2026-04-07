"""
Example of how to use the document conversion script.
"""

from pathlib import Path
from main import DocumentConverter


def example_1_single_file():
    """Convert a single PDF file."""
    print("=" * 50)
    print("Example 1: Convert single PDF")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_file('example.pdf')


def example_2_single_docx():
    """Convert a single DOCX file."""
    print("=" * 50)
    print("Example 2: Convert single DOCX")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_file('example.docx')


def example_3_directory():
    """Convert all files in a directory."""
    print("=" * 50)
    print("Example 3: Convert entire directory")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_directory('./documents')


def example_4_recursive():
    """Recursive conversion (with subdirectories)."""
    print("=" * 50)
    print("Example 4: Recursive conversion")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_directory('./documents', recursive=True)


def example_5_images_with_ocr():
    """Convert images with OCR."""
    print("=" * 50)
    print("Example 5: Convert images with OCR")
    print("=" * 50)
    
    converter = DocumentConverter(output_dir='./output')
    # converter.convert_directory('./images', use_ocr=True)


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("Document & Image to Markdown Converter - Examples")
    print("=" * 50 + "\n")
    
    print("INSTRUCTIONS:")
    print("-" * 50)
    print()
    print("To run the examples:")
    print()
    print("1. Place files to convert in appropriate directories:")
    print("   - example.pdf, example.docx in main directory")
    print("   - Images in ./images/")
    print("   - Documents in ./documents/")
    print()
    print("2. Uncomment the appropriate example (uncomment the convert_ line)")
    print()
    print("3. Run the script:")
    print("   python examples.py")
    print()
    print("ALTERNATIVELY - Use command line directly:")
    print("-" * 50)
    print()
    print("# Single file:")
    print("python main.py example.pdf")
    print()
    print("# Directory:")
    print("python main.py ./documents -d")
    print()
    print("# Recursively:")
    print("python main.py ./documents -d -r")
    print()
    print("# With OCR:")
    print("python main.py ./images -d --ocr")
    print()
