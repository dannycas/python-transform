"""
Base class for all converters.
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseConverter(ABC):
    """Abstract base class for converters."""
    
    @abstractmethod
    def convert(self, file_path: str, **kwargs) -> Optional[str]:
        """
        Convert file to Markdown.
        
        Args:
            file_path: Path to the input file
            **kwargs: Additional parameters specific to the converter
            
        Returns:
            Markdown content or None
        """
        pass
    
    def _create_markdown_header(self, title: str, level: int = 1) -> str:
        """Create a Markdown header."""
        return f"{'#' * level} {title}\n\n"
    
    def _escape_markdown(self, text: str) -> str:
        """Escape special Markdown characters."""
        special_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
        for char in special_chars:
            text = text.replace(char, f'\\{char}')
        return text
