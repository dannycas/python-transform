#!/usr/bin/env python3
"""
Document and Image to Markdown Converter

Konwertuje dokumenty (PDF, DOCX) i obrazy (PNG, JPG, itd.) na pliki Markdown.
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
    Główna klasa do konwersji dokumentów i obrazów na Markdown.
    """
    
    # Mapowanie typów plików na konwertery
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
        Inicjalizacja konwertera.
        
        Args:
            output_dir: Katalog wyjściowy dla plików Markdown
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {self.output_dir}")
    
    def convert_file(self, input_path: str, use_ocr: bool = False) -> Optional[Path]:
        """
        Konwertuje pojedynczy plik na Markdown.
        
        Args:
            input_path: Ścieżka do pliku wejściowego
            use_ocr: Czy używać OCR dla obrazów
            
        Returns:
            Ścieżka do stworzonego pliku Markdown lub None
        """
        input_file = Path(input_path)
        
        if not input_file.exists():
            logger.error(f"Plik nie istnieje: {input_path}")
            return None
        
        file_ext = input_file.suffix.lower()
        
        if file_ext not in self.CONVERTERS:
            logger.error(f"Nieobsługiwany format pliku: {file_ext}")
            return None
        
        converter_class = self.CONVERTERS[file_ext]
        converter: BaseConverter = converter_class()
        
        logger.info(f"Konwertowanie: {input_file.name}")
        
        try:
            output_path = self.output_dir / f"{input_file.stem}.md"
            
            if file_ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp']:
                markdown_content = converter.convert(input_path, use_ocr=use_ocr)
            else:
                markdown_content = converter.convert(input_path)
            
            if markdown_content:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                logger.info(f"✓ Plik utworzony: {output_path}")
                return output_path
            else:
                logger.error(f"Nie udało się konwertować: {input_path}")
                return None
                
        except Exception as e:
            logger.error(f"Błąd konwersji: {e}")
            return None
    
    def convert_directory(self, input_dir: str, recursive: bool = False, use_ocr: bool = False) -> List[Path]:
        """
        Konwertuje wszystkie obsługiwane pliki w katalogu.
        
        Args:
            input_dir: Katalog wejściowy
            recursive: Czy szukać rekursywnie w podkatalogach
            use_ocr: Czy używać OCR dla obrazów
            
        Returns:
            Lista ścieżek do stworzonych plików Markdown
        """
        input_path = Path(input_dir)
        
        if not input_path.exists():
            logger.error(f"Katalog nie istnieje: {input_dir}")
            return []
        
        logger.info(f"Szukanie plików w: {input_dir}")
        
        results = []
        
        # Szukanie plików
        if recursive:
            pattern = '**/*'
        else:
            pattern = '*'
        
        for file_path in input_path.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower() in self.CONVERTERS:
                result = self.convert_file(str(file_path), use_ocr=use_ocr)
                if result:
                    results.append(result)
        
        logger.info(f"Skonwertowano {len(results)} plików")
        return results


def main():
    """Główna funkcja."""
    parser = argparse.ArgumentParser(
        description='Konwertuje dokumenty i obrazy na pliki Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Przykłady użycia:
  # Konwersja pojedynczego pliku
  python main.py input.pdf
  
  # Konwersja z zapisem w innym katalogu
  python main.py input.pdf -o ./markdown_files
  
  # Konwersja całego katalogu
  python main.py ./documents -d
  
  # Konwersja rekursywnie z OCR dla obrazów
  python main.py ./files -d -r --ocr
        """
    )
    
    parser.add_argument('input', help='Plik lub katalog do konwersji')
    parser.add_argument('-o', '--output', default='./output', 
                        help='Katalog wyjściowy (domyślnie: ./output)')
    parser.add_argument('-d', '--directory', action='store_true',
                        help='Tryb katalogowy - konwertuj wszystkie pliki w katalogu')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Szukaj rekursywnie w podkatalogach')
    parser.add_argument('--ocr', action='store_true',
                        help='Używaj OCR dla obrazów (wymaga pytesseract i Tesseract-OCR)')
    
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
        logger.warning("Przerwano przez użytkownika")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Błąd: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
