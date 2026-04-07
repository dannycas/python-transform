"""
PDF to Markdown converter.
"""

import logging
from typing import Optional
import pdfplumber

from .base_converter import BaseConverter

logger = logging.getLogger(__name__)


class PDFConverter(BaseConverter):
    """Convert PDF files to Markdown."""
    
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        """
        Convert PDF to Markdown.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            Markdown content
        """
        try:
            markdown_content = []
            
            with pdfplumber.open(file_path) as pdf:
                # Add document information
                markdown_content.append(f"# PDF Document\n")
                markdown_content.append(f"**Number of pages:** {len(pdf.pages)}\n\n")
                
                # Process each page
                for page_num, page in enumerate(pdf.pages, 1):
                    # Page header
                    markdown_content.append(f"## Page {page_num}\n\n")
                    
                    # Text extraction
                    text = page.extract_text()
                    if text:
                        markdown_content.append(text)
                        markdown_content.append("\n\n")
                    
                    # Table extraction
                    tables = page.extract_tables()
                    if tables:
                        for table_num, table in enumerate(tables, 1):
                            markdown_content.append(f"### Table {table_num}\n\n")
                            markdown_content.append(self._table_to_markdown(table))
                            markdown_content.append("\n\n")
            
            return ''.join(markdown_content)
            
        except Exception as e:
            logger.error(f"PDF conversion error: {e}")
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
