"""
Utility functions for python-transform.
"""

import os
import logging
from pathlib import Path
from typing import Dict, List


logger = logging.getLogger(__name__)


def setup_logging(level=logging.INFO):
    """Configure logging."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def get_supported_extensions() -> Dict[str, str]:
    """
    Return a dictionary of supported extensions and their types.
    
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
    Check if the file has a supported extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        bool: True if format is supported
    """
    ext = Path(file_path).suffix.lower()
    return ext in get_supported_extensions()


def get_all_files(directory: str, recursive: bool = False) -> List[Path]:
    """
    Get all files from a directory.
    
    Args:
        directory: Path to the directory
        recursive: Whether to search recursively
        
    Returns:
        List[Path]: List of files
    """
    dir_path = Path(directory)
    
    if not dir_path.exists():
        logger.error(f"Directory does not exist: {directory}")
        return []
    
    if recursive:
        return list(dir_path.rglob('*'))
    else:
        return list(dir_path.glob('*'))


def get_supported_files(directory: str, recursive: bool = False) -> List[Path]:
    """
    Get all supported files from a directory.
    
    Args:
        directory: Path to the directory
        recursive: Whether to search recursively
        
    Returns:
        List[Path]: List of supported files
    """
    all_files = get_all_files(directory, recursive)
    return [f for f in all_files if f.is_file() and is_supported(str(f))]


def ensure_output_dir(output_dir: str) -> Path:
    """
    Ensure that the output directory exists.
    
    Args:
        output_dir: Path to the output directory
        
    Returns:
        Path: Path to the created directory
    """
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {path}")
    return path


def format_file_size(bytes_size: int) -> str:
    """
    Format file size to a readable format.
    
    Args:
        bytes_size: Size in bytes
        
    Returns:
        str: Formatted size
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    
    return f"{bytes_size:.2f} TB"


def print_conversion_summary(total: int, successful: int, failed: int):
    """
    Print the conversion summary.
    
    Args:
        total: Total number of files
        successful: Number of successfully converted files
        failed: Number of failed conversions
    """
    print("\n" + "=" * 50)
    print("CONVERSION SUMMARY")
    print("=" * 50)
    print(f"Processed: {successful}/{total}")
    
    if failed > 0:
        print(f"Errors: {failed}")
    
    success_rate = (successful / total * 100) if total > 0 else 0
    print(f"Success rate: {success_rate:.1f}%")
    print("=" * 50 + "\n")
