"""
Testy integracyjne dla całego systemu konwersji.
"""

import unittest
from pathlib import Path
import tempfile
import shutil
from main import DocumentConverter
from utils import is_supported, get_supported_extensions, get_supported_files


class TestDocumentConverter(unittest.TestCase):
    """Testy dla głównej klasy DocumentConverter."""
    
    def setUp(self):
        """Przygotowanie do testów."""
        self.temp_output = tempfile.mkdtemp()
        self.converter = DocumentConverter(output_dir=self.temp_output)
    
    def test_converter_initialization(self):
        """Test inicjalizacji konwertera."""
        self.assertIsNotNone(self.converter)
        self.assertEqual(str(self.converter.output_dir), self.temp_output)
    
    def test_converter_has_supported_formats(self):
        """Test czy konwerter ma zdefiniowane obsługiwane formaty."""
        self.assertIsNotNone(self.converter.CONVERTERS)
        self.assertGreater(len(self.converter.CONVERTERS), 0)
    
    def test_pdf_in_supported_formats(self):
        """Test czy PDF jest w obsługiwanych formatach."""
        self.assertIn('.pdf', self.converter.CONVERTERS)
    
    def test_docx_in_supported_formats(self):
        """Test czy DOCX jest w obsługiwanych formatach."""
        self.assertIn('.docx', self.converter.CONVERTERS)
    
    def test_image_formats_in_supported(self):
        """Test czy formaty obrazów są obsługiwane."""
        image_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
        for fmt in image_formats:
            self.assertIn(fmt, self.converter.CONVERTERS,
                         f"Format {fmt} nie jest obsługiwany")
    
    def test_output_directory_created(self):
        """Test czy katalog wyjściowy został stworzony."""
        self.assertTrue(Path(self.temp_output).exists())
    
    def test_convert_nonexistent_file(self):
        """Test konwersji nieistniejącego pliku."""
        result = self.converter.convert_file('nonexistent.pdf')
        self.assertIsNone(result)
    
    def test_convert_unsupported_format(self):
        """Test konwersji nieobsługiwanego formatu."""
        # Stworzymy tymczasowy plik z nieobsługiwanym formatem
        temp_file = Path(self.temp_output) / 'test.txt'
        temp_file.write_text('test')
        
        result = self.converter.convert_file(str(temp_file))
        self.assertIsNone(result)
    
    def tearDown(self):
        """Clean up after tests."""
        if Path(self.temp_output).exists():
            shutil.rmtree(self.temp_output)


class TestUtilsIntegration(unittest.TestCase):
    """Testy integracyjne dla utils."""
    
    def setUp(self):
        """Przygotowanie do testów."""
        self.temp_dir = tempfile.mkdtemp()
    
    def test_get_supported_extensions(self):
        """Test pobierania obsługiwanych rozszerzeń."""
        extensions = get_supported_extensions()
        
        self.assertIsNotNone(extensions)
        self.assertIsInstance(extensions, dict)
        self.assertGreater(len(extensions), 0)
    
    def test_supported_extensions_have_types(self):
        """Test czy rozszerzenia mają przypisane typy."""
        extensions = get_supported_extensions()
        
        for ext, ext_type in extensions.items():
            self.assertIn('.', ext)
            self.assertIn(ext_type, ['document', 'image'])
    
    def test_is_supported_case_insensitive(self):
        """Test czy sprawdzanie obsługiwaności jest case-insensitive."""
        self.assertTrue(is_supported('document.PDF'))
        self.assertTrue(is_supported('DOCUMENT.DOCX'))
        self.assertTrue(is_supported('image.PNG'))
    
    def test_ensure_output_dir(self):
        """Test stworzenia katalogu wyjściowego."""
        from utils import ensure_output_dir
        
        new_dir = Path(self.temp_dir) / 'nested' / 'output' / 'dir'
        result = ensure_output_dir(str(new_dir))
        
        self.assertTrue(result.exists())
    
    def test_format_file_size(self):
        """Test formatowania rozmiaru pliku."""
        from utils import format_file_size
        
        # Testowanie różnych rozmiarów
        self.assertEqual(format_file_size(512), '512.00 B')
        self.assertEqual(format_file_size(1024), '1.00 KB')
        self.assertEqual(format_file_size(1024 * 1024), '1.00 MB')
    
    def test_get_supported_files_empty_directory(self):
        """Test pobierania obsługiwanych plików z pustego katalogu."""
        files = get_supported_files(self.temp_dir)
        self.assertEqual(len(files), 0)
    
    def test_get_supported_files_with_mixed_formats(self):
        """Test pobierania obsługiwanych plików ze zmieszanymi formatami."""
        # Stworzymy kilka plików
        (Path(self.temp_dir) / 'test.pdf').touch()
        (Path(self.temp_dir) / 'test.docx').touch()
        (Path(self.temp_dir) / 'test.txt').touch()
        (Path(self.temp_dir) / 'test.png').touch()
        
        files = get_supported_files(self.temp_dir)
        
        # Powinno być 3 obsługiwane pliki (bez .txt)
        self.assertEqual(len(files), 3)
    
    def tearDown(self):
        """Clean up after tests."""
        if Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir)


