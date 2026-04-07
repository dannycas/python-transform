"""
Utility functions for python-transform.
"""

import os
import logging
from pathlib import Path
from typing import Dict, List


logger = logging.getLogger(__name__)


def setup_logging(level=logging.INFO):
    """Skonfiguruj logging."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def get_supported_extensions() -> Dict[str, str]:
    """
    Zwraca słownik obsługiwanych rozszerzeń i ich typów.
    
    Returns:
        Dict[str, str]: {'extension': 'type', ...}
    """
    return {
        '.pdf': 'document',
        '.docx': 'document',
        '.doc': 'document',
        '.png': 'image',
        '.jpg': 'image',
        '.jpeg': 'image',
        '.bmp': 'image',
        '.gif': 'image',
        '.tiff': 'image',
        '.webp': 'image',
    }


def is_supported(file_path: str) -> bool:
    """
    Sprawdź czy plik ma obsługiwane rozszerzenie.
    
    Args:
        file_path: Ścieżka do pliku
        
    Returns:
        bool: True jeśli format jest obsługiwany
    """
    ext = Path(file_path).suffix.lower()
    return ext in get_supported_extensions()


def get_all_files(directory: str, recursive: bool = False) -> List[Path]:
    """
    Pobierz wszystkie pliki z katalogu.
    
    Args:
        directory: Ścieżka do katalogu
        recursive: Czy szukać rekursywnie
        
    Returns:
        List[Path]: Lista plików
    """
    dir_path = Path(directory)
    
    if not dir_path.exists():
        logger.error(f"Katalog nie istnieje: {directory}")
        return []
    
    if recursive:
        return list(dir_path.rglob('*'))
    else:
        return list(dir_path.glob('*'))


def get_supported_files(directory: str, recursive: bool = False) -> List[Path]:
    """
    Pobierz wszystkie obsługiwane pliki z katalogu.
    
    Args:
        directory: Ścieżka do katalogu
        recursive: Czy szukać rekursywnie
        
    Returns:
        List[Path]: Lista obsługiwanych plików
    """
    all_files = get_all_files(directory, recursive)
    return [f for f in all_files if f.is_file() and is_supported(str(f))]


def ensure_output_dir(output_dir: str) -> Path:
    """
    Upewnij się że katalog wyjściowy istnieje.
    
    Args:
        output_dir: Ścieżka do katalogu wyjściowego
        
    Returns:
        Path: Ścieżka do stworzonym katalogu
    """
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {path}")
    return path


def format_file_size(bytes_size: int) -> str:
    """
    Sformatuj rozmiar pliku na czytelny format.
    
    Args:
        bytes_size: Rozmiar w bajtach
        
    Returns:
        str: Sformatowany rozmiar
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    
    return f"{bytes_size:.2f} TB"


def print_conversion_summary(total: int, successful: int, failed: int):
    """
    Wydrukuj podsumowanie konwersji.
    
    Args:
        total: Całkowita liczba plików
        successful: Liczba pomyślnie skonwertowanych
        failed: Liczba nieudanychkonwersji
    """
    print("\n" + "=" * 50)
    print("PODSUMOWANIE KONWERSJI")
    print("=" * 50)
    print(f"Zmapowanie: {successful}/{total}")
    
    if failed > 0:
        print(f"Błędy: {failed}")
    
    success_rate = (successful / total * 100) if total > 0 else 0
    print(f"Wskaźnik sukcesu: {success_rate:.1f}%")
    print("=" * 50 + "\n")
