"""
Konwerter obrazów (PNG, JPG, itd.) na Markdown z opcjonalnym OCR.
"""

import logging
import base64
from typing import Optional
from pathlib import Path
from PIL import Image
import pytesseract

from .base_converter import BaseConverter

logger = logging.getLogger(__name__)


class ImageConverter(BaseConverter):
    """Konwertuje pliki obrazów na Markdown."""
    
    def convert(self, file_path: str, use_ocr: bool = False, **kwargs) -> Optional[str]:
        """
        Konwertuje obraz na Markdown.
        
        Args:
            file_path: Ścieżka do pliku obrazu
            use_ocr: Czy wykonać OCR na obrazie
            
        Returns:
            Zawartość Markdown
        """
        try:
            path = Path(file_path)
            markdown_content = []
            
            # Nagłówek
            markdown_content.append(f"# {path.stem}\n\n")
            
            # Dodaj obraz
            markdown_content.append(f"![{path.stem}]({file_path})\n\n")
            
            # Informacje o pliku
            try:
                img = Image.open(file_path)
                markdown_content.append("## Właściwości obrazu\n\n")
                markdown_content.append(f"- **Format:** {img.format}\n")
                markdown_content.append(f"- **Wymiary:** {img.width} x {img.height} px\n")
                markdown_content.append(f"- **Tryb koloru:** {img.mode}\n")
                markdown_content.append(f"- **Rozmiar pliku:** {path.stat().st_size / 1024:.2f} KB\n\n")
            except Exception as e:
                logger.warning(f"Nie można odczytać właściwości obrazu: {e}")
            
            # OCR - ekstrakcja tekstu z obrazu
            if use_ocr:
                markdown_content.append("## Tekst z obrazu (OCR)\n\n")
                try:
                    text = self._extract_text_ocr(file_path)
                    if text.strip():
                        markdown_content.append(f"```\n{text}\n```\n\n")
                    else:
                        markdown_content.append("*Nie znaleziono tekstu w obrazie*\n\n")
                except Exception as e:
                    logger.warning(f"Błąd OCR: {e}\nUpewnij się, że masz zainstalowany Tesseract-OCR")
                    markdown_content.append(f"*OCR nie jest dostępne: {e}*\n\n")
            
            # Wersja zakodowana base64 (opcjonalnie)
            # markdown_content.append(self._create_embedded_image(file_path))
            
            return ''.join(markdown_content)
            
        except Exception as e:
            logger.error(f"Błąd konwersji obrazu: {e}")
            return None
    
    def _extract_text_ocr(self, file_path: str) -> str:
        """Ekstrakcja tekstu z obrazu przy użyciu OCR."""
        try:
            img = Image.open(file_path)
            
            # Optymalizuj obraz dla OCR
            # Konwertuj na skale szarości
            if img.mode != 'L':
                img = img.convert('L')
            
            # Powiększ obraz dla lepszych rezultatów (jeśli jest mały)
            if img.width < 400 or img.height < 400:
                scale = max(400 / img.width, 400 / img.height)
                new_size = (int(img.width * scale), int(img.height * scale))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Ekstrakcja tekstu
            text = pytesseract.image_to_string(img, lang='pol+eng')
            return text
            
        except Exception as e:
            logger.error(f"Błąd OCR: {e}")
            raise
    
    def _create_embedded_image(self, file_path: str) -> str:
        """Tworzy obraz zakodowany w base64 (osadzony bezpośrednio w Markdown)."""
        try:
            with open(file_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            ext = Path(file_path).suffix.lower()
            mime_type = self._get_mime_type(ext)
            
            return f"![Embedded Image](data:{mime_type};base64,{image_data})\n\n"
        except Exception as e:
            logger.warning(f"Nie można osadzić obrazu: {e}")
            return ""
    
    def _get_mime_type(self, extension: str) -> str:
        """Zwraca MIME type dla rozszerzenia pliku."""
        mime_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp',
            '.tiff': 'image/tiff',
        }
        return mime_types.get(extension, 'image/png')
