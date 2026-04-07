"""
Konwerter PDF na Markdown.
"""

import logging
from typing import Optional
import pdfplumber

from .base_converter import BaseConverter

logger = logging.getLogger(__name__)


class PDFConverter(BaseConverter):
    """Konwertuje pliki PDF na Markdown."""
    
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        """
        Konwertuje PDF na Markdown.
        
        Args:
            file_path: Ścieżka do pliku PDF
            
        Returns:
            Zawartość Markdown
        """
        try:
            markdown_content = []
            
            with pdfplumber.open(file_path) as pdf:
                # Dodaj informacje o dokumencie
                markdown_content.append(f"# PDF Document\n")
                markdown_content.append(f"**Liczba stron:** {len(pdf.pages)}\n\n")
                
                # Przetwórz każdą stronę
                for page_num, page in enumerate(pdf.pages, 1):
                    # Nagłówek strony
                    markdown_content.append(f"## Strona {page_num}\n\n")
                    
                    # Ekstrakcja tekstu
                    text = page.extract_text()
                    if text:
                        markdown_content.append(text)
                        markdown_content.append("\n\n")
                    
                    # Ekstrakcja tabel
                    tables = page.extract_tables()
                    if tables:
                        for table_num, table in enumerate(tables, 1):
                            markdown_content.append(f"### Tabela {table_num}\n\n")
                            markdown_content.append(self._table_to_markdown(table))
                            markdown_content.append("\n\n")
            
            return ''.join(markdown_content)
            
        except Exception as e:
            logger.error(f"Błąd konwersji PDF: {e}")
            return None
    
    def _table_to_markdown(self, table: list) -> str:
        """Konwertuje tabelę na format Markdown."""
        if not table or not table[0]:
            return ""
        
        lines = []
        
        for row_idx, row in enumerate(table):
            # Konwertuj None na pusty string
            row_cells = [str(cell) if cell is not None else "" for cell in row]
            lines.append("| " + " | ".join(row_cells) + " |")
            
            # Dodaj separator po nagłówku (pierwszy wiersz)
            if row_idx == 0:
                separator = "|" + "|".join(["---"] * len(row)) + "|"
                lines.append(separator)
        
        return "\n".join(lines)
