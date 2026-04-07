"""
Image converter (PNG, JPG, etc.) to Markdown with optional OCR.
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
    """Convert image files to Markdown."""
    
    def convert(self, file_path: str, use_ocr: bool = False, **kwargs) -> Optional[str]:
        """
        Convert image to Markdown.
        
        Args:
            file_path: Path to the image file
            use_ocr: Whether to perform OCR on the image
            
        Returns:
            Markdown content
        """
        try:
            path = Path(file_path)
            
            # Check if file exists
            if not path.exists():
                logger.error(f"File does not exist: {file_path}")
                return None
            
            markdown_content = []
            
            # Header
            markdown_content.append(f"# {path.stem}\n\n")
            
            # Add image
            markdown_content.append(f"![{path.stem}]({file_path})\n\n")
            
            # Image properties
            try:
                img = Image.open(file_path)
                markdown_content.append("## Image Properties\n\n")
                markdown_content.append(f"- **Format:** {img.format}\n")
                markdown_content.append(f"- **Dimensions:** {img.width} x {img.height} px\n")
                markdown_content.append(f"- **Color mode:** {img.mode}\n")
                markdown_content.append(f"- **File size:** {path.stat().st_size / 1024:.2f} KB\n\n")
            except Exception as e:
                logger.warning(f"Cannot read image properties: {e}")
            
            # OCR - extract text from image
            if use_ocr:
                markdown_content.append("## Text from image (OCR)\n\n")
                try:
                    text = self._extract_text_ocr(file_path)
                    if text.strip():
                        markdown_content.append(f"```\n{text}\n```\n\n")
                    else:
                        markdown_content.append("*No text found in image*\n\n")
                except Exception as e:
                    logger.warning(f"OCR error: {e}\nMake sure you have Tesseract-OCR installed")
                    markdown_content.append(f"*OCR not available: {e}*\n\n")
            
            # Base64 encoded version (optional)
            # markdown_content.append(self._create_embedded_image(file_path))
            
            return ''.join(markdown_content)
            
        except Exception as e:
            logger.error(f"Image conversion error: {e}")
            return None
    
    def _extract_text_ocr(self, file_path: str) -> str:
        """Extract text from image using OCR."""
        try:
            img = Image.open(file_path)
            
            # Optimize image for OCR
            # Convert to grayscale
            if img.mode != 'L':
                img = img.convert('L')
            
            # Enlarge image for better results (if it's small)
            if img.width < 400 or img.height < 400:
                scale = max(400 / img.width, 400 / img.height)
                new_size = (int(img.width * scale), int(img.height * scale))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Extract text
            text = pytesseract.image_to_string(img, lang='pol+eng')
            return text
            
        except Exception as e:
            logger.error(f"OCR error: {e}")
            raise
    
    def _create_embedded_image(self, file_path: str) -> str:
        """Create base64-encoded image (embedded directly in Markdown)."""
        try:
            with open(file_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            ext = Path(file_path).suffix.lower()
            mime_type = self._get_mime_type(ext)
            
            return f"![Embedded Image](data:{mime_type};base64,{image_data})\n\n"
        except Exception as e:
            logger.warning(f"Cannot embed image: {e}")
            return ""
    
    def _get_mime_type(self, extension: str) -> str:
        """Return MIME type for file extension."""
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