class TestConverterIntegration(unittest.TestCase):
    """Testy integracyjne konwerterów."""
    
    def test_all_converters_exist(self):
        """Test czy wszystkie konwertery można zaimportować."""
        from converters import PDFConverter, DOCXConverter, ImageConverter, BaseConverter
        
        self.assertIsNotNone(PDFConverter)
        self.assertIsNotNone(DOCXConverter)
        self.assertIsNotNone(ImageConverter)
        self.assertIsNotNone(BaseConverter)
    
    def test_converters_are_subclasses_of_base(self):
        """Test czy wszystkie konwertery dziedziczą z BaseConverter."""
        from converters import PDFConverter, DOCXConverter, ImageConverter, BaseConverter
        
        pdf_converter = PDFConverter()
        docx_converter = DOCXConverter()
        image_converter = ImageConverter()
        
        self.assertIsInstance(pdf_converter, BaseConverter)
        self.assertIsInstance(docx_converter, BaseConverter)
        self.assertIsInstance(image_converter, BaseConverter)
    
    def test_converters_have_convert_method(self):
        """Test czy wszystkie konwertery mają metodę convert."""
        from converters import PDFConverter, DOCXConverter, ImageConverter
        
        converters = [PDFConverter(), DOCXConverter(), ImageConverter()]
        
        for converter in converters:
            self.assertTrue(hasattr(converter, 'convert'))
            self.assertTrue(callable(getattr(converter, 'convert')))


class TestConfigurationModule(unittest.TestCase):
    """Testy dla modułu konfiguracji."""
    
    def test_config_import(self):
        """Test czy można importować config."""
        try:
            from config import ConversionConfig, get_config
            self.assertIsNotNone(ConversionConfig)
            self.assertIsNotNone(get_config)
        except ImportError:
            self.fail("Nie można zaimportować config")
    
    def test_config_default(self):
        """Test konfiguracji domyślnej."""
        from config import get_config
        
        config = get_config('default')
        self.assertIsNotNone(config)
        self.assertEqual(config.output_dir, './output')
    
    def test_config_fast(self):
        """Test konfiguracji szybkiej."""
        from config import get_config
        
        config = get_config('fast')
        self.assertFalse(config.pdf_extract_images)
        self.assertFalse(config.image_use_ocr)
    
    def test_config_full(self):
        """Test konfiguracji pełnej."""
        from config import get_config
        
        config = get_config('full')
        self.assertTrue(config.image_use_ocr)
        self.assertTrue(config.markdown_include_metadata)


if __name__ == '__main__':
    unittest.main()
