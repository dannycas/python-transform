"""
PDF to Markdown converter.
"""

import logging
from typing import Optional
import pdfplumber
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract

from .base_converter import BaseConverter

logger = logging.getLogger(__name__)


class PDFConverter(BaseConverter):
    """Convert PDF files to Markdown."""
    
    def convert(self, file_path: str, use_ocr: bool = False, **kwargs) -> Optional[str]:
        """
        Convert PDF to Markdown.
        
        Args:
            file_path: Path to the PDF file
            use_ocr: Whether to use OCR for image-based PDFs
            
        Returns:
            Markdown content
        """
        try:
            markdown_content = []
            
            with pdfplumber.open(file_path) as pdf:
                logger.info(f"Processing PDF with {len(pdf.pages)} pages")
                
                # Add document information
                markdown_content.append(f"# PDF Document\n")
                markdown_content.append(f"**Number of pages:** {len(pdf.pages)}\n\n")
                
                # Process each page
                for page_num, page in enumerate(pdf.pages, 1):
                    # Page header
                    markdown_content.append(f"## Page {page_num}\n\n")
                    
                    # Text extraction with improved parameters
                    text = page.extract_text(x_tolerance=3, y_tolerance=3)
                    if not text:
                        # Try alternative extraction methods
                        text = page.extract_text(layout=True)
                    
                    if not text:
                        # Try fallback with PyPDF2
                        text = self._extract_text_fallback(file_path, page_num)
                    
                    if not text and use_ocr:
                        # Try OCR for image-based PDFs
                        text = self._extract_text_ocr(page)
                    
                    if text and text.strip():
                        # Clean up the text
                        cleaned_text = text.strip()
                        logger.info(f"Extracted {len(cleaned_text)} characters from page {page_num}")
                        markdown_content.append(cleaned_text)
                        markdown_content.append("\n\n")
                    else:
                        if use_ocr:
                            logger.warning(f"No text extracted from page {page_num} even with OCR")
                            markdown_content.append("*No text content found on this page, even with OCR. The page may be blank or contain only images/ graphics.*\n\n")
                        else:
                            logger.warning(f"No text extracted from page {page_num}")
                            markdown_content.append("*No text content found on this page. The PDF may be image-based or use an unsupported font encoding. Try using --ocr flag for OCR extraction.*\n\n")
                    
                    # Table extraction
                    tables = page.extract_tables()
                    if tables:
                        logger.info(f"Found {len(tables)} tables on page {page_num}")
                        for table_num, table in enumerate(tables, 1):
                            markdown_content.append(f"### Table {table_num}\n\n")
                            markdown_content.append(self._table_to_markdown(table))
                            markdown_content.append("\n\n")
            
            return ''.join(markdown_content)
            
        except Exception as e:
            logger.error(f"PDF conversion error: {e}")
            return None
    
    def _extract_text_fallback(self, file_path: str, page_num: int) -> Optional[str]:
        """Fallback text extraction using PyPDF2."""
        try:
            reader = PdfReader(file_path)
            if page_num <= len(reader.pages):
                page = reader.pages[page_num - 1]  # PyPDF2 uses 0-based indexing
                text = page.extract_text()
                return text.strip() if text else None
        except Exception as e:
            logger.debug(f"PyPDF2 extraction failed for page {page_num}: {e}")
            return None
    
    def _extract_text_ocr(self, page) -> Optional[str]:
        """Extract text from PDF page using OCR."""
        try:
            # Convert PDF page to image
            img = page.to_image(resolution=300).original  # High resolution for better OCR
            
            # Optimize image for OCR (similar to image converter)
            if img.mode != 'L':
                img = img.convert('L')
            
            # Extract text using OCR
            text = pytesseract.image_to_string(img, lang='pol+eng')
            return text.strip() if text else None
            
        except Exception as e:
            logger.error(f"OCR extraction failed: {e}")
            return None
    
    def _table_to_markdown(self, table: list) -> str:
        """Convert table to Markdown format."""
        if not table or not table[0]:
            return ""
        
        lines = []
        
        for row_idx, row in enumerate(table):
            # Convert None to empty string
            row_cells = [str(cell) if cell is not None else "" for cell in row]
            lines.append("| " + " | ".join(row_cells) + " |")
            
            # Add separator after header (first row)
            if row_idx == 0:
                separator = "|" + "|".join(["---"] * len(row)) + "|"
                lines.append(separator)
        
        return "\n".join(lines)
