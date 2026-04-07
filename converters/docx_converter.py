"""
Konwerter DOCX na Markdown.
"""

import logging
from typing import Optional
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.table import Table, _Cell
from docx.text.paragraph import Paragraph

from .base_converter import BaseConverter

logger = logging.getLogger(__name__)


class DOCXConverter(BaseConverter):
    """Konwertuje pliki DOCX na Markdown."""
    
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        """
        Konwertuje DOCX na Markdown.
        
        Args:
            file_path: Ścieżka do pliku DOCX
            
        Returns:
            Zawartość Markdown
        """
        try:
            doc = Document(file_path)
            markdown_content = []
            
            # Przetwórz każdy element dokumentu
            for element in doc.element.body:
                if isinstance(element, CT_P):
                    paragraph = Paragraph(element, doc.element.body)
                    md_text = self._process_paragraph(paragraph)
                    if md_text:
                        markdown_content.append(md_text)
                
                elif element.tag.endswith('tbl'):
                    table = Table(element, doc.element.body)
                    md_table = self._table_to_markdown(table)
                    if md_table:
                        markdown_content.append(md_table)
                        markdown_content.append("\n\n")
            
            return ''.join(markdown_content)
            
        except Exception as e:
            logger.error(f"Błąd konwersji DOCX: {e}")
            return None
    
    def _process_paragraph(self, paragraph: Paragraph) -> str:
        """Przetwórz paragraf z formatowaniem."""
        if not paragraph.text.strip():
            return ""
        
        # Określ poziom nagłówka na podstawie stylu
        style = paragraph.style.name
        level = self._get_header_level(style)
        
        # Przetwórz tekst z formatowaniem
        text_parts = []
        for run in paragraph.runs:
            if run.text.strip():
                formatted_text = self._format_run(run)
                text_parts.append(formatted_text)
        
        text = ''.join(text_parts)
        
        if level > 0:
            return f"{'#' * level} {text}\n\n"
        elif paragraph.style.name.startswith('List'):
            # Lista punktowana
            indent = len(paragraph.paragraph_format.left_indent or 0) // 100
            return f"{'  ' * indent}* {text}\n"
        else:
            return f"{text}\n\n"
    
    def _get_header_level(self, style_name: str) -> int:
        """Określ poziom nagłówka na podstawie nazwy stylu."""
        style_name_lower = style_name.lower()
        
        if 'heading 1' in style_name_lower:
            return 1
        elif 'heading 2' in style_name_lower:
            return 2
        elif 'heading 3' in style_name_lower:
            return 3
        elif 'heading 4' in style_name_lower:
            return 4
        elif 'heading 5' in style_name_lower:
            return 5
        elif 'heading 6' in style_name_lower:
            return 6
        
        return 0
    
    def _format_run(self, run) -> str:
        """Sformatuj tekst bieżący na podstawie właściwości."""
        text = run.text
        
        if run.bold:
            text = f"**{text}**"
        
        if run.italic:
            text = f"*{text}*"
        
        if run.underline:
            text = f"<u>{text}</u>"
        
        return text
    
    def _table_to_markdown(self, table: Table) -> str:
        """Konwertuje tabelę DOCX na format Markdown."""
        lines = []
        
        for row_idx, row in enumerate(table.rows):
            cells = []
            for cell in row.cells:
                # Ekstrakcja tekstu z komórki
                cell_text = ' '.join([p.text for p in cell.paragraphs]).strip()
                cells.append(cell_text)
            
            lines.append("| " + " | ".join(cells) + " |")
            
            # Dodaj separator po nagłówku
            if row_idx == 0:
                separator = "|" + "|".join(["---"] * len(cells)) + "|"
                lines.append(separator)
        
        return "\n".join(lines)
