"""
Konfiguracja dla skryptu konwersji.
"""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ConversionConfig:
    """Konfiguracja procesu konwersji."""
    
    # Directory settings
    input_dir: str = './documents'
    output_dir: str = './output'
    recursive: bool = False
    
    # PDF settings
    pdf_extract_tables: bool = True
    pdf_extract_images: bool = False
    
    # DOCX settings
    docx_preserve_formatting: bool = True
    docx_extract_tables: bool = True
    
    # Image settings
    image_include_metadata: bool = True
    image_use_ocr: bool = False
    image_ocr_language: str = 'pol+eng'  # Polish + English
    
    # OCR settings (Tesseract)
    tesseract_cmd: Optional[str] = None  # e.g., r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # Output settings
    markdown_include_toc: bool = False  # Table of contents
    markdown_include_metadata: bool = True
    markdown_use_html_comments: bool = True
    
    # File filtering
    supported_formats: List[str] = None
    
    def __post_init__(self):
        if self.supported_formats is None:
            self.supported_formats = [
                'pdf', 'docx', 'doc',
                'png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff', 'webp'
            ]


# Domyślna konfiguracja
DEFAULT_CONFIG = ConversionConfig()


# Konfiguracja dla szybkiej konwersji
FAST_CONFIG = ConversionConfig(
    pdf_extract_images=False,
    image_use_ocr=False,
    markdown_use_html_comments=False,
)


# Konfiguracja dla pełnej konwersji z OCR
FULL_CONFIG = ConversionConfig(
    pdf_extract_images=True,
    image_use_ocr=True,
    markdown_include_toc=True,
    markdown_include_metadata=True,
)


def get_config(config_name: str = 'default') -> ConversionConfig:
    """
    Pobierz konfigurację na podstawie nazwy.
    
    Args:
        config_name: Nazwa konfiguracji ('default', 'fast', 'full')
        
    Returns:
        Obiekt ConversionConfig
    """
    configs = {
        'default': DEFAULT_CONFIG,
        'fast': FAST_CONFIG,
        'full': FULL_CONFIG,
    }
    
    return configs.get(config_name, DEFAULT_CONFIG)
