#!/usr/bin/env python3
"""
Document and Image to Markdown Converter

Converts documents (PDF, DOCX) and images (PNG, JPG, etc.) to Markdown files.
"""

import os
import sys
from pathlib import Path
from typing import Optional, List
import argparse
import logging

# Import specific converters
from converters.pdf_converter import PDFConverter
from converters.docx_converter import DOCXConverter
from converters.image_converter import ImageConverter
from converters.base_converter import BaseConverter

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DocumentConverter:
    """
    Main class for converting documents and images to Markdown.
    """
    
    # Map file types to converters
    CONVERTERS = {
        '.pdf': PDFConverter,
        '.docx': DOCXConverter,
        '.doc': DOCXConverter,
        '.png': ImageConverter,
        '.jpg': ImageConverter,
        '.jpeg': ImageConverter,
        '.bmp': ImageConverter,
        '.gif': ImageConverter,
        '.tiff': ImageConverter,
        '.webp': ImageConverter,
    }
    
    def __init__(self, output_dir: str = './output'):
        """
        Initialize the converter.
        
        Args:
            output_dir: Output directory for Markdown files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {self.output_dir}")
    
    def convert_file(self, input_path: str, use_ocr: bool = False) -> Optional[Path]:
        """
        Convert a single file to Markdown.
        
        Args:
            input_path: Path to the input file
            use_ocr: Whether to use OCR for images
            
        Returns:
            Path to the created Markdown file or None
        """
        input_file = Path(input_path)
        
        if not input_file.exists():
            logger.error(f"File does not exist: {input_path}")
            return None
        
        file_ext = input_file.suffix.lower()
        
        if file_ext not in self.CONVERTERS:
            logger.error(f"Unsupported file format: {file_ext}")
            return None
        
        converter_class = self.CONVERTERS[file_ext]
        converter: BaseConverter = converter_class()
        
        logger.info(f"Converting: {input_file.name}")
        
        try:
            output_path = self.output_dir / f"{input_file.stem}.md"
            
            if file_ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp']:
                markdown_content = converter.convert(input_path, use_ocr=use_ocr)
            else:
                markdown_content = converter.convert(input_path)
            
            if markdown_content:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                logger.info(f"✓ File created: {output_path}")
                return output_path
            else:
                logger.error(f"Failed to convert: {input_path}")
                return None
                
        except Exception as e:
            logger.error(f"Conversion error: {e}")
            return None
    
    def convert_directory(self, input_dir: str, recursive: bool = False, use_ocr: bool = False) -> List[Path]:
        """
        Convert all supported files in a directory.
        
        Args:
            input_dir: Input directory
            recursive: Whether to search recursively in subdirectories
            use_ocr: Whether to use OCR for images
            
        Returns:
            List of paths to created Markdown files
        """
        input_path = Path(input_dir)
        
        if not input_path.exists():
            logger.error(f"Directory does not exist: {input_dir}")
            return []
        
        logger.info(f"Searching for files in: {input_dir}")
        
        results = []
        
        # Search for files
        if recursive:
            pattern = '**/*'
        else:
            pattern = '*'
        
        for file_path in input_path.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower() in self.CONVERTERS:
                result = self.convert_file(str(file_path), use_ocr=use_ocr)
                if result:
                    results.append(result)
        
        logger.info(f"Converted {len(results)} files")
        return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Convert documents and images to Markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  # Convert a single file
  python main.py input.pdf
  
  # Convert to a different output directory
  python main.py input.pdf -o ./markdown_files
  
  # Convert entire directory
  python main.py ./documents -d
  
  # Recursively convert with OCR for images
  python main.py ./files -d -r --ocr
        """
    )
    
    parser.add_argument('input', help='File or directory to convert')
    parser.add_argument('-o', '--output', default='./output', 
                        help='Output directory (default: ./output)')
    parser.add_argument('-d', '--directory', action='store_true',
                        help='Directory mode - convert all files in directory')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Search recursively in subdirectories')
    parser.add_argument('--ocr', action='store_true',
                        help='Use OCR for images (requires pytesseract and Tesseract-OCR)')
    
    args = parser.parse_args()
    
    converter = DocumentConverter(output_dir=args.output)
    
    try:
        if args.directory:
            converter.convert_directory(
                args.input, 
                recursive=args.recursive,
                use_ocr=args.ocr
            )
        else:
            converter.convert_file(args.input, use_ocr=args.ocr)
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
