"""
Klasa bazowa dla wszystkich konwerterów.
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseConverter(ABC):
    """Abstrakcyjna klasa bazowa dla konwerterów."""
    
    @abstractmethod
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        """
        Konwertuje plik na Markdown.
        
        Args:
            file_path: Ścieżka do pliku wejściowego
            **kwargs: Dodatkowe parametry specyficzne dla konwertera
            
        Returns:
            Zawartość Markdown lub None
        """
        pass
    
    def _create_markdown_header(self, title: str, level: int = 1) -> str:
        """Tworzy nagłówek Markdown."""
        return f"{'#' * level} {title}\n\n"
    
    def _escape_markdown(self, text: str) -> str:
        """Escapeuje znaki specjalne Markdown."""
        special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
        for char in special_chars:
            text = text.replace(char, f'\\{char}')
        return text
